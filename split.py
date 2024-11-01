import sys
import re

def split_by_chapter(file_in):
    with open(file_in, 'r', encoding='utf-8') as f:
        content = f.read()

    # Use regex to split content based on lines starting with one or more '#'
    chapters = re.split(r'(?m)^#+', content)

    # Iterate over the chapters and save each one to a separate file
    for i, chapter in enumerate(chapters):
        chapter = chapter.strip()
        if chapter:  # Check if the chapter is not empty
            # Prepend the '#' delimiter to the chapter
            file_name = f'part{i}.txt'
            with open(file_name, 'w', encoding='utf-8') as f_out:
                f_out.write('#' + chapter)
            print(f'Written to {file_name}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python split_by_chap.py <file_in>")
    else:
        split_by_chapter(sys.argv[1])
