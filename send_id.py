def generate_sent_id(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    output_lines = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("#") or not line:  # Skip comments and empty lines
            output_lines.append(line)
        elif line.isdigit():  # Identify sentence number
            sent_id = f"<sent_id={line}>\n"
            output_lines.append(sent_id)  # Add <sent_id>
            output_lines.append(line)    # Retain the sentence number
        else:
            output_lines.append(line)  # Add sentence line as-is
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join(output_lines))

# Input and Output file paths
input_file = "verified_out"
output_file = "verified_output"

# Run the function
generate_sent_id(input_file, output_file)

