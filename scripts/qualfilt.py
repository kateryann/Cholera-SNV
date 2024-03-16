import pandas as pd
import glob

def filter_vcf(input_file, output_file):
    # Initialize an empty list to hold header lines
    headers = []

    # Open the input VCF file and read header lines
    with open(input_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                headers.append(line)
            else:
                break  # Stop reading when you reach the first data line

    # Convert the last header line (column names) to a list, trimming the newline character
    col_names = headers[-1].strip().split('\t')

    # Now read the VCF data into a DataFrame, using the column names extracted
    vcf_df = pd.read_csv(input_file, sep='\t', comment='#', names=col_names, header=None)

    # Filter rows where QUAL is greater than or equal to 20
    filtered_df = vcf_df[vcf_df['QUAL'] >= 20]

    # Write header lines and filtered DataFrame to a new VCF file
    with open(output_file, 'w') as file:
        for header in headers[:-1]:  # Write all but the last header line
            file.write(header)
        filtered_df.to_csv(file, sep='\t', index=False)

if __name__ == "__main__":
    # Specify the path to your VCF files
    vcf_files = glob.glob('*.vcf')

    # Specify the output directory for filtered VCF files
    output_directory = './'

    for vcf_file in vcf_files:
        # Generate output file path
        output_file = output_directory + 'qualfiltered_' + vcf_file.split('/')[-1]

        # Filter the VCF file and save the result
        filter_vcf(vcf_file, output_file)
