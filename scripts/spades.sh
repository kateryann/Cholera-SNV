for i in *_1.fastq; do  
    base=$(basename $i "_1.fastq")
    spades.py -1 ${base}_1.fastq -2 ${base}_2.fastq -o ${base}_assembly
done


