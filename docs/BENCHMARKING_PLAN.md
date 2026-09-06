
LongReadX — Structural Variant Benchmarking Plan
Status

BENCHMARK STRATEGY FROZEN

Exact truth URLs and selected chr20 interval remain pending verification.

Benchmark Sample

HG002 / NA24385

Truth Resource

LongReadX will use:

Genome in a Bottle HG002 v5.0q structural-variant benchmark

Genome build:

GRCh38

Planned truth components:

HG002_GRCh38_v5.0q_stvar.vcf.gz
HG002_GRCh38_v5.0q_stvar.vcf.gz.tbi
HG002_GRCh38_v5.0q_stvar.benchmark.bed

Exact file names and URLs must be verified before download.

Benchmark Tool

Primary evaluation tool:

Truvari

Benchmark Principle

Only calls inside official GIAB benchmark regions are eligible for formal performance evaluation.

A structural variant outside the benchmarkable region must not automatically be classified as a false positive.

Callers to Benchmark
Primary

Sniffles2

Secondary

cuteSV

Each caller will be benchmarked independently against the same truth set.

Core Metrics

LongReadX will report:

True Positives
TP
False Positives
FP
False Negatives
FN
Precision
Precision = TP / (TP + FP)
Recall
Recall = TP / (TP + FN)
F1 score
F1 = 2 × Precision × Recall / (Precision + Recall)
Caller Comparison

Final benchmark summary will compare:

Metric	Sniffles2	cuteSV
TP		
FP		
FN		
Precision		
Recall		
F1		

Values will only be populated from actual Truvari output.

SV-Type Stratification

Where supported by the truth benchmark, performance will be calculated separately for:

DEL
INS

Additional types may be summarized descriptively if appropriately represented.

No formal performance metric will be claimed for an SV class without suitable truth representation.

Size Stratification

Planned size bins:

50–99 bp
100–499 bp
500–999 bp
1–4,999 bp
>=5,000 bp

These bins may be adjusted if the regional truth dataset contains too few variants in individual categories.

Any adjustment must be documented.

Additional Benchmark Analyses

Where available from Truvari:

genotype concordance
breakpoint-distance distributions
size agreement
sequence similarity for resolved insertions

These metrics are secondary.

Benchmark Region Selection

Before input extraction, the GIAB truth set will be used to examine chr20.

Window-level analysis will calculate:

number of truth SVs
DEL count
INS count
benchmarkable bases
SV density per Mb

Candidate windows will then be ranked.

The final LongReadX interval will favor:

high benchmarkable coverage
adequate SV count
mixed SV classes
manageable expected input size
Minimum Benchmark Adequacy

LongReadX should ideally contain enough truth variants to make precision and recall informative.

If the selected interval produces only a very small number of benchmark SVs, the interval should be reconsidered before sequencing data are downloaded.

Benchmark Outputs

Planned output structure:

results/benchmarking/
├── sniffles/
│   ├── summary.json
│   ├── tp-base.vcf.gz
│   ├── tp-call.vcf.gz
│   ├── fp.vcf.gz
│   └── fn.vcf.gz
│
├── cutesv/
│   ├── summary.json
│   ├── tp-base.vcf.gz
│   ├── tp-call.vcf.gz
│   ├── fp.vcf.gz
│   └── fn.vcf.gz
│
├── benchmark_summary.csv
├── benchmark_by_svtype.csv
└── benchmark_by_size.csv

Exact Truvari output names may vary by version and will be documented during implementation.

Legitimate Claims

LongReadX may claim:

benchmarked performance within the selected GIAB benchmark region
precision
recall
F1
caller comparison
DEL / INS performance when supported
size-stratified performance

LongReadX must not claim:

whole-genome performance
clinical diagnostic sensitivity
population-level performance
universal caller superiority
performance outside the selected benchmark region
Benchmark Reproducibility

The following must be recorded:

Truvari version
command line
truth VCF checksum
benchmark BED checksum
caller VCF checksum
reference build
genomic interval
minimum SV size
benchmark parameters
