
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_bed_file>"
    exit 1
fi

input_file=$1
output_file="${input_file%.bed}_filtered.bed"

# Filter the BED file for QUAL values greater than 20 in the 9th field
awk '$9 > 20' "$input_file" > "$output_file"

echo "Filtered BED file created: $output_file"
