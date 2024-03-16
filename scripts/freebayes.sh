# Assuming sorted BAM files are named file1_sorted.bam, file2_sorted.bam, etc.  
# Activate freebayes
#Added new filtering


for i in *_sorted.bam; do  

 
base=$(basename $i "_sorted.bam") 

 
# Run FreeBayes  

freebayes -f A1552.fasta  --ploidy 1 --min-mapping-quality 20 --min-coverage 5 --min-base-quality 30 ${base}_sorted.bam > ${base}.vcf 

done 
