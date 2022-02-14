#!/bin/bash

for i in $(ls *.md); do ./ensure_80char.sh "$i" && markdownlint -f "$i"; done
