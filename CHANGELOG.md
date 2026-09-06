# Changelog

All notable changes to LongReadX are documented in this file.

The project follows a simple versioned-release model.

---

## [0.1.0] - 2026-09-06

### Added

- Initial LongReadX project release
- PacBio HiFi HG002 regional benchmark dataset design
- Locked GRCh38 chr20 interval:
  - chr20:20,000,001-40,000,000
- GIAB HG002 v5.0q structural-variant truth integration
- Long-read input quality assessment using seqkit
- GRCh38 chr20 reference preparation
- PacBio HiFi alignment using minimap2 `map-hifi`
- BAM sorting, indexing and quality assessment using samtools
- Sniffles2 primary structural-variant calling
- cuteSV comparison structural-variant calling
- Structural-variant filtering for:
  - PASS calls
  - DEL
  - INS
  - SV length >=50 bp
- Truvari benchmarking against GIAB truth
- Overall benchmark metrics:
  - TP
  - FP
  - FN
  - precision
  - recall
  - F1
  - genotype concordance
- SV-type-specific benchmarking
- SV-size-stratified benchmarking
- GENCODE v49 chr20 gene annotation
- BEDTools-based gene overlap analysis
- Final structured SV dataset
- SQLite summary database
- Modular Nextflow DSL2 workflow
- Docker execution environment
- pytest validation
- repository validation script
- GitHub Actions CI
- interactive Streamlit dashboard
- lightweight deployment data snapshot
- project architecture and frozen decision documentation

### Benchmark Highlights

#### Sniffles2

- Precision: 95.45%
- Recall: 70.95%
- F1: 81.40%
- Genotype concordance: 79.05%

#### cuteSV

- Precision: 95.10%
- Recall: 65.54%
- F1: 77.60%
- Genotype concordance: 73.20%

### Notes

LongReadX v0.1.0 is intentionally scoped to a compact HG002 chr20 benchmark
region rather than full whole-genome long-read processing in order to remain
reproducible on modest local hardware.
