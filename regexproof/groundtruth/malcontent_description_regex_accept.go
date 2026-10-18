package main

import (
	"bufio"
	"io"
	"os"
	"regexp"
)

var descriptionPattern = regexp.MustCompile(`Detection patterns for the tool '(.*)' taken from the ThreatHunting-Keywords github project`)

func main() {
	input, err := io.ReadAll(bufio.NewReader(os.Stdin))
	if err != nil {
		os.Exit(2)
	}
	if descriptionPattern.FindStringSubmatch(string(input)) == nil {
		os.Exit(1)
	}
}
