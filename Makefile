.PHONY: fix
fix:
	markdownlint '**/*.md' --config ./lint/config/default.yml --ignore ./src/SUMMARY.md --fix

.PHONY: lint
lint:
	markdownlint '**/*.md' --config ./lint/config/default.yml --ignore ./src/SUMMARY.md
	markdownlint 'src/SUMMARY.md' --config ./lint/config/summary.yml

.PHONY: build
build:
	mdbook build

.PHONY: serve
serve:
	mdbook serve
