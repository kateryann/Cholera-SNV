#Custom script to extract top 20 gene entries from filtered intersected BED file
#Not working

input_filtered_file = "filtered_intersected_file.bed"
output_top_gene_entries = "top_gene_entries.txt"

# Open filtered file and output file
with open(input_filtered_file, 'r') as filtered_file, open(output_top_gene_entries, 'w') as output:
    # Read all lines into a list
    lines = filtered_file.readlines()

    # Sort lines based on the last field (assuming it's a mixture of numerical and non-numerical values)
    sorted_lines = sorted(lines, key=lambda x: float(x.strip().split()[-1]) if x.strip().split()[-1].replace('.', '', 1).isdigit() else float('-inf'), reverse=True)

    # Extract and print only the top 20 gene names
    for line in sorted_lines[:20]:
        annotations = line.strip().split()[-1].split(';')
        gene_name = ""
        for annotation in annotations:
            if annotation.startswith('gene='):
                gene_name = annotation.split('=')[1]
                output.write(f"{gene_name}\n")

print("Extraction of top 20 gene entries complete. Check the output file:", output_top_gene_entries)
