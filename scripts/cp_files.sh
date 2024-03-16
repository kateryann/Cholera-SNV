#!/bin/bash

# Target directory where .tsv files will be copied
TARGET_DIR="/home/pc/Documents/08_03/ariba_reports"

# Ensure the target directory exists
if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Target directory does not exist: $TARGET_DIR"
  exit 1
fi

# Find and copy all .tsv files from current and subdirectories to the target directory
find . -type f -name "*.tsv" -exec cp {} "$TARGET_DIR" \;

echo "All .tsv files have been copied to $TARGET_DIR."
