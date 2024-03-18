import sys

def count_nonsyn(file_path):
    count = 0
    with open(file_path, 'r') as tsv_file:
        for line in tsv_file:
            fields = line.strip().split('\t')
            # Check if there are enough fields and if field 20 (index 19) contains 'NONSYN'
            if len(fields) > 19 and fields[19].upper() == 'NONSYN':
                count += 1
    return count

def main():
    if len(sys.argv) < 2:
        print("Usage: python count_nonsyn.py <file1.tsv> <file2.tsv> ...")
        sys.exit(1)

    tsv_files = sys.argv[1:]
    results = []

    for tsv_file in tsv_files:
        count = count_nonsyn(tsv_file)
        results.append((tsv_file, count))

    with open('nonsyn_counts.txt', 'w') as output_file:
        for tsv_file, count in results:
            output_file.write(f"{tsv_file}\t{count}\n")

    print("Counts have been written to nonsyn_counts.txt")

if __name__ == "__main__":
    main()
