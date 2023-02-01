# Search and replace text in files using python

This is a simple script to recursively search and replace text in files using python3, using only built-ins.

usage:

Example using regex to pattern to search 'my-text' and excluding all files ending in .py

```sh
python3 search_replace.py /path/to/dir/to/run/search/and/replace 'my-text.*' my_replacement_text --exclude='*.py'
```

The purpose of this script is that it can be included with python template projects to replace text (like boilerplate project names).  Some OSes don't have built-in utils like grep & sed etc by default (such as windows).

This script can be included in a tools directory for such projects and then scripted to assist in set up.

