#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3.5: filter_blacklist_merged_SNPs.py

Using the SNPs between 'our' B73 and the reference genome as a blacklist
for the filtering of "true" SNPs.

Input:  SNP file of LINE (GATK output, VCF format)
        SNP file of B73 (GATK output, VCF format)
Output: Filtered SNP file of LINE (TSV format)

@date 2017, October 04
@author Lucia Vedder
Copyright (c) 2024 Lucia Vedder
"""

from optparse import OptionParser


# Filter for SNPs, not included in the blacklist, and write them to output
def filter_SNPs(in_filter_vcf, bl, out_tsv):
    with open(out_tsv, 'w') as tsv:
        tsv.write("#chromosome\tposition\treference_allele\tSNP_allele\n")

        num_total = 0
        num_out = 0
        num_in = 0

        with open(in_filter_vcf, 'r') as filter:
            for line in filter:
                if line.startswith('#'):
                    continue

                snp = line.split('\t')
                found = False
                num_total += 1

                for bl_snp in bl:
                    if snp[0] == bl_snp[0] and snp[1] == bl_snp[1]:
#                        print(snp[0], snp[1])
                        found = True
                        num_out += 1
                        break

                if found == False:
                    num_in += 1
                    tsv.write(snp[0]) #chromosome
                    tsv.write('\t')
                    tsv.write(snp[1]) #position
                    tsv.write('\t')
                    tsv.write(snp[3]) #ref_allele
                    tsv.write('\t')
                    tsv.write(snp[4]) #SNP_allele
                    tsv.write('\n')

        # Print numbers
        print("Total number of processed SNPs: ", num_total)
        print("Number of SNPs, filtered-out due to given blacklist: ", num_out)
        print("Number of \"true\" SNPs: ", num_in)


# Read-in of the SNP blacklist
def read_bl(in_bl):
    bl = []
    with open(in_bl, 'r') as b:
        for line in b:
            if line.startswith('#'):
                continue

            s = line.split('\t')
            bl.append((s[0], s[1]))

    return bl


# Run script
def main():
    parser = OptionParser(usage="Usage= %prog <IN-FILTER_VCF> <IN-BLACKLIST-VCF> <OUT-TSV>")
    (options, args) = parser.parse_args()

    blacklist = read_bl(args[1])

    filter_SNPs(args[0], blacklist, args[2])



if __name__ == "__main__":
    main()
