from pathlib import Path

APP_ROOT = Path(__file__).resolve().parents[1]
DATA = APP_ROOT / "data"

READ_STATS = DATA / "read_stats.csv"
COVERAGE = DATA / "coverage.csv"
FLAGSTAT = DATA / "flagstat.txt"

SV_TABLE = DATA / "longreadx_structural_variants.csv"
SV_TYPE_SUMMARY = DATA / "sv_type_summary.csv"
GENE_SUMMARY = DATA / "gene_overlap_summary.csv"

BENCHMARK = DATA / "benchmark_summary.csv"
BENCHMARK_TYPE = DATA / "benchmark_by_type.csv"
BENCHMARK_SIZE = DATA / "benchmark_by_size.csv"

TRACE = DATA / "nextflow_trace.csv"
