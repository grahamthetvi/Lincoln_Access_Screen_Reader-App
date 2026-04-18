import os
import re

files_to_check = [
    "readme.md",
    "security.md",
    "CODE_OF_CONDUCT.md"
]

# Add all markdown and text files in user_docs/en/
user_docs_dir = "user_docs/en"
if os.path.exists(user_docs_dir):
    for f in os.listdir(user_docs_dir):
        if f.endswith(".md") or f.endswith(".txt") or f.endswith(".t2t") or f.endswith(".xliff"):
            files_to_check.append(os.path.join(user_docs_dir, f))

def replace_in_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, not found")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the expanded term first
    new_content = content.replace("NonVisual Desktop Access", "Lincoln Access Screen Reader")
    new_content = new_content.replace("NVDA", "LASR")
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")

for f in files_to_check:
    replace_in_file(f)

