#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Python2.7: count_SNP_alleles_mergedBAM.py

!!!This script requires a python2 environment, because of the pysam package!!!

Count the number of reads matching the Ref/SNP allele using the merges BAM files
Adapted from 'count_SNP_alleles.py'

Input:  SNP file, TSV-format (SNPs_LINE_merged_to_AGPv3.tsv)
        Read mapping file, BAM-format (LINE_merged.rg_sort.bam)
Output: SNP file incl. allele frequencies, TSV-format  (SNPs_LINE_merged_to_AGPv3.count.tsv)

@author: Lucia Vedder
@date: 2017, October 09 (original file July 03)
Copyright (c) Lucia Vedder 2024
"""

from optparse import OptionParser
import pysam


# Count allele frequencies of SNPs, using the pysam package
def count_alleles(in_snp, in_bam, out_tsv):
    samfile = pysam.AlignmentFile(in_bam, 'rb')
    
    with open(out_tsv, 'w') as tsv:
        with open (in_snp, 'r') as snp_file:
            for line in snp_file:
                line = line.replace('\n', '')
                line = line.replace('\r', '')

                if line.startswith('#'):
                    tsv.write(line)
                    tsv.write('\treference_count\tSNP_count\tother_count\n')
                    continue
                snp = line.split('\t')
                
#                print(snp)
                count_ref_allele = 0
                count_snp_allele = 0
                count_other = 0
                
                cov = samfile.count_coverage(snp[0], int(snp[1])-1, int(snp[1])+1) #chromosome + position
                counter = {'A': int(cov[0][0]), 'C': int(cov[1][0]), 'G': int(cov[2][0]), 'T': int(cov[3][0])}
                for key, value in counter.iteritems():
                    if snp[2] == key: #ref allele
                        count_ref_allele = value
                    if snp[3] == key: #snp allele
                        count_snp_allele = value
                count_other = int(cov[0][0]) + int(cov[1][0]) + int(cov[2][0]) + int(cov[3][0]) - count_ref_allele - count_snp_allele
                
#                print "Ref. allele: " + str(count_ref_allele) + "\tSNP allele: " + str(count_snp_allele) + "\tOther: " + str(count_other)
                tsv.write(line)
                tsv.write('\t')
                tsv.write(str(count_ref_allele))
                tsv.write('\t')
                tsv.write(str(count_snp_allele))
                tsv.write('\t')
                tsv.write(str(count_other))
                tsv.write('\n')

    samfile.close()


# Run script
def main():
    # handle the command line arguments
    parser = OptionParser(usage="Usage: %prog <IN-SNP> <IN-BAM> <OUT-TSV>")
    
    (options, args) = parser.parse_args()
    
    count_alleles(args[0], args[1], args[2])



if __name__ == "__main__":
   main()
