#!/usr/bin/env python3

#search and replace text in files

import argparse
import os
import re

def search_and_replace(directory, search_text, replace_text, exclude=None):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if exclude and re.search(exclude, file):
                continue
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()
            content = re.sub(search_text, replace_text, content)
            with open(file_path, 'w') as f:
                f.write(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search and replace text in files recursively.')
    parser.add_argument('directory', type=str, help='The directory to search in')
    parser.add_argument('search_text', type=str, help='The regular expression to search for')
    parser.add_argument('replace_text', type=str, help='The text to replace with')
    parser.add_argument('--exclude', type=str, help='Regular expression for file names to exclude')
    args = parser.parse_args()

    search_and_replace(args.directory, args.search_text, args.replace_text, exclude=args.exclude)

