#!/bin/bash
tsv_files=$(ls *.tsv)

# Write the list of .tsv files to a txt file
echo "$tsv_files" > tsv_files.txt
