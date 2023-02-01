# Search and replace text in files using python

This is a simple script to recursively search and replace text in files using python3, using only built-ins.

usage:

Example using regex to pattern to search 'my-text' and excluding all files ending in .py

```sh
python3 search_replace.py /path/to/dir/to/run/search/and/replace 'my-text.*' my_replacement_text --exclude='*.py'
```
