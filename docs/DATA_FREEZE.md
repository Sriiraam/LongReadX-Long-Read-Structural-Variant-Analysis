# LongReadX — Data Freeze

## Status

**PARTIALLY FROZEN — exact source file and genomic interval pending verification**

No large sequencing data will be downloaded until the public source, file size, remote-access method, and benchmark interval are verified.

## Sample

- Sample: HG002
- Identifier: NA24385
- Organism: Homo sapiens
- Technology: PacBio HiFi
- Genome build: GRCh38

## Dataset Strategy

LongReadX will use a genuine PacBio HiFi subset from HG002.

A normal full-depth whole-genome dataset will NOT be downloaded.

The workflow will use:

Public HG002 PacBio HiFi data  
→ chr20 regional extraction  
→ approximately 15–20 Mb benchmark-rich interval  
→ FASTQ extraction  
→ independent LongReadX alignment and SV calling

## Region

Chromosome: chr20

Target interval size: approximately 15–20 Mb

Exact coordinates: **PENDING GIAB truth-density analysis**

The final interval must:

1. overlap official GIAB benchmark regions
2. contain sufficient truth SVs
3. preferably contain both deletions and insertions
4. have adequate PacBio HiFi coverage
5. remain computationally manageable
6. keep active project data approximately ≤1.5 GB

## Truth Dataset

Planned benchmark:

**GIAB HG002 v5.0q GRCh38 structural-variant benchmark**

Expected resources:

- HG002 GRCh38 v5.0q SV truth VCF
- VCF index
- official SV benchmark BED

Exact URLs, filenames and sizes will be verified before download.

## Planned Input

Final working long-read input:

data/raw/HG002_LongReadX.fastq.gz

Temporary regional source BAM:

data/interim/HG002_LongReadX_source_region.bam

The temporary BAM may be deleted after FASTQ extraction and validation.

## Storage Rule

Preferred active project-data budget:

**≤1.5 GB**

We will avoid retaining unnecessary duplicate BAM/FASTQ files.

## Required Validation Before Final Freeze

The final data freeze must record:

- exact public source
- source filename
- source URL
- exact chr20 coordinates
- regional BAM size
- FASTQ size
- read count
- total bases
- sequencing technology
- reference build
- SHA256 checksums

Until these are verified:

**NO LARGE DATA DOWNLOADS**

## Status

Dataset strategy: **FROZEN**

Exact input interval/files: **PENDING VERIFICATION**

---

# Final Regional Benchmark Freeze

## Selected LongReadX Region

**chr20:20,000,001-40,000,000 (GRCh38)**

Region length: **20 Mb**

This interval was selected empirically after scanning HG002 GIAB v5.0q structural-variant truth records across chromosome 20.

## Truth Density

Whole selected interval:

- DEL: 536
- INS: 802
- Total typed DEL/INS records: 1,338

Within the official GIAB structural-variant benchmark regions:

- Benchmark-covered bases: 14,502,269
- Benchmark coverage: 72.51%
- Benchmarkable DEL: 148
- Benchmarkable INS: 195
- Total benchmarkable DEL/INS: 343

## Benchmark Resources

Sample: HG002 / NA24385  
Genome: GRCh38  
Benchmark: GIAB v5.0q structural variants

Files:

- HG002_GRCh38_v5.0q_stvar.vcf.gz
- HG002_GRCh38_v5.0q_stvar.vcf.gz.tbi
- HG002_GRCh38_v5.0q_stvar.benchmark.bed
- NIST_HG002_v5.0q_variant-benchmarksets_README.md

## Decision

**REGION LOCKED**

LongReadX downstream analysis will use:

HG002 PacBio HiFi  
→ chr20:20,000,001-40,000,000  
→ GRCh38  
→ Sniffles2 primary SV calling  
→ cuteSV comparison  
→ GIAB v5.0q truth  
→ Truvari benchmarking

The selected region will not be changed unless a verified technical incompatibility is discovered.
