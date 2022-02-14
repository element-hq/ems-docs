#!/bin/bash

for i in $(ls *.md); do markdownlint -f $i; done
