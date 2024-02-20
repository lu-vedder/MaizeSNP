#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3.5: filter_merged_snps_for_codingGenes.py

Filter the SNPs of the merged BAM files for protein-coding genes set

Input:  Annotation file of protein-coding genes, TSV-format (protein_coding_genes.tsv)
        SNP file, TSV-format (SNPs_LINE_merged_to_AGPv3.tsv), may also include allele counts
Output: Coding genes SNP file, TSV-format (SNPs_LINE_merged_to_AGPv3.codingGene.tsv)

@author: Lucia Vedder
@date: 2017, October 09
Copyright (c) Lucia Vedder 2024
"""

from optparse import OptionParser


# Read-in of the protein-coding genes
def read_genes(in_genes):
    genes = []
    num_genes = 0

    with open(in_genes, 'r') as g:
        for line in g:
            if line.startswith('#'):
                continue

            gene = line.split('\t')
            genes.append([gene[0], gene[1], gene[2], gene[3]]) # gene_id, chromosome, start_pos, end_pos
            num_genes += 1

    print(num_genes, " protein-coding genes are read in from file.\n")
    return genes


# Checking, if a SNP position is within a given gene
def in_gene(snp_pos, gene):
    
    if int(snp_pos) >= int(gene[2]) and int(snp_pos) <= int(gene[3]):
        return True
    else:
        return False


# Filter for SNPs positioned within protein-coding genes and write them to output
def filter_codingGenes(out_tsv, in_snps, genes):
    with open(out_tsv, 'w') as tsv:
        num_snps_total = 0
        num_snps_codingGenes = 0

        with open(in_snps, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    line = line.replace('#', '#gene_id\t')
                    tsv.write(line)
                    continue
            
                snp = line.split(sep='\t')
                num_snps_total += 1

                for gene in genes:
                    if snp[0] == gene[1]: # chromosome
                        if in_gene(snp[1], gene): # position in gene
                            num_snps_codingGenes += 1
                            tsv.write(gene[0])
                            tsv.write('\t')
                            tsv.write(line)

        print("Total number of processed SNPs: ", num_snps_total)
        print("Number of SNPs within protein-coding genes: ", num_snps_codingGenes)
 

# Run script
def main():
    parser = OptionParser(usage="Usage: %prog <IN-GENES> <IN-SNPS> <OUT-TSV>")
    
    (options, args) = parser.parse_args()
    
    genes = read_genes(args[0])
    filter_codingGenes(args[2], args[1], genes)
    


if __name__ == "__main__":
   main()
