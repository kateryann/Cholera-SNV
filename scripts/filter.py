import os
import glob

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Directory where your *_intersected.bed files are located
input_directory = "./"

# Iterate over all files matching the pattern
for input_file in glob.glob(os.path.join(input_directory, '*_intersected.bed')):
    base = os.path.basename(input_file).replace("_intersected.bed", "")

    output_filtered_file = f"filtered_{base}_intersected.bed"

    with open(input_file, 'r') as intersected_file, open(output_filtered_file, 'w') as output:
        lines = intersected_file.readlines()

        sorted_lines = sorted(lines, key=lambda x: float(x.strip().split()[-1]) if is_numeric(x.strip().split()[-1]) else float('-inf'), reverse=True)

        for line in sorted_lines:
            if 'hypothetical protein' in line:
                continue

            output.write(line)

    print(f"Filtering and sorting complete for {input_file}. Check the output file:", output_filtered_file)
