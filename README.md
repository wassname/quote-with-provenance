# quote-with-provenance

An agent skill for quoting sources faithfully in Markdown. Quotes follow [Wikipedia's quotation rules](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Quotations): `...` for cuts, `[brackets]` for the editor's words, small typos fixed. An HTML comment holds the source and the exact original passage, so the raw file shows what changed and the rendered page does not.

## Example

Original ([Seneca, *On Anger* III.12, trans. John W. Basore, p. 285](https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html)):

> Plato once, when he was angry with his slave, was unable to impose delay upon himself, and, bent upon flogging him with his own hand, ordered him forthwith to take off his shirt and bare his shoulders for the blows; but afterwards realizing that he was angry he stayed his uplifted hand, and just as he was stood with his band in the air like one in the act of striking. Later, when a friend who happened to come in asked him what he was doing, he said, "I am exacting punishment from an angry man."

Quote with metadata:

```md
<!--
{"source_url":"https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html",
"author":"Seneca",
"work":"Moral Essays, Volume I, On Anger",
"translator":"John W. Basore",
"edition":"Loeb Classical Library, 1928–1935",
"locator":"On Anger III.12, p. 285","editor":"PI/Claude",
"original":"Plato once, when he was angry with his slave, was unable to impose delay upon himself, and, bent upon flogging him with his own hand, ordered him forthwith to take off his shirt and bare his shoulders for the blows; but afterwards realizing that he was angry he stayed his uplifted hand, and just as he was stood with his band in the air like one in the act of striking. Later, when a friend who happened to come in asked him what he was doing, he said, \"I am exacting punishment from an angry man.\"",
"fixed":{"band":"hand"}}
-->

> Plato once, when he was angry with his slave, ... bent upon flogging him with his own hand, ordered him [at once] to ... bare his shoulders for the blows;
> but ... realizing that he was angry he [held back] his uplifted hand, and ... stood with his hand in the air like one in the act of striking.
> Later, when a friend ... asked him what he was doing, [Plato] said, "I am [punishing] an angry man."

Seneca, *On Anger* III.12, trans. John W. Basore, p. 285.
```

Quote rendered:

> Plato once, when he was angry with his slave, ... bent upon flogging him with his own hand, ordered him [at once] to ... bare his shoulders for the blows;
> but ... realizing that he was angry he [held back] his uplifted hand, and ... stood with his hand in the air like one in the act of striking.
> Later, when a friend ... asked him what he was doing, [Plato] said, "I am [punishing] an angry man."

Seneca, *On Anger* III.12, trans. John W. Basore, p. 285.

Comparing the quote with `original` shows each cut and substitution. `fixed` records the one change the reader cannot see: the scan error `band` → `hand`.

## Install

Clone into your agent's skills folder, e.g. for Claude Code:

```sh
git clone https://github.com/wassname/quote-with-provenance.git ~/.claude/skills/quote-with-provenance
```

If your skills folder is a git repo, add it as a submodule instead:

```sh
cd ~/.claude/skills
git submodule add https://github.com/wassname/quote-with-provenance.git quote-with-provenance
git commit -m "Add quote-with-provenance skill"
```

Or with [vercel-labs/skills](https://github.com/vercel-labs/skills): `npx skills add wassname/quote-with-provenance`. Or copy [SKILL.md](SKILL.md). MIT license.
