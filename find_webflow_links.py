import os
import re

def find_webflow_links(directory='.'):
    # Pattern to match URLs containing website-files.com
    pattern = r'https?://[^\s<>"\']+?website-files\.com[^\s<>"\']+'
    found_links = set()  # Using set to avoid duplicates
    
    # Walk through all directories and files
    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                # Try to read the file as text
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Find all matches in the file
                    matches = re.findall(pattern, content)
                    found_links.update(matches)
            except (UnicodeDecodeError, IOError):
                # Skip files that can't be read as text
                continue

    # Save results to output file
    with open('webflow_links.txt', 'w') as f:
        for link in sorted(found_links):
            f.write(f"{link}\n")
    
    print(f"Found {len(found_links)} unique links. Results saved to webflow_links.txt")

if __name__ == "__main__":
    find_webflow_links() 