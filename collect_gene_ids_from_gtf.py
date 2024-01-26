# -*- coding: utf-8 -*-
"""
Python3.5: collect_gene_ids_from_gtf.py

Collecting the 39,469 gene IDs of the protein coding genes of Zea mays

Input:  Zea_mays.AGPv3.31.gtf
Output: protein_coding_genes.AGPv3.tsv

@author: Lucia Vedder
@date: 2017, May 9
"""

from optparse import OptionParser


def collect_gene_ids(infile, outfile):
    
    with open(outfile, 'w') as out:
        out.write('#gene_id\tchromosome\tstart_pos\tend_pos\n')
    
        with open(infile, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                
                parts = line.split(sep='\t')
                if parts[2] == 'gene':
                    chromosome = parts[0]
                    start_pos = parts[3]
                    end_pos = parts[4]
                    annotation = parts[8]
                    annotation = annotation.replace('\n', '')
                    info = annotation.split(sep=';')
                    
                    if 'gene_biotype \"protein_coding\"' in annotation:
                        gene_id = info[0].replace('gene_id \"', '')
                        gene_id = gene_id.replace('\"', '')
                        #print(gene_id, chromosome, start_pos, end_pos)
                        
                        out.write(gene_id), out.write('\t')
                        out.write(chromosome), out.write('\t')
                        out.write(start_pos), out.write('\t')
                        out.write (end_pos), out.write('\n')
                
                
                

def main():
    
    # handle the command line arguments
    parser = OptionParser(usage="Usage: %prog <INFILE> <OUTFILE>")
    
    (options, args) = parser.parse_args()
    
    # start the computaions
    collect_gene_ids(args[0], args[1])


if __name__ == "__main__":
   main()
