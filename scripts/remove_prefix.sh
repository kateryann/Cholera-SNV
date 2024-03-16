
# Specify the path to your VCF files
vcf_dir="/path/to/your/vcf/files"

# Move to the VCF directory
cd "$vcf_dir" || exit

# Loop through all VCF files matching the pattern
for vcf_file in modified_*.vcf; do
    # Extract the basename without the "qualfiltered_" prefix
    new_name=$(echo "$vcf_file" | sed 's/modified_//')

    # Rename the file
    mv "$vcf_file" "$new_name"
done
