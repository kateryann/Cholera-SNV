#!/bin/bash

# Find all .tsv files in subdirectories and loop through them
find . -type f -name "*.tsv" | while read -r file; do
  # Extract the directory path and filename
  dir_path=$(dirname "$file")
  parent_dir_name=$(basename "$dir_path")
  
  # Remove '_run.out' suffix from parent directory name, if present
  parent_dir_name=${parent_dir_name%_run.out}

  new_name="${parent_dir_name}.tsv"

  # Construct the new path for the file
  new_path="${dir_path}/${new_name}"

  # Check if the target file already exists
  if [[ -f "$new_path" ]]; then
    echo "Skipping, target file already exists: $new_path"
  else
    # Rename the file
    mv "$file" "$new_path"
    echo "Renamed $file to $new_path"
  fi
done
