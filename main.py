import ai
import functools
import concurrent.futures
import os
import argparse
from tqdm import tqdm

def read_text_file(file_path, ignore_nonexistent=True):
    if not os.path.exists(file_path) and ignore_nonexistent:
        return ""

    with open(file_path, 'r') as f:
        return f.read()

def file_processor(prompt, input_file):
    if template:= read_text_file('template.txt'):
        prompt = template.format(prompt=prompt)

    return ai.query(prompt, read_text_file(input_file), json_mode=False)

def process_file(file_processor_fn, input_file):
    try:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_out{ext}"
        
        if os.path.exists(output_file):
            print(f"Skipping {input_file} -> {output_file} (already exists)")
            return
    
        if base.endswith("_out"):
            print(f"Skipping {input_file} -> {output_file} (output file name already ends with '_out')")
            return

        output_content = file_processor_fn(input_file=input_file)
        if not output_content:
            raise Exception("No output content")

        with open(output_file, 'w') as f:
            f.write(output_content)
        print(f"Processed {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

def main(input_files):
    file_processor_impl = functools.partial(file_processor, prompt=read_text_file('prompt.txt'))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_file, file_processor_impl, file): file for file in input_files}
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing files"):
            try:
                future.result()
            except Exception as e:
                print(f"Error in future: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='批量处理文件的脚本')
    parser.add_argument('input_files', nargs='+', help='输入文件列表')
    
    args = parser.parse_args()
    
    main(args.input_files)
