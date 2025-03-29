#!/bin/bash

# Ensure the docs folder exists
mkdir -p docs

# Loop through all .md files in the current directory
for file in *.md; do
    # Check if there are any .md files
    [ -e "$file" ] || continue

    # Get the filename without extension
    filename=$(basename "$file" .md)

    # Convert to .docx using pandoc
    pandoc "$file" -o "docs/$filename.docx"

    echo "Converted: $file -> docs/$filename.docx"
done

echo "All Markdown files have been converted to DOCX."

