import re

def remove_chapter_numbers(text):
    pattern = r'^(#+\s*)(\d+(\.\d+)*\s*)+'
    
    modified_text = re.sub(pattern, r'\1', text, flags=re.MULTILINE)
    
    return modified_text

text = open("combined_output.txt", "r", encoding="utf-8").read()

cleaned_text = remove_chapter_numbers(text)
print(cleaned_text)
