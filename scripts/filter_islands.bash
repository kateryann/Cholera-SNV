
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_bed_file>"
    exit 1
fi

input_file=$1
output_file="${input_file%.bed}_filtered.bed"

# Check if input file exists
if [ ! -f "$input_file" ]; then
    echo "Error: Input file '$input_file' not found."
    exit 1
fi

# Filter the BED file for values greater than 200 in the 9th field
awk '$9 > 200' "$input_file" > "$output_file"

echo "Filtered BED file created: $output_file"
