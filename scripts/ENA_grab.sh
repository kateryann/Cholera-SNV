# Base command
base_command="fastq-dl --outdir . --cpus 4 -a"

# List of sample identifiers
samples=("ERS2494002" "ERS2493884" "ERS2493826" "ERS2493842" "ERS2493883" "ERS2493754" "ERS2494023")

# Loop through samples and download files
for sample in "${samples[@]}"; do
  full_command="$base_command $sample"
  echo "Running command: $full_command"
  $full_command
done
