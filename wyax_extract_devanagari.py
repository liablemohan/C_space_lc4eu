import os
import glob

def collect_files_with_word(folder_path, word, output_file):
    # Get all files in the specified folder, including those without extensions
    all_files = os.listdir(folder_path)
    
    # This list will contain the content of files that contain the specified word
    matching_files_content = []
    
    # Loop through all files and check if they contain the specific word (case-sensitive)
    for filename in all_files:
        # Only consider files with no extensions or specific extension if needed
        if '.' not in filename or filename.endswith(''):  # No extension or empty extension
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if word in content:  # Case-sensitive match
                        matching_files_content.append(content)
            except Exception as e:
                print(f"Could not read file {filename}: {e}")
    
    # Write the combined content into a new output file
    with open(output_file, 'w', encoding='utf-8') as output:
        for content in matching_files_content:
            output.write(content)
            output.write("\n")  # Add a newline between different file contents

# Usage example
folder_path = "verified_sent"  # Path to the folder containing gedit files
word = "kim"  # The case-sensitive word to search for
output_file = "combined_output.txt"  # Name of the new text file to write to

collect_files_with_word(folder_path, word, output_file)

