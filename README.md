# Quote with provenance

An LLM skill for source-faithful quotations in Markdown. It follows [Wikipedia's quotation conventions](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Quotations) and adds source details and exact edit records in HTML comments.

The rendered text uses ordinary quotation marks, square brackets and ellipses. The raw Markdown also records the source URL, edition, locator, editor, and the original words behind each edit. Comments are deliberately public but do not appear in the rendered reading.

For example, the raw Markdown can contain:

```md
[her father]<!--{"type":"edit","op":"replace","original":"him","rendered":"[her father]","reason":"The preceding source sentence identifies him."}-->
```

The reader sees `[her father]`; an auditor can also see that it replaced `him` and why. The [complete Seneca example](examples/seneca.md) shows source attribution, internal omissions and a two-sentence scenario extraction.

## Use

Read [SKILL.md](SKILL.md), or install this directory as an [Agent Skill](https://agentskills.io/specification). It needs no API, package installation or executable code. The [metadata format](references/metadata.md) specifies the comments.

To track it in an existing private skills repository:

```sh
git -C /path/to/private-skills-repo submodule add \
  https://github.com/wassname/quote-with-provenance.git skills/quote-with-provenance
```

Keep the comments when edit history is needed. A rendered-only copy can remove them and retain a conventional quotation.

## Basis and scope

This is a complete procedure for selecting, editing, attributing and checking a quotation, including short scenario extraction. It adds metadata to Wikipedia's visible conventions; it is not a new quotation standard endorsed by Wikipedia. The linked style guide remains the reference for quotation rules. This skill does not require quoting a source more extensively than the task needs.

Wikipedia provides a detailed, publicly accessible rule set. The metadata format is specified here rather than left to a model's interpretation of the style guide. Exact edit records help an auditor check a quotation; they do not prove that its selection or wording preserves the source's meaning.

Related projects solve different problems: [Verbatim](https://github.com/KRLabsOrg/verbatim-skill) offers API-based cited extraction; [citation-check-skill](https://github.com/serenakeyitan/citation-check-skill) audits claims; [markdown-provenance](https://github.com/rickmanelius/markdown-provenance) records file authenticity. No code or skill text from those projects is bundled here.

## License and authorship

MIT for this project's instructions and examples' editorial material. Quoted source passages retain their original attribution and rights.

Created with wassname's direction; written by PI/OpenAI. Wikipedia supplies the quotation conventions, not the JSON-in-comments extension.
