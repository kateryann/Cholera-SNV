#!/bin/bash

# Define the file name
fasta_file="prot_A1552.fasta"
output_file="filtered.fasta"

# Define the list of names to keep
keep_names=(
rpsL 

cysI 

nlpD 

rpoS 

pnp 

pstS 

fadL 

rtxA 

cry1 

chrR 

ftsY_2 

mcpP_3 

pxpC 

glxK 

yxeM 

rpoC 

dhbE 

ssrA 

sdhD 

nqrF 

arcA_2 

barA 

serA 

rpoA 

rplD 

aroB 

dcuA 

rcsC_8 

kbl 

gyrB 

oadA_1 

luxO_1 

rcsC_2 

oppA 

nqrE 

dcuB 

mepA_1 

ppk 

tcpN 

pepN_1 

pepN_2 

mnmC 

era 

yheS 

crp 

fabH2 

glpR_2 

trkI 

tldD 

infB 

moaC 

gyrA 

asnS 

mcpU 

rho 

dusA 

metH 

mreB 

truD 

mutS 

ypjD 

degS 

rsmC 

rbfA 

fepC 

purF 

rsxC 

acsA 

rmf 

dpiB 

norM_2 

ybhF 

sapA 

ruvA 

rpsA 

cheY_4 

lpxB 

carB 

aceE 

leuD1 

metB 

pulA 

actP 

manA_2 

hlyA 

phaB 

luxP 

ravA 

calB 

rhaS_4 

acnB 

frp 

ppnN 

cysG_1 

srpA 

galR_2 

mdtL_1 

pglF 

nfsB 

tupB 

fadD 

pckA 

pstB3 

helD 

rpoB 

ihfA 

fnr 

rseA 
)

# Prepare an associative array for faster lookup
declare -A name_map
for name in "${keep_names[@]}"; do
  name_map["$name"]=1
done

# Filter the FASTA file
{
while IFS= read -r line; do
  # Check if the line is a header line
  if [[ $line == ">"* ]]; then
    # Extract the last part of the header after the last semicolon
    name=$(echo "$line" | rev | cut -d';' -f1 | rev)
    # Check if this name is in the list to keep
    if [[ ${name_map[$name]} ]]; then
      # If so, flag to print this and the next line (sequence)
      print_next=1
      echo "$line"
    else
      # Do not print the next line (sequence)
      print_next=0
    fi
  elif [[ $print_next -eq 1 ]]; then
    # If the flag is set, print the sequence line
    echo "$line"
  fi
done < "$fasta_file"
} > "$output_file"

echo "Filtering complete. Output saved to $output_file"
