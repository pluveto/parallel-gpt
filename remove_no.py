import re
import sys

def remove_chapter_numbers(text):
    pattern = r'^(#+\s*)(\d+(\.\d+)*\s*)+'
    
    modified_text = re.sub(pattern, r'\1', text, flags=re.MULTILINE)
    
    return modified_text

DEFAULT_FILENAME = "combined_output.txt"

if __name__ == "__main__":
    if sys.argv[1:]:
        DEFAULT_FILENAME = sys.argv[1]

    text = open(DEFAULT_FILENAME, "r", encoding="utf-8").read()

    cleaned_text = remove_chapter_numbers(text)
    print(cleaned_text)
