#!/bin/bash

sed -e 's/* /- /g' "$1" > "$1"-backup
mv "$1"-backup "$1"
