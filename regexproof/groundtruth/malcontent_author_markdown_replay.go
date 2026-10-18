// This command is run from an exact pinned Malcontent checkout by
// malcontent_author_markdown_replay.py. It exercises the real YARA-X metadata
// parser, Malcontent report generator, and Markdown renderer.
package main

import (
	"bytes"
	"context"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	yarax "github.com/VirusTotal/yara-x/go"
	"github.com/chainguard-dev/malcontent/pkg/malcontent"
	"github.com/chainguard-dev/malcontent/pkg/programkind"
	"github.com/chainguard-dev/malcontent/pkg/render"
	"github.com/chainguard-dev/malcontent/pkg/report"
)

type result struct {
	RuleName     string `json:"rule_name"`
	Author       string `json:"author"`
	AuthorURL    string `json:"author_url"`
	ReferenceURL string `json:"reference_url"`
	Markdown     string `json:"markdown"`
	InputSHA256  string `json:"input_sha256"`
}

func main() {
	author := os.Getenv("MALCONTENT_AUTHOR_METADATA")
	if author == "" {
		fatal("MALCONTENT_AUTHOR_METADATA is required")
	}

	ruleSource := fmt.Sprintf(`rule regexproof_author_metadata_replay {
	meta:
		author = %s
		ref = "https://reference.invalid"
		description = "metadata replay"
	strings:
		$needle = "regexproof-replay-sentinel"
	condition:
		$needle
}
`, strconv.Quote(author))

	compiler, err := yarax.NewCompiler()
	if err != nil {
		fatal("create YARA-X compiler: %v", err)
	}
	if err := compiler.AddSource(ruleSource); err != nil {
		fatal("compile YARA metadata fixture: %v", err)
	}
	if errors := compiler.Errors(); len(errors) != 0 {
		fatal("YARA-X reported compiler errors: %v", errors)
	}
	rules := compiler.Build()
	scanner := yarax.NewScanner(rules)
	target := []byte("regexproof-replay-sentinel")
	scanResults, err := scanner.Scan(target)
	if err != nil {
		fatal("scan YARA metadata fixture: %v", err)
	}
	if len(scanResults.MatchingRules()) != 1 {
		fatal("expected one matching YARA rule, got %d", len(scanResults.MatchingRules()))
	}

	sum := sha256.Sum256(target)
	fileReport, err := report.Generate(
		context.Background(),
		"sample.bin",
		scanResults,
		malcontent.Config{},
		"",
		nil,
		target,
		int64(len(target)),
		hex.EncodeToString(sum[:]),
		(*programkind.FileType)(nil),
		0,
	)
	if err != nil {
		fatal("generate Malcontent report: %v", err)
	}
	if len(fileReport.Behaviors) != 1 || fileReport.Behaviors[0] == nil {
		fatal("expected one generated behavior, got %d", len(fileReport.Behaviors))
	}

	var markdown bytes.Buffer
	if err := render.NewMarkdown(&markdown).File(context.Background(), fileReport); err != nil {
		fatal("render Malcontent Markdown: %v", err)
	}

	inputSum := sha256.Sum256([]byte(author))
	out := result{
		RuleName:     scanResults.MatchingRules()[0].Identifier(),
		Author:       fileReport.Behaviors[0].RuleAuthor,
		AuthorURL:    fileReport.Behaviors[0].RuleAuthorURL,
		ReferenceURL: fileReport.Behaviors[0].ReferenceURL,
		Markdown:     markdown.String(),
		InputSHA256:  hex.EncodeToString(inputSum[:]),
	}
	if err := json.NewEncoder(os.Stdout).Encode(out); err != nil {
		fatal("encode replay result: %v", err)
	}
}

func fatal(format string, args ...any) {
	fmt.Fprintf(os.Stderr, format+"\n", args...)
	os.Exit(2)
}
