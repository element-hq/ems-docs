#!/bin/bash

fmt -w 80 -s "$1" > "$1"-backup
mv "$1"-backup "$1"

