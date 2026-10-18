package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net"
	"net/http"
	"strings"
	"time"
)

type replayResult struct {
	Case       string `json:"case"`
	Status     string `json:"status"`
	HandlerRan bool   `json:"handler_ran"`
	Origin     string `json:"origin,omitempty"`
	Injected   string `json:"injected_header,omitempty"`
	HasCRLF    bool   `json:"origin_contains_crlf,omitempty"`
}

func replay(name, raw string) replayResult {
	listener, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		panic(err)
	}
	seen := make(chan replayResult, 1)
	server := &http.Server{Handler: http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		origin := r.Header.Get("Origin")
		seen <- replayResult{
			Case:       name,
			HandlerRan: true,
			Origin:     origin,
			Injected:   r.Header.Get("X-Injected"),
			HasCRLF:    strings.ContainsAny(origin, "\r\n"),
		}
		w.Header().Set("Connection", "close")
		w.WriteHeader(http.StatusNoContent)
	})}
	go func() { _ = server.Serve(listener) }()

	conn, err := net.DialTimeout("tcp", listener.Addr().String(), time.Second)
	if err != nil {
		_ = server.Close()
		panic(err)
	}
	_ = conn.SetDeadline(time.Now().Add(2 * time.Second))
	if _, err := fmt.Fprint(conn, raw); err != nil {
		_ = conn.Close()
		_ = server.Close()
		panic(err)
	}
	status, err := bufio.NewReader(conn).ReadString('\n')
	_ = conn.Close()
	_ = server.Close()
	if err != nil {
		return replayResult{Case: name, Status: "no-response: " + err.Error()}
	}
	status = strings.TrimSpace(status)
	select {
	case result := <-seen:
		result.Status = status
		return result
	default:
		return replayResult{Case: name, Status: status, HandlerRan: false}
	}
}

func main() {
	base := "GET / HTTP/1.1\r\nHost: example.test\r\n%sConnection: close\r\n\r\n"
	cases := []struct{ name, headers string }{
		{"ordinary", "Origin: https://good.example\r\n"},
		{"obs_fold", "Origin: https://fold.example\r\n X-Injected: yes\r\n"},
		{"separate_header_after_origin", "Origin: https://split.example\r\nX-Injected: yes\r\n"},
		{"bare_lf_inside_origin", "Origin: https://lf.example\nX-Injected: yes\r\n"},
		{"bare_cr_inside_origin", "Origin: https://cr.example\rX-Injected: yes\r\n"},
		{"repeated_origin", "Origin: https://first.example\r\nOrigin: https://second.example\r\n"},
	}
	results := make([]replayResult, 0, len(cases))
	for _, item := range cases {
		results = append(results, replay(item.name, fmt.Sprintf(base, item.headers)))
	}
	for _, result := range results {
		encoded, err := json.Marshal(result)
		if err != nil {
			panic(err)
		}
		fmt.Println(string(encoded))
	}
}
