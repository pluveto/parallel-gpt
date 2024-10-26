import os
import re

def get_sorted_files(directory):
    # 获取所有以 _out 结尾的文件
    files = [f for f in os.listdir(directory) if f.endswith('_out.txt')]
    
    # 提取文件名中的数字并排序
    def extract_number(filename):
        match = re.search(r'part(\d+)_out\.txt', filename)
        return int(match.group(1)) if match else float('inf')
    
    sorted_files = sorted(files, key=extract_number)
    return sorted_files

def concatenate_files(directory, output_file):
    sorted_files = get_sorted_files(directory)
    
    with open(output_file, 'w') as outfile:
        for filename in sorted_files:
            with open(os.path.join(directory, filename), 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')  # 添加换行符以分隔文件内容

if __name__ == "__main__":
    directory = '.'  # 当前目录
    output_file = 'combined_output.txt'
    concatenate_files(directory, output_file)
