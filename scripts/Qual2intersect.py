# Custom script to append QUAL column to intersected file
#Working 

 

intersected_file = "test_intersected.bed" 

vcf_file = "variants.vcf" 

output_file = "intersected_with_qual.bed" 

 

# Create a dictionary to store QUAL values based on chromosome and position 

qual_dict = {} 

 

# Open VCF file and populate the qual_dict 

with open(vcf_file, 'r') as vcf: 

    for line in vcf: 

        if not line.startswith('#'): 

            fields = line.strip().split() 

            chromosome = fields[0] 

            position = fields[1] 

            qual_value = fields[5] if len(fields) > 5 else "N/A"  # Assuming QUAL is in the 6th field 

            qual_dict[(chromosome, position)] = qual_value 

 

# Open intersected file and output file 

with open(intersected_file, 'r') as intersected, open(output_file, 'w') as output: 

    # Iterate through each line in the intersected file 

    for line in intersected: 

        # Split the line based on spaces 

        fields = line.strip().split() 

 

        # Extract relevant information 

        chromosome = fields[0] 

        start_position = int(fields[1]) 

        end_position = int(fields[2]) 

 

        # Find corresponding QUAL value for the range 

        qual_value = "N/A" 

        for position in range(start_position, end_position + 1): 

            qual_key = (chromosome, str(position)) 

            qual_value = qual_dict.get(qual_key, qual_value) 

 

        # Append QUAL value to the end of the line 

        output.write(line.strip() + "\t" + qual_value + "\n") 

 

print(f"Script execution complete. Check the output file: {output_file}") 
