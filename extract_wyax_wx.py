import os
import glob

def collect_files_with_word(folder_path, word, output_file):
    # Get all text files in the specified folder
    text_files = glob.glob(os.path.join(folder_path, "*.txt"))
    
    # This list will contain the content of files that contain the specified word
    matching_files_content = []
    
    # Loop through all text files and find the ones containing the specific word
    for file_path in text_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if word in content:
                matching_files_content.append(content)
    
    # Write the combined content into a new output file
    with open(output_file, 'w', encoding='utf-8') as output:
        for content in matching_files_content:
            output.write(content)
            output.write("\n")  # Add a newline between different file contents

# Usage example
folder_path = "verified_sent"  # Path to the folder containing text files
word = "लडको"  # The word to search for in the text files
output_file = "combined_output.txt"  # Name of the new text file to write to

collect_files_with_word(folder_path, word, output_file)

