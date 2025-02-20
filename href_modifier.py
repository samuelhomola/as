import re

def modify_hrefs(content):
    # List of paths to modify
    paths = [
        '/featured',
        '/history',
        '/privacy-policy',
        '/work',
        '/about',
        '/careers',
        '/contact',
        '/behind-the-scenes'
    ]
    
    # Create a pattern that matches any of these paths
    pattern = '|'.join(re.escape(path) for path in paths)
    pattern = f'(href=")({pattern})"'
    
    # Replace function that adds .html to the matched href
    def replace_func(match):
        return f'{match.group(1)}{match.group(2)}.html"'
    
    # Perform the replacement
    modified_content = re.sub(pattern, replace_func, content)
    return modified_content

def process_file(file_path):
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_hrefs(content)
        
        # Write back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
            
        print(f"Successfully processed {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python href_modifier.py <file1> [file2 ...]")
        sys.exit(1)
    
    # Process each file provided as argument
    for file_path in sys.argv[1:]:
        process_file(file_path) 