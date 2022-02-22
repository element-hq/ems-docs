#!/bin/bash

RUN_PATH=$(dirname "$0")

for i in $(ls *.md); do $RUN_PATH/ensure_80char.sh "$i" && $RUN_PATH/fix_code_fence.sh "$i" && $RUN_PATH/fix_unordered_list.sh "$i" && markdownlint -c $RUN_PATH/../lint/config/default.yml -c $RUN_PATH/../lint/config/summary.yml -f "$i"; done
