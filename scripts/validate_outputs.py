#!/usr/bin/env python3

from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

SUMMARY = ROOT / "results" / "summary"
BENCH = ROOT / "results" / "benchmarking"

required = [
    SUMMARY / "longreadx_structural_variants.csv",
    SUMMARY / "sv_type_summary.csv",
    SUMMARY / "gene_overlap_summary.csv",
    SUMMARY / "longreadx.db",
    BENCH / "benchmark_summary.csv",
]

print("=== LongReadX output validation ===")

for f in required:
    if not f.exists():
        raise SystemExit(f"FAIL: missing {f}")
    if f.stat().st_size == 0:
        raise SystemExit(f"FAIL: empty {f}")
    print(f"PASS: {f.relative_to(ROOT)}")

sv = pd.read_csv(SUMMARY / "longreadx_structural_variants.csv")

required_columns = {
    "chrom",
    "pos",
    "end",
    "svtype",
    "svlen",
    "region_class",
}

missing = required_columns - set(sv.columns)

if missing:
    raise SystemExit(
        f"FAIL: structural variant table missing columns: {sorted(missing)}"
    )

if len(sv) == 0:
    raise SystemExit("FAIL: structural variant table contains no variants")

bad_types = set(sv["svtype"].dropna()) - {"DEL", "INS"}

if bad_types:
    raise SystemExit(f"FAIL: unexpected SV types: {bad_types}")

if (sv["svlen"].abs() < 50).any():
    raise SystemExit("FAIL: found structural variant <50 bp")

print(f"PASS: {len(sv)} structural variants")
print(f"PASS: SV types = {sorted(sv['svtype'].unique())}")

bench = pd.read_csv(BENCH / "benchmark_summary.csv")

expected_callers = {"sniffles2", "cutesv"}

if set(bench["caller"]) != expected_callers:
    raise SystemExit(
        f"FAIL: benchmark callers = {set(bench['caller'])}"
    )

for metric in ["precision", "recall", "f1"]:
    if not bench[metric].between(0, 1).all():
        raise SystemExit(f"FAIL: invalid {metric}")

print("PASS: benchmark metrics")

db_path = SUMMARY / "longreadx.db"

con = sqlite3.connect(db_path)

tables = {
    row[0]
    for row in con.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )
}

expected_tables = {
    "structural_variants",
    "gene_overlaps",
    "sv_type_summary",
    "gene_overlap_summary",
    "benchmark_summary",
}

missing_tables = expected_tables - tables

if missing_tables:
    con.close()
    raise SystemExit(
        f"FAIL: database missing tables: {sorted(missing_tables)}"
    )

db_count = con.execute(
    "SELECT COUNT(*) FROM structural_variants"
).fetchone()[0]

con.close()

if db_count != len(sv):
    raise SystemExit(
        f"FAIL: database has {db_count} variants; CSV has {len(sv)}"
    )

print(f"PASS: SQLite structural_variants = {db_count}")
print("=== VALIDATION PASSED ===")
