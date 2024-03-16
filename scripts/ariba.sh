for i in *1.fastq; do     
base=$(basename "$i" "_1.fastq");     
ariba run filtered_A1552_prepareref.out "${base}_1.fastq" "${base}_2.fastq" "${base}_run.out"; 
done
