import os

def add_sample_id_to_vcf():
    # Get the current working directory
    directory = os.getcwd()

    # List all files in the current directory
    vcf_files = [file for file in os.listdir(directory) if file.endswith(".vcf")]

    for vcf_file in vcf_files:
        # Extract sample ID from the file name
        sample_id = vcf_file.split('.')[0]

        # Read the contents of the VCF file
        with open(os.path.join(directory, vcf_file), 'r') as file:
            vcf_content = file.read()

        # Add the sample ID as a comment line to the VCF content
        modified_vcf_content = '##SAMPLE_ID={}\n{}'.format(
            sample_id, vcf_content
        )

        # Write the modified content back to the VCF file
        with open(os.path.join(directory, vcf_file), 'w') as file:
            file.write(modified_vcf_content)

        print(f"Sample ID '{sample_id}' added to {vcf_file}")

# Run the script to add sample IDs to VCF files in the current directory
add_sample_id_to_vcf()
