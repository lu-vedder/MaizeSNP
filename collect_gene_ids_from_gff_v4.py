#==============================================================================
# 
# Collecting the gene IDs of the protein coding genes of Zea mays based on v4
# Input file: C:\Users\Lucia\Zea mays\reference\GCF_000005005.2_B73_RefGen_v4_genomic.gff
# Output file: protein_coding_genes_v4.tsv
# 
# Method adapted from: collect_gene_ids_from_gtf.py
# 
# @author: Lucia
# @date: 8 June 2017
# 
#==============================================================================

from optparse import OptionParser


def collect_gene_ids(infile, outfile):
    
    with open(outfile, 'w') as out:
        out.write('#gene_id\tgene_name\tchromosome\tstart_pos\tend_pos\n')
    
        with open(infile, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                
                parts = line.split(sep='\t')
                if parts[2] == 'gene':
                    annotation = parts[8]
                    annotation = annotation.replace('\n', '')
                    
                    if "gene_biotype=protein_coding" in annotation:
                        chromosome = parts[0]
                        start_pos = parts[3]
                        end_pos = parts[4]
                        
                        info = annotation.split(sep=';')
                        gene_name = ""
                        gene_id = ""
                        for i in info:
                            if i.startswith("Name="):
                                gene_name = i.replace('Name=', '')
                            elif i.startswith("Dbxref=GeneID:"):
                                gene_id = i.replace('Dbxref=GeneID:', '')
                        #print(gene_id, chromosome, start_pos, end_pos)
                        
                        out.write(gene_id), out.write('\t')
                        out.write(gene_name), out.write('\t')
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
