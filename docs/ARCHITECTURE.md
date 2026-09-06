
LongReadX — Workflow Architecture
High-Level Architecture
PUBLIC PACBIO HIFI SOURCE
            │
            ▼
REGIONAL INPUT EXTRACTION
            │
            ▼
        FASTQ INPUT
            │
            ▼
      LONG-READ QC
   NanoPlot + seqkit
            │
            ▼
    REFERENCE PREPARATION
       GRCh38 chr20
            │
            ▼
        ALIGNMENT
    minimap2 -x map-hifi
            │
            ▼
       BAM PROCESSING
    samtools sort/index
            │
            ▼
          BAM QC
            │
      ┌─────┴─────┐
      ▼           ▼
  SNIFFLES2     cuteSV
  PRIMARY       SECONDARY
      │           │
      ▼           ▼
 FILTERED SV    FILTERED SV
      │           │
      └─────┬─────┘
            ▼
      CALLER COMPARISON
            │
            ▼
      TRUVARI BENCHMARK
            │
            ▼
 TP / FP / FN / PRECISION / RECALL / F1
            │
            ▼
    TYPE + SIZE STRATIFICATION
            │
            ▼
      GENE OVERLAP
        BEDTools
            │
            ▼
      STRUCTURED SV TABLE
            │
            ▼
         SQLite
            │
            ▼
    STREAMLIT DASHBOARD
Nextflow Architecture

Planned modules:

workflow/modules/

read_qc.nf
reference_prepare.nf
align_minimap2.nf
bam_qc.nf
sniffles.nf
cutesv.nf
sv_filter.nf
truvari_bench.nf
sv_annotation.nf
sv_summary.nf
sqlite_build.nf

The exact module boundaries may be refined during implementation but should remain compact.

Data Flow
Raw input
data/raw/
Reference
data/reference/
Truth data
data/truth/
Temporary data
data/interim/
Final compact processed data
data/processed/
Results
results/
├── qc/
├── alignment/
├── sv_calls/
├── filtered/
├── annotation/
├── benchmarking/
└── reports/
Software Layers
Biological / analytical layer
NanoPlot
seqkit
minimap2
samtools
Sniffles2
cuteSV
bcftools
BEDTools
Truvari
Workflow layer
Nextflow DSL2
Data-processing layer
Python
pandas
pysam
SQLite
Testing layer
pytest
GitHub Actions
Presentation layer
Streamlit
Plotly
Reproducibility layer
Docker
Git
provenance capture
checksums
benchmark reports
Dashboard Architecture

Planned pages:

1. Overview
2. Long-Read QC
3. Alignment
4. Structural Variant Explorer
5. Gene Overlaps
6. Caller Comparison
7. Benchmarking
8. Engineering & Performance
Dashboard Visualizations

Meaningful visualizations may include:

read-length histogram
read-quality distribution
read length vs quality scatter
SV chromosome track
SV type composition
SV-size distribution
SV length vs read support
gene-overlap summary
caller concordance
TP / FP / FN comparison
precision / recall / F1 comparison
F1 by SV type
recall by size bin
breakpoint-distance distribution
runtime by process
memory usage by process
Design Principle

LongReadX must remain:

reproducible
compact
interpretable
benchmark-driven
resource-conscious
interview-ready

Complexity is included only when it adds scientific or engineering value.
