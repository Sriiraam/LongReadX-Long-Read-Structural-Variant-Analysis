#!/usr/bin/env python3

from pathlib import Path
import json
import shutil
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUT = ROOT / "streamlit_app" / "data"
OUT.mkdir(parents=True, exist_ok=True)

# ---------- Read QC ----------
read_stats = pd.read_csv(
    RESULTS / "qc" / "read_stats.txt",
    sep="\t"
)
read_stats.to_csv(OUT / "read_stats.csv", index=False)

# ---------- Coverage ----------
coverage = pd.read_csv(
    RESULTS / "bam_qc" / "coverage.txt",
    sep="\t"
)
coverage.to_csv(OUT / "coverage.csv", index=False)

# ---------- Flagstat ----------
shutil.copy(
    RESULTS / "bam_qc" / "flagstat.txt",
    OUT / "flagstat.txt"
)

# ---------- Main summaries ----------
for name in [
    "longreadx_structural_variants.csv",
    "sv_type_summary.csv",
    "gene_overlap_summary.csv",
]:
    shutil.copy(
        RESULTS / "summary" / name,
        OUT / name
    )

shutil.copy(
    RESULTS / "benchmarking" / "benchmark_summary.csv",
    OUT / "benchmark_summary.csv"
)

# ---------- Benchmark by SV type ----------
rows = []

for caller in ["sniffles2", "cutesv"]:
    for svtype in ["DEL", "INS"]:
        path = RESULTS / "benchmarking" / f"{caller}_{svtype}" / "summary.json"

        with open(path) as f:
            x = json.load(f)

        rows.append({
            "caller": caller,
            "svtype": svtype,
            "tp": x["TP-base"],
            "fp": x["FP"],
            "fn": x["FN"],
            "precision": x["precision"],
            "recall": x["recall"],
            "f1": x["f1"],
            "gt_concordance": x.get("gt_concordance")
        })

pd.DataFrame(rows).to_csv(
    OUT / "benchmark_by_type.csv",
    index=False
)

# ---------- Benchmark by size ----------
rows = []

labels = {
    "50_99": "50–99 bp",
    "100_999": "100–999 bp",
    "1000_plus": "≥1000 bp"
}

for caller in ["sniffles2", "cutesv"]:
    for key, label in labels.items():

        path = (
            RESULTS
            / "benchmarking"
            / f"{caller}_size_{key}"
            / "summary.json"
        )

        with open(path) as f:
            x = json.load(f)

        rows.append({
            "caller": caller,
            "size_bin": label,
            "tp": x["TP-base"],
            "fp": x["FP"],
            "fn": x["FN"],
            "precision": x["precision"],
            "recall": x["recall"],
            "f1": x["f1"]
        })

pd.DataFrame(rows).to_csv(
    OUT / "benchmark_by_size.csv",
    index=False
)

# ---------- Nextflow trace ----------
trace = RESULTS / "nextflow_trace.txt"

if trace.exists():
    try:
        df = pd.read_csv(trace, sep="\t")
        df.to_csv(OUT / "nextflow_trace.csv", index=False)
    except Exception:
        pass

print("Dashboard data prepared:")

for f in sorted(OUT.iterdir()):
    print(f"  {f.name}: {f.stat().st_size / 1024:.1f} KB")
