# Custom script to parse BED-like file and extract relevant information
#Not working

input_bed_file = "filtered_intersected_file.bed"
output_file = "extracted_information.txt"

# Open input and output files
with open(input_bed_file, 'r') as bed_file, open(output_file, 'w') as output:
    # Write header to output file
    output.write("Gene_Name\tChromosome\tStart_Position\tEnd_Position\n")

    # Iterate through each line in the BED file
    for line in bed_file:
        # Extract relevant information from each line
        entries = line.strip().split()

        # Initialize variables
        chromosome = ""
        start_position = ""
        end_position = ""
        gene_name = ""

        # Extract information from the line
        for entry in entries:
            if entry.startswith('gene='):
                gene_name = entry.split('=')[1]
            elif entry.startswith('Name='):
                gene_name = entry.split('=')[1]  # Override gene name if 'Name=' is found
            elif entry.startswith('hypothetical protein'):
                # Skip lines with 'hypothetical protein'
                break
            elif not chromosome:
                chromosome = entry
            elif not start_position:
                start_position = entry
            elif not end_position:
                end_position = entry

        # Write the extracted information to the output file
        if gene_name:
            output.write(f"{gene_name}\t{chromosome}\t{start_position}\t{end_position}\n")

print("Extraction complete. Check the output file:", output_file)
