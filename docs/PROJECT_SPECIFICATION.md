# LongReadX — Project Specification

## Project Title

**LongReadX — Long-Read Structural Variant Analysis**

## Project Type

Production-style long-read genomics and structural-variant workflow engineering project.

## Primary Career Relevance

LongReadX is designed to demonstrate skills relevant to:

- Bioinformatics Pipeline Engineer
- Genomics Workflow Engineer
- NGS Pipeline Engineer
- Cloud Bioinformatics Engineer
- Long-Read Genomics Analyst
- Clinical Genomics Pipeline Engineer

---

## Scientific Objective

LongReadX will build a reproducible PacBio HiFi structural-variant workflow using a resource-conscious subset of the HG002 benchmark genome.

The workflow will detect, filter, annotate, benchmark and interactively explore structural variants while remaining suitable for execution on a local WSL2 workstation.

---

## Primary Research Question

> How accurately can a lightweight PacBio HiFi workflow detect structural variants from a restricted HG002 benchmark region, and how does performance vary by structural-variant class and size?

## Secondary Research Question

> Which detected structural variants overlap genes or functionally relevant genomic regions, and how do results differ between structural-variant callers?

---

## Locked Biological / Technical Scope

### Sequencing technology

**PacBio HiFi**

### Benchmark sample

**HG002 / NA24385**

### Genome build

**GRCh38**

### Genomic scope

**Chromosome 20 regional subset**

Target region size:

**approximately 15–20 Mb**

The exact interval is intentionally not frozen yet.

It will be selected objectively after examining the density and distribution of benchmarkable GIAB structural variants on chromosome 20.

---

## Compute Constraints

Execution environment:

- WSL2 Linux
- Approximately 7.6 GB RAM
- Local disk with substantial free space
- CPU usage intentionally limited to safe local settings

### Data-budget constraint

**Active LongReadX working data should remain ≤1.5 GB whenever practical.**

The project must not download or retain a normal full-depth human long-read whole-genome dataset.

Large temporary intermediate files may be deleted after validation to maintain the project budget.

---

## Input Strategy

LongReadX will not begin from an already finalized SV VCF.

The intended workflow begins with genuine PacBio HiFi reads corresponding to the selected HG002 chr20 interval.

The preferred strategy is:

1. Identify official/public HG002 PacBio HiFi source data.
2. Use indexed regional access where technically possible.
3. Extract only the selected chr20 benchmark interval.
4. Convert the retained reads to FASTQ if necessary.
5. Independently realign those reads to the frozen reference.

This preserves a real:

FASTQ → alignment → BAM → SV calling

workflow.

---

## Core Workflow

```text
PacBio HiFi long reads
        ↓
Long-read QC
        ↓
Read length / quality statistics
        ↓
Reference preparation
        ↓
minimap2 long-read alignment
        ↓
SAM/BAM sorting and indexing
        ↓
BAM QC
        ↓
Sniffles2 structural-variant calling
        ↓
cuteSV comparison branch
        ↓
SV filtering / normalization
        ↓
GIAB benchmark-region restriction
        ↓
Truvari benchmarking
        ↓
TP / FP / FN
        ↓
Precision / Recall / F1
        ↓
SV-type benchmarking
        ↓
Size-stratified benchmarking
        ↓
Gene / genomic-region overlap
        ↓
Structured annotated SV dataset
        ↓
SQLite summary database
        ↓
Streamlit interactive dashboard
Structural Variant Types

LongReadX will support and report SV classes where produced by the selected caller and scientifically meaningful:

DEL — deletion
INS — insertion
DUP — duplication
INV — inversion
BND — breakend / translocation representation where supported

Benchmark claims will only be made for SV classes that are appropriately represented by the selected truth benchmark.

No unsupported accuracy claim will be made for a class simply because the caller emits it.

Primary Tools
Read QC
NanoPlot
seqkit
Alignment
minimap2
BAM processing
samtools
Primary SV caller
Sniffles2
Secondary comparison caller
cuteSV
SV handling
bcftools
BEDTools
Benchmarking
Truvari
Annotation / interpretation
BEDTools
GENCODE gene annotation
Python / pandas
Workflow engineering
Nextflow DSL2
Docker
pytest
GitHub Actions
Reporting
Streamlit
Plotly
SQLite
Why Sniffles2 Is Primary

Sniffles2 is selected because it:

is purpose-built for long-read structural-variant detection
supports PacBio HiFi data
supports major structural-variant classes
is computationally practical
integrates cleanly into BAM-to-VCF workflows
is widely used in long-read SV analysis
is suitable for benchmarking against HG002 truth data
Why cuteSV Is Included

cuteSV is included only as a meaningful comparison caller.

Its purpose is to answer:

How sensitive are LongReadX benchmark results to structural-variant caller choice?

LongReadX will not build a large multi-caller consensus framework.

Two callers are sufficient for this project.

SV Definition

Primary minimum structural-variant size:

50 bp

Filtering will retain structurally valid calls based on:

SVTYPE
SVLEN
FILTER status
genomic interval
caller-specific support where scientifically justified

The exact caller-specific support threshold will be decided after inspecting real output rather than guessed in advance.

Benchmark Goal

LongReadX aims to calculate, where supported:

True Positives
False Positives
False Negatives
Precision
Recall
F1 score
SV-type-specific performance
SV-size-stratified performance

Optional metrics may include:

genotype concordance
breakpoint-distance summaries

These will only be reported when technically supported by the selected truth set and Truvari outputs.

Annotation Goal

The final structural-variant table should contain fields such as:

chromosome
POS
END
SVTYPE
SVLEN
caller
genotype
support
FILTER
gene overlap
gene biotype
genomic region class
truth-match status
benchmark category
Final Deliverables

LongReadX is complete only when it contains:

validated small public PacBio HiFi input
frozen reference
frozen truth benchmark
long-read QC
minimap2 alignment
BAM QC
Sniffles2 calls
cuteSV calls
filtered SV datasets
Truvari benchmarking
gene-overlap annotation
structured summary tables
SQLite database
Nextflow DSL2 pipeline
Docker support
automated tests
GitHub Actions CI
provenance capture
runtime/resource benchmarking
premium Streamlit dashboard
professional README
architecture documentation
live deployment
versioned GitHub release
Explicit Non-Goals

LongReadX will not include:

full human whole-genome long-read processing
assembly generation
hifiasm
methylation analysis
DeepVariant
Clair3
SNP/indel calling
pangenome graph analysis
full-scale haplotype phasing
machine learning
five or more SV callers
paid cloud execution
unnecessary Kubernetes execution
giant VEP cache
tools added only for appearance

The project remains intentionally focused on long-read structural-variant workflow engineering and objective benchmarking.

Project Status

SPECIFICATION FROZEN

Exact source URLs, checksums and the final chr20 interval remain pending Phase 2 verification.
