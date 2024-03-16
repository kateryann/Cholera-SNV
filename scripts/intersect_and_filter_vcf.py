for vcf_file in *.vcf; do 

    # Extract file name without extension 

    file_name=$(basename "$vcf_file" .vcf) 

 

    # Perform bedtools intersect 

    bedtools intersect -a A1552.bed -b "$vcf_file" -wa -wb > "${file_name}_intersected.bed" 

 

    # Run Python filter script 

    python filter.py "${file_name}_intersected.bed" 

done
