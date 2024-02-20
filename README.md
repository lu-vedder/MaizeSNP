# MaizeSNP

The MaizeSNP wolkflow was specifically designed for the SNP analysis of different maize (_Zea mays_ L.) inbred lines in comparison to B73 as a reference line.
The final result is a TSV-file, containing a set of SNPs between the respective inbred line and B73, located in the protein-coding regions of maize. Further, this file includes the allele counts, obtained from the original mapping.

**Workflow.txt** <br>
The workflow file gives the exact order and parameter settings for runnig the other scripts. Please mind the following:
* Beforehand a mapping of all merged reads of one indred line ('LINE') has been performed using Bowtie2 (performed with version v2.2.9) [1]. The resulting mapping files (SAM-files) were prepared for the SNP calling as stated in the workflow using Samtools (v1.3.1) [2] and Picard (v2.9.0) [3].
* The SNP calling was performed using GATK (performed with version v3.7-0-gcfedb67) [4]. The input file is the before mentioned prepared mapping result.
* The reference genome of B73 was used in version 3. The usage of new versions may need some adaptations.

**filter_blacklist_merged_SNPs.py** <br>
Using the SNPs between 'our' B73 and the reference genome as a blacklist for the filtering of "true" SNPs.
This step should reduce the mapping bias caused by variations between the reference B73 and 'our' B73 used in the lab experiments.

**empty_blacklist.txt** <br>
This is just a dummy file. It can be used as an empty blacklist file in the 'filter_blacklist_merged_SNPs.py' script.

**count_SNP_alleles_mergedBAM.py - Python2 environment required!** <br>
Count the number of reads matching the Ref/SNP allele using the merged BAM files.

**collect_gene_ids_from_gtf.py** <br>
Collecting the 39,469 gene IDs of the protein coding genes of Zea mays, reference version 3 (GTF-format).

**collect_gene_ids_from_gff3.py** <br>
Collecting the gene IDs of the protein coding genes of Zea mays based on reference version 4 (GFF3-format).

**filter_merged_snps_for_coding_genes.py** <br>
Filter the SNPs (TSV-format) for positions located in the protein-coding genes set. Allele counts may be included in the file.


# Citation
Please cite via Zenodo: 


# License
Copyright (c) 2024 Lucia Vedder <br>
For details see the [LICENSE](LICENSE) file.

---
[1] https://bowtie-bio.sourceforge.net/bowtie2/index.shtml <br>
[2] http://www.htslib.org <br>
[3] https://broadinstitute.github.io/picard <br>
[4] https://gatk.broadinstitute.org
