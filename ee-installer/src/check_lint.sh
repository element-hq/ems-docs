#!/bin/bash

for i in $(ls *.md); do ./ensure_80char.sh "$i" && ./fix_code_fence.sh "$i" && ./fix_unordered_list.sh "$i" && markdownlint -c "../../lint/config/default.yml" -c "../../lint/config/summary.yml" -f "$i"; done
