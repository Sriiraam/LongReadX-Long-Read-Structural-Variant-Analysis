# LongReadX — Reference Freeze

## Status

**REFERENCE STRATEGY FROZEN — exact source pending verification**

## Genome Build

LongReadX will use:

**GRCh38**

The primary workflow will not mix GRCh37, GRCh38 and T2T-CHM13 resources.

## Working Reference

Only chromosome 20 is required for the regional LongReadX analysis.

Planned working reference:

data/reference/GRCh38_chr20.fa

## Chromosome Naming

Preferred chromosome name:

chr20

Before analysis we must verify naming compatibility among:

- reference FASTA
- source PacBio data
- GIAB truth VCF
- GIAB benchmark BED
- gene annotation

Any required chromosome-name normalization must be documented.

## Reference Source

Exact GRCh38 source:

**PENDING VERIFICATION**

The selected reference must be:

- publicly accessible
- versioned
- compatible with the GIAB HG002 GRCh38 benchmark
- reproducible
- documented

## Reference Files

Planned files:

data/reference/GRCh38_chr20.fa  
data/reference/GRCh38_chr20.fa.fai  
data/reference/GRCh38_chr20.mmi

A sequence dictionary may also be generated if required.

## FASTA Index

Tool:

samtools faidx

## Alignment Index

Tool:

minimap2

PacBio HiFi alignment preset:

minimap2 -x map-hifi

## Gene Annotation

A GRCh38-compatible GENCODE annotation will be used for gene/SV overlap analysis.

Exact GENCODE release:

**PENDING VERIFICATION**

Only chr20 annotation will be retained for the working analysis where practical.

## Validation Requirements

Before the reference is considered fully frozen we must verify:

- exact source URL
- exact reference release
- chr20 sequence length
- chromosome naming
- FASTA index
- minimap2 index
- compatibility with GIAB truth
- compatibility with gene annotation
- SHA256 checksum

## Status

Genome build: **FROZEN — GRCh38**

Working chromosome: **FROZEN — chr20**

Exact reference source/checksum: **PENDING VERIFICATION**
