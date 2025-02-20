#!/usr/bin/env python3

import os
from bs4 import BeautifulSoup
import re

def find_hrefs_in_file(file_path, output_file):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Try parsing as HTML/XML
            try:
                soup = BeautifulSoup(content, 'html.parser')
                for tag in soup.find_all(href=True):
                    output_file.write(tag['href'] + '\n')
            except:
                # Fallback to regex for non-HTML files
                href_pattern = r'href=[\'"]([^\'"]+)[\'"]'
                matches = re.findall(href_pattern, content)
                for match in matches:
                    output_file.write(match + '\n')
    except Exception as e:
        pass  # Skip files that can't be read

def main():
    output_path = 'hrefs.txt'
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file != 'hrefs.txt':  # Skip the output file itself
                    file_path = os.path.join(root, file)
                    find_hrefs_in_file(file_path, output_file)
    print(f"All hrefs have been saved to {output_path}")

if __name__ == "__main__":
    main() 