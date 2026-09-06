
LongReadX — Decision Log
D001 — Use PacBio HiFi
Decision

Use PacBio HiFi instead of Oxford Nanopore for LongReadX v0.1.0.

Reason

PacBio HiFi provides:

high per-read accuracy
strong structural-variant performance
straightforward minimap2 support
compatibility with Sniffles2 and cuteSV
strong HG002 benchmarking ecosystem
lower risk of sequencing-error noise dominating a small benchmark project
Status

ACCEPTED

D002 — Use HG002 / NA24385
Decision

Use HG002 as the benchmark individual.

Reason

HG002 provides:

established Genome in a Bottle truth resources
publicly available long-read sequencing
reproducible benchmarking opportunities
strong industry recognition
Status

ACCEPTED

D003 — Do Not Use Full Whole Genome
Decision

Reject normal full-depth long-read human WGS.

Reason

The project is constrained to approximately:

≤1.5 GB active working data

Full-depth HG002 PacBio/ONT whole-genome datasets would violate this constraint and add unnecessary compute burden.

Status

ACCEPTED

D004 — Use Regional chr20 Subset
Decision

Use a benchmark-rich approximately 15–20 Mb interval from chromosome 20.

Reason

This retains genuine long-read SV analysis while keeping:

downloads manageable
alignment lightweight
BAM size manageable
caller runtime short
benchmarking realistic
Exact interval

PENDING GIAB truth-density analysis.

Status

ACCEPTED

D005 — Use GRCh38
Decision

Use GRCh38 for:

reference
truth benchmark
annotation
alignment
Reason

Avoid unnecessary liftover and keep all resources on one build.

Status

ACCEPTED

D006 — Primary Caller = Sniffles2
Decision

Use Sniffles2 as the main SV caller.

Reason

Sniffles2 is appropriate for:

PacBio HiFi
germline structural variants
major SV classes
lightweight workflow execution
reproducible benchmarking
Status

ACCEPTED

D007 — Secondary Caller = cuteSV
Decision

Use cuteSV as one comparison caller.

Reason

Caller comparison adds genuine scientific value by showing how benchmark performance changes with caller choice.

Constraint

Do not build a large multi-caller consensus system.

Status

ACCEPTED

D008 — Benchmark with Truvari
Decision

Use Truvari.

Truth set

GIAB HG002 v5.0q GRCh38 structural-variant benchmark.

Metrics
TP
FP
FN
precision
recall
F1
SV-type stratification
size stratification
Status

ACCEPTED

D009 — Start with BEDTools Gene Overlap
Decision

Use BEDTools + GENCODE annotation as the primary biological annotation strategy.

Reason

For large SVs, genomic interval overlap is transparent and easy to interpret.

Full VEP will not be added unless it provides clear additional value.

Status

ACCEPTED

D010 — Python Instead of R
Decision

Use Python for:

tabular processing
benchmark parsing
annotation summaries
SQLite
plotting
dashboard support
Reason

R does not provide enough additional value for this workflow to justify a second analysis language.

Status

ACCEPTED

D011 — Use Nextflow DSL2
Decision

Build LongReadX as a modular Nextflow DSL2 workflow.

Reason

Portfolio focus includes:

workflow orchestration
reproducibility
pipeline modularity
resume
container execution
infrastructure readiness
Status

ACCEPTED

D012 — Docker
Decision

Provide one reproducible LongReadX Docker environment.

Reason

Avoid unnecessary per-process containers during the initial portfolio implementation.

Status

ACCEPTED

D013 — No Paid Cloud Execution
Decision

LongReadX will execute locally.

Cloud/HPC profiles may be documented where useful, but the project will not require paid infrastructure.

Status

ACCEPTED

D014 — Lightweight CI
Decision

GitHub Actions will not run the full long-read dataset.

CI will focus on:

pytest
Python compilation
configuration validation
Nextflow syntax/profile validation
tiny fixture/stub tests where practical
Status

ACCEPTED

D015 — Lightweight Streamlit Deployment
Decision

The live Streamlit app will use compact summary files rather than large FASTQ/BAM assets.

Status

ACCEPTED

D016 — Avoid Overengineering

LongReadX will deliberately exclude:

assembly
methylation
ML
many SV callers
full WGS
unnecessary cloud infrastructure
huge annotation caches

The project succeeds through scientific validation and workflow quality, not tool count.

Status

ACCEPTED
