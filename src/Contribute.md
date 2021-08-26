# Contribute

1. Fork the [GitHib repo](https://github.com/vector-im/ems-docs)
1. Look at other pages, make your contributions in the same style and formatting etc
1. Use American English
1. Make your changes
1. Install `pngcrush`, `mdbook`, `markdownlint-cli`, and a local web server, for example `sensible-browser`
1. Add your new page to `SUMMARY.md` if applicable
1. `pngcrush` all your images with `pngcrush -brute -ow "Screen Shot 2020-10-20 at 12.02.17 PM.png"`
1. Run the linter and fix any errors
1. Compile the book using `mdbook build`
1. `sensible-browser book/index.html` - make sure it looks good, and that all links etc. are working
1. Make a pull request

## Linter

[markdownlint](https://github.com/igorshubovych/markdownlint-cli) is used to ensure consistent Markdown formatting across all documents.

You can run the checks locally by installing `markdownlint-cli` and running:

```bash
markdownlint '**/*.md' --config ./lint/config/default.yml --ignore ./src/SUMMARY.md
markdownlint 'src/SUMMARY.md' --config ./lint/config/summary.yml
```

The rules are defined in `lint/config/default.yml` and `lint/config/summary.yml`. Summary has `MD025` and `MD041` turned off due to how `mdbook` expects the file `SUMMARY.md`.

Extended rule descriptions, including how to fix any formatting errors, are available [here](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md).

[Here](https://meta.stackexchange.com/questions/184108/what-is-syntax-highlighting-and-how-does-it-work) is a list of languages for code blocks. Please use a language where possible, otherwise you may use `none`.
