import sys

def check_presence(file_path):
    with open(file_path, 'r') as bed_file:
        for line in bed_file:
            fields = line.strip().split('\t')
            if len(fields) >= 5:
                identifier = fields[4]  # Adjusted to field 5
                if identifier == '618513':
                    return "Presence"
        return "Absence"

def main():
    if len(sys.argv) < 2:
        print("Usage: python presence_absence_check.py <bed_file1> <bed_file2> ...")
        sys.exit(1)

    bed_files = sys.argv[1:]
    results = []
    for bed_file in bed_files:
        result = check_presence(bed_file)
        results.append((bed_file, result))
    
    with open('presence_absence_results.txt', 'w') as output_file:
        for bed_file, result in results:
            output_file.write(f"{bed_file}\t{result}\n")

    print("Results written to presence_absence_results.txt")

if __name__ == "__main__":
    main()
