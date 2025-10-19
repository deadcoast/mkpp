# Revisions for .markdownlint config

## `MD033` - Inline HTML

Tags: `html`

Aliases: `no-inline-html`

Parameters:

- `allowed_elements`: Allowed elements (`string[]`, default `[]`)

This rule is triggered whenever raw HTML is used in a Markdown document:

```markdown
<h1>Inline HTML heading</h1>
```

To fix this, use 'pure' Markdown instead of including raw HTML:

```markdown
# Markdown heading
```

Note: To allow specific HTML elements, use the `allowed_elements` parameter.

Rationale: Raw HTML is allowed in Markdown, but this rule is included for
those who want their documents to only include "pure" Markdown, or for those
who are rendering Markdown documents into something other than HTML.

```json
{
	"resource": "/c:/Users/ryanf/github/mkpp/README.md",
	"owner": "markdownlint",
	"code": {
		"value": "MD033",
		"target": {
			"$mid": 1,
			"path": "/DavidAnson/markdownlint/blob/v0.38.0/doc/md033.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "MD033/no-inline-html: Inline HTML [Element: div]",
	"source": "markdownlint",
	"startLineNumber": 3,
	"startColumn": 1,
	"endLineNumber": 3,
	"endColumn": 21,
	"origin": "extHost1"
}
```

---

## `MD036` - Emphasis used instead of a heading

Tags: `emphasis`, `headings`

Aliases: `no-emphasis-as-heading`

Parameters:

- `punctuation`: Punctuation characters (`string`, default `.,;:!?。，；：！？`)

This check looks for instances where emphasized (i.e. bold or italic) text is
used to separate sections, where a heading should be used instead:

```markdown
**My document**

Lorem ipsum dolor sit amet...

_Another section_

Consectetur adipiscing elit, sed do eiusmod.
```

To fix this, use Markdown headings instead of emphasized text to denote
sections:

```markdown
# My document

Lorem ipsum dolor sit amet...

## Another section

Consectetur adipiscing elit, sed do eiusmod.
```

Note: This rule looks for single-line paragraphs that consist entirely
of emphasized text. It won't fire on emphasis used within regular text,
multi-line emphasized paragraphs, or paragraphs ending in punctuation
(normal or full-width). Similarly to rule MD026, you can configure what
characters are recognized as punctuation.

Rationale: Using emphasis instead of a heading prevents tools from inferring
the structure of a document. More information:
<https://cirosantilli.com/markdown-style-guide#emphasis-vs-headers>.

```json
{
	"resource": "/c:/Users/ryanf/github/mkpp/README.md",
	"owner": "markdownlint",
	"code": {
		"value": "MD036",
		"target": {
			"$mid": 1,
			"path": "/DavidAnson/markdownlint/blob/v0.38.0/doc/md036.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "MD036/no-emphasis-as-heading: Emphasis used instead of a heading",
	"source": "markdownlint",
	"startLineNumber": 5,
	"startColumn": 1,
	"endLineNumber": 5,
	"endColumn": 45,
	"origin": "extHost1"
}
```

---

MD013 - Line length
Tags: line_length

Aliases: line-length

Parameters:

code_block_line_length: Number of characters for code blocks (integer, default 80)
code_blocks: Include code blocks (boolean, default true)
heading_line_length: Number of characters for headings (integer, default 80)
headings: Include headings (boolean, default true)
line_length: Number of characters (integer, default 80)
stern: Stern length checking (boolean, default false)
strict: Strict length checking (boolean, default false)
tables: Include tables (boolean, default true)
This rule is triggered when there are lines that are longer than the configured line_length (default: 80 characters). To fix this, split the line up into multiple lines. To set a different maximum length for headings, use heading_line_length. To set a different maximum length for code blocks, use code_block_line_length

This rule has an exception when there is no whitespace beyond the configured line length. This allows you to include items such as long URLs without being forced to break them in the middle. To disable this exception, set the strict parameter to true and an issue will be reported when any line is too long. To warn for lines that are too long and could be fixed but allow long lines without spaces, set the stern parameter to true.

For example (assuming normal behavior):

IF THIS LINE IS THE MAXIMUM LENGTH
This line is okay because there are-no-spaces-beyond-that-length
This line is a violation because there are spaces beyond that length
This-line-is-okay-because-there-are-no-spaces-anywhere-within
In strict mode, the last three lines above are all violations. In stern mode, the middle two lines above are both violations, but the last is okay.

You have the option to exclude this rule for code blocks, tables, or headings. To do so, set the code_blocks, tables, or headings parameter(s) to false.

Code blocks are included in this rule by default since it is often a requirement for document readability, and tentatively compatible with code rules. Still, some languages do not lend themselves to short lines.

Lines with link/image reference definitions and standalone lines (i.e., not part of a paragraph) with only a link/image (possibly using (strong) emphasis) are always exempted from this rule (even in strict mode) because there is often no way to split such lines without breaking the URL.

Rationale: Extremely long lines can be difficult to work with in some editors. More information: <https://cirosantilli.com/markdown-style-guide#line-wrapping>.

```json
{
	"resource": "/c:/Users/ryanf/github/mkpp/README.md",
	"owner": "markdownlint",
	"code": {
		"value": "MD013",
		"target": {
			"$mid": 1,
			"path": "/DavidAnson/markdownlint/blob/v0.38.0/doc/md013.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "MD013/line-length: Line length [Expected: 80; Actual: 154]",
	"source": "markdownlint",
	"startLineNumber": 7,
	"startColumn": 81,
	"endLineNumber": 7,
	"endColumn": 155,
	"origin": "extHost1"
}
```

---

## `MD051` - Link fragments should be valid

Tags: `links`

Aliases: `link-fragments`

Parameters:

- `ignore_case`: Ignore case of fragments (`boolean`, default `false`)
- `ignored_pattern`: Pattern for ignoring additional fragments (`string`,
  default ``)

Fixable: Some violations can be fixed by tooling

This rule is triggered when a link fragment does not match any of the fragments
that are automatically generated for headings in a document:

```markdown
# Heading Name

[Link](#fragment)
```

To fix this issue, change the link fragment to reference an existing heading's
generated name (see below):

```markdown
# Heading Name

[Link](#heading-name)
```

For consistency, this rule requires fragments to exactly match the [GitHub
heading algorithm][github-heading-algorithm] which converts letters to
lowercase. Therefore, the following example is reported as a violation:

```markdown
# Heading Name

[Link](#Heading-Name)
```

To ignore case when comparing fragments with heading names, the `ignore_case`
parameter can be set to `true`. In this configuration, the previous example is
not reported as a violation.

Alternatively, some platforms allow the syntax `{#named-anchor}` to be used
within a heading to provide a specific name (consisting of only lower-case
letters, numbers, `-`, and `_`):

```markdown
# Heading Name {#custom-name}

[Link](#custom-name)
```

Alternatively, any HTML tag with an `id` attribute or an `a` tag with a `name`
attribute can be used to define a fragment:

```markdown
<a id="bookmark"></a>

[Link](#bookmark)
```

An `a` tag can be useful in scenarios where a heading is not appropriate or for
control over the text of the fragment identifier.

[HTML links to `#top` scroll to the top of a document][html-top-fragment]. This
rule allows that syntax (using lower-case for consistency):

```markdown
[Link](#top)
```

This rule also recognizes the custom fragment syntax used by GitHub to highlight
[specific content in a document][github-linking-to-content].

For example, this link to line 20:

```markdown
[Link](#L20)
```

And this link to content starting within line 19 running into line 21:

```markdown
[Link](#L19C5-L21C11)
```

Some Markdown generators dynamically create and insert headings when building
documents, for example by combining a fixed prefix like `figure-` and an
incrementing numeric counter. To ignore such generated fragments, set the
`ignored_pattern` [regular expression][RegEx] parameter to a pattern that
matches (e.g., `^figure-`).

Rationale: [GitHub section links][github-section-links] are created
automatically for every heading when Markdown content is displayed on GitHub.
This makes it easy to link directly to different sections within a document.
However, section links change if headings are renamed or removed. This rule
helps identify broken section links within a document.

Section links are **not** part of the CommonMark specification. This rule
enforces the [GitHub heading algorithm][github-heading-algorithm] which is:
convert heading to lowercase, remove punctuation, convert spaces to dashes,
append an incrementing integer as needed for uniqueness.

[github-section-links]: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links
[github-heading-algorithm]: https://github.com/gjtorikian/html-pipeline/blob/f13a1534cb650ba17af400d1acd3a22c28004c09/lib/html/pipeline/toc_filter.rb
[github-linking-to-content]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-a-permanent-link-to-a-code-snippet#linking-to-markdown#linking-to-markdown
[html-top-fragment]: https://html.spec.whatwg.org/multipage/browsing-the-web.html#scrolling-to-a-fragment
[RegEx]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions

```json
{
	"resource": "/c:/Users/ryanf/github/mkpp/README.md",
	"owner": "markdownlint",
	"code": {
		"value": "MD051",
		"target": {
			"$mid": 1,
			"path": "/DavidAnson/markdownlint/blob/v0.38.0/doc/md051.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "MD051/link-fragments: Link fragments should be valid",
	"source": "markdownlint",
	"startLineNumber": 14,
	"startColumn": 51,
	"endLineNumber": 14,
	"endColumn": 81,
	"origin": "extHost1"
}
```

---

## `MD013` - Line length

Tags: `line_length`

Aliases: `line-length`

Parameters:

- `code_block_line_length`: Number of characters for code blocks (`integer`,
  default `80`)
- `code_blocks`: Include code blocks (`boolean`, default `true`)
- `heading_line_length`: Number of characters for headings (`integer`, default
  `80`)
- `headings`: Include headings (`boolean`, default `true`)
- `line_length`: Number of characters (`integer`, default `80`)
- `stern`: Stern length checking (`boolean`, default `false`)
- `strict`: Strict length checking (`boolean`, default `false`)
- `tables`: Include tables (`boolean`, default `true`)

This rule is triggered when there are lines that are longer than the
configured `line_length` (default: 80 characters). To fix this, split the line
up into multiple lines. To set a different maximum length for headings, use
`heading_line_length`. To set a different maximum length for code blocks, use
`code_block_line_length`

This rule has an exception when there is no whitespace beyond the configured
line length. This allows you to include items such as long URLs without being
forced to break them in the middle. To disable this exception, set the `strict`
parameter to `true` and an issue will be reported when any line is too long. To
warn for lines that are too long and could be fixed but allow long lines
without spaces, set the `stern` parameter to `true`.

For example (assuming normal behavior):

```markdown
IF THIS LINE IS THE MAXIMUM LENGTH
This line is okay because there are-no-spaces-beyond-that-length
This line is a violation because there are spaces beyond that length
This-line-is-okay-because-there-are-no-spaces-anywhere-within
```

In `strict` mode, the last three lines above are all violations. In `stern`
mode, the middle two lines above are both violations, but the last is okay.

You have the option to exclude this rule for code blocks, tables, or headings.
To do so, set the `code_blocks`, `tables`, or `headings` parameter(s) to false.

Code blocks are included in this rule by default since it is often a
requirement for document readability, and tentatively compatible with code
rules. Still, some languages do not lend themselves to short lines.

Lines with link/image reference definitions and standalone lines (i.e., not part
of a paragraph) with only a link/image (possibly using (strong) emphasis) are
always exempted from this rule (even in `strict` mode) because there is often no
way to split such lines without breaking the URL.

Rationale: Extremely long lines can be difficult to work with in some editors.
More information: <https://cirosantilli.com/markdown-style-guide#line-wrapping>.

```json
{
	"resource": "/c:/Users/ryanf/github/mkpp/README.md",
	"owner": "markdownlint",
	"code": {
		"value": "MD013",
		"target": {
			"$mid": 1,
			"path": "/DavidAnson/markdownlint/blob/v0.38.0/doc/md013.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "MD013/line-length: Line length [Expected: 80; Actual: 112]",
	"source": "markdownlint",
	"startLineNumber": 14,
	"startColumn": 81,
	"endLineNumber": 14,
	"endColumn": 113,
	"origin": "extHost1"
}
```

---

## `MD040` - Fenced code blocks should have a language specified

Tags: `code`, `language`

Aliases: `fenced-code-language`

Parameters:

- `allowed_languages`: List of languages (`string[]`, default `[]`)
- `language_only`: Require language only (`boolean`, default `false`)

This rule is triggered when fenced code blocks are used, but a language isn't
specified:

````markdown
```
#!/bin/bash
echo Hello world
```
````

To fix this, add a language specifier to the code block:

````markdown
```bash
#!/bin/bash
echo Hello world
```
````

To display a code block without syntax highlighting, use:

````markdown
```text
Plain text in a code block
```
````

You can configure the `allowed_languages` parameter to specify a list of
languages code blocks could use. Languages are case sensitive. The default value
is `[]` which means any language specifier is valid.

You can prevent extra data from being present in the info string of fenced code
blocks. To do so, set the `language_only` parameter to `true`.

<!-- markdownlint-disable-next-line no-space-in-code -->
Info strings with leading/trailing whitespace (ex: `js `) or other content (ex:
`ruby startline=3`) will trigger this rule.

Rationale: Specifying a language improves content rendering by using the
correct syntax highlighting for code. More information:
<https://cirosantilli.com/markdown-style-guide#option-code-fenced>.

---

## `MD040` - Fenced code blocks should have a language specified

Tags: `code`, `language`

Aliases: `fenced-code-language`

Parameters:

- `allowed_languages`: List of languages (`string[]`, default `[]`)
- `language_only`: Require language only (`boolean`, default `false`)

This rule is triggered when fenced code blocks are used, but a language isn't
specified:

````markdown
```
#!/bin/bash
echo Hello world
```
````

To fix this, add a language specifier to the code block:

````markdown
```bash
#!/bin/bash
echo Hello world
```
````

To display a code block without syntax highlighting, use:

````markdown
```text
Plain text in a code block
```
````

You can configure the `allowed_languages` parameter to specify a list of
languages code blocks could use. Languages are case sensitive. The default value
is `[]` which means any language specifier is valid.

You can prevent extra data from being present in the info string of fenced code
blocks. To do so, set the `language_only` parameter to `true`.

<!-- markdownlint-disable-next-line no-space-in-code -->
Info strings with leading/trailing whitespace (ex: `js `) or other content (ex:
`ruby startline=3`) will trigger this rule.

Rationale: Specifying a language improves content rendering by using the
correct syntax highlighting for code. More information:
<https://cirosantilli.com/markdown-style-guide#option-code-fenced>.

```json
{
	"resource": "/c:/Users/ryanf/github/mkpp/README.md",
	"owner": "markdownlint",
	"code": {
		"value": "MD040",
		"target": {
			"$mid": 1,
			"path": "/DavidAnson/markdownlint/blob/v0.38.0/doc/md040.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "MD040/fenced-code-language: Fenced code blocks should have a language specified",
	"source": "markdownlint",
	"startLineNumber": 87,
	"startColumn": 1,
	"endLineNumber": 87,
	"endColumn": 4,
	"origin": "extHost1"
}
```

```json
[{
	"resource": "/c:/Users/ryanf/github/mkpp/README.md",
	"owner": "markdownlint",
	"code": {
		"value": "MD033",
		"target": {
			"$mid": 1,
			"path": "/DavidAnson/markdownlint/blob/v0.38.0/doc/md033.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "MD033/no-inline-html: Inline HTML [Element: div]",
	"source": "markdownlint",
	"startLineNumber": 368,
	"startColumn": 1,
	"endLineNumber": 368,
	"endColumn": 21,
	"origin": "extHost1"
}]
```

---

## `MD010` - Hard tabs

Tags: `hard_tab`, `whitespace`

Aliases: `no-hard-tabs`

Parameters:

- `code_blocks`: Include code blocks (`boolean`, default `true`)
- `ignore_code_languages`: Fenced code languages to ignore (`string[]`, default
  `[]`)
- `spaces_per_tab`: Number of spaces for each hard tab (`integer`, default `1`)

Fixable: Some violations can be fixed by tooling

This rule is triggered by any lines that contain hard tab characters instead
of using spaces for indentation. To fix this, replace any hard tab characters
with spaces instead.

Example:

<!-- markdownlint-disable no-hard-tabs -->

```markdown
Some text

	* hard tab character used to indent the list item
```

<!-- markdownlint-restore -->

Corrected example:

```markdown
Some text

    * Spaces used to indent the list item instead
```

You have the option to exclude this rule for code blocks and spans. To do so,
set the `code_blocks` parameter to `false`. Code blocks and spans are included
by default since handling of tabs by Markdown tools can be inconsistent (e.g.,
using 4 vs. 8 spaces).

When code blocks are scanned (e.g., by default or if `code_blocks` is `true`),
the `ignore_code_languages` parameter can be set to a list of languages that
should be ignored (i.e., hard tabs will be allowed, though not required). This
makes it easier for documents to include code for languages that require hard
tabs.

By default, violations of this rule are fixed by replacing the tab with 1 space
character. To use a different number of spaces, set the `spaces_per_tab`
parameter to the desired value.

Rationale: Hard tabs are often rendered inconsistently by different editors and
can be harder to work with than spaces.

```json
[{
	"resource": "/c:/Users/ryanf/github/mkpp/revisions.md",
	"owner": "markdownlint",
	"code": {
		"value": "MD010",
		"target": {
			"$mid": 1,
			"path": "/DavidAnson/markdownlint/blob/v0.38.0/doc/md010.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "MD010/no-hard-tabs: Hard tabs [Column: 1]",
	"source": "markdownlint",
	"startLineNumber": 47,
	"startColumn": 1,
	"endLineNumber": 47,
	"endColumn": 2,
	"origin": "extHost1"
}]
```
