# GUIDE ON NOTEPAD++ MARKDOWNPLUSPLUS UDL

Notepad++ features Dark Mode with great UDL enhancements since v8.1.3.

NPP will pick up the correct file for dark mode. Here're some conventions in this package:

|          | Normal | Dark Mode |
| -------- | ------ | --------- |
| Command  | `mpp <theme-name>` | `mpp <theme-name> --dark` |
| Filename | `<markdown.theme-name.udl.xml>` | `<markdown.theme-name.dark.udl.xml>` |
| UDL name | Theme Name (markdown) | Theme Name \[markdown\] |

## Limitations

Need your input to solve the following problems:

- `_em text_`, `__strong text__` and `___em strong text___` only parse the first word because it will screw up some URLs such as `example__url`.
- Cannot use asterisk-style bullet points (`* a \<li\> bullet point`). Instead, please write in `- a bullet point` or `+ a bullet point`.
- Improve documentations. My English sucks. (\*´ｰ\`\*)
- The GFM's strikethrough `~~like this~~` is still missing. Will do it later.

If Notepad++ doesn't redraw your current markdown file(s), please re-open the NPP application and/or re-open the markdown file. Upgrade NPP may help.

## Build Your Own UDL Files

The best way to build your own UDL file is to fork this repo. You need to install Node.js in your system.

```cmd
:: In your dev folder
git clone https://github.com/Edditoria/markdown-plus-plus.git
cd markdown-plus-plus
npm install

:: Play around. Finally, run the build script
npm run build
```

For details, please read the document: [build-workflow.md](docs/build-workflow.md)

## Options

Options are reviewed in v3. In **each** config file in the config folder, you can adjust for your own build. Here are some examples:

| Option | Descriptions |
| ------ | ------------ |
| `goodies.highlightHex` | Highlight HEX value. |
| `flags.transparentBg` | Make the text background being transparent. :warning: **Use it with caution** |
| `flags.asteriskUnorderedList` | Enable the markdown style of asterisk-style bullet points (`* a \<li\> bullet point`). :warning: **Use it with caution** |

For details, please read the document: [build-workflow.md](docs/build-workflow.md)

## Key Changes from v2 to v3

- Markdown-plus-plus is a npm package now. You can fetch the UDL files in command line directly, `npx markdown-plus-plus --help`.
- Build system relies on Node.js. `git clone` then `npm install` to develop this repo. Less dependency hell.
- In v2, there are 2 builds for every theme: Modern and classic. Now, there are only 1 build. The main difference in classic build, [asterisk-style bullet points][end_of_v2], becomes an option in v3.
- Better file structure:
   	- You can find all UDL files in one single folder called `<udl\>`.
   	- You can modify the config files in another folder called `<config\>`.
   	- Filename for UDLs follows the pattern: `<markdown.[theme-name].udl.xml>`.
   	- Filename for configs follows this pattern: `<markdown.[theme-name].config.json>`
