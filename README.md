# parallel-gpt

## Overview

parallel-gpt is a project that facilitates processing large datasets using the GPT model within a Map-Reduce architecture. This setup allows for efficient data handling and processing, making it ideal for tasks requiring significant computational power and data organization.

## Features

- **Scalability**: Designed to handle large datasets effectively.
- **Error Handling**: Automatically skips files that have already been processed, allowing for easy reruns.
- **Output Management**: Outputs are organized and easy to merge.

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
    
    ```bash
    git clone https://github.com/pluveto/parallel-gpt.git
    cd parallel-gpt
    ```
    
2. Install the required libraries:
    
    ```bash
    pip install -r requirements.txt
    ```

3. Configurations:

.env file:

```
TOKEN=sk-...
ENDPOINT=https://.../v1/chat/completions
```

## Usage Instructions

1. **Generate Input Files**: Use the gen.sh script to create empty files. These files will be named part_N.txt, where N is a unique identifier.
    
    ```bash
    ./gen.sh
    ```
    
2. **Add Data**: Place the data you want to process into the corresponding part_N.txt files.
    
3. **Execute Processing**: Run the main processing script using:
    
    ```bash
    python main.py part_*.txt
    ```
    
4. **Handle Errors**: If an error occurs during processing, you can rerun the command. Files that are already processed will be skipped, ensuring efficiency.
    
5. **Output Files**: The results will be saved in files named part_N_out.txt, where N matches the identifier of the input file.
    
6. **Merge Output**: To combine all output files into a single file, run:
    
    ```bash
    python comb.py
    ```
    
    The final merged output will be saved as combined_output.txt.
    

## Customization

- **Prompts**: You can specify your custom prompts in the prompt.txt file. This file allows you to provide dynamic inputs for generating content.
    
- **Templates**: Similarly, define your templates in template.txt. For instance:
    
    ```plaintext
    Write a short story about {prompt}.
    ```
    
    You can modify this template to suit your needs and control the format of the output data.
    

## Contributing

We welcome contributions! If you have improvements or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
