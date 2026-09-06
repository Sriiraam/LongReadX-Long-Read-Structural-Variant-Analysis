process BENCHMARK_SUMMARY {

    tag "benchmark_summary"

    cpus 1
    memory '1 GB'

    publishDir "${params.outdir}/benchmarking",
        mode: 'copy',
        overwrite: true

    input:
    tuple val(caller_a), path(summary_a), path(tpbase_a), path(tpcomp_a), path(fp_a), path(fn_a)
    tuple val(caller_b), path(summary_b), path(tpbase_b), path(tpcomp_b), path(fp_b), path(fn_b)

    output:
    path "benchmark_summary.csv"

    script:
    """
    python - <<'PY'
import csv
import json

inputs = [
    ("${caller_a}", "${summary_a}"),
    ("${caller_b}", "${summary_b}")
]

rows = []

for caller, path in inputs:
    with open(path) as f:
        x = json.load(f)

    rows.append({
        "caller": caller,
        "tp": x["TP-base"],
        "fp": x["FP"],
        "fn": x["FN"],
        "precision": x["precision"],
        "recall": x["recall"],
        "f1": x["f1"],
        "gt_concordance": x.get("gt_concordance")
    })

with open("benchmark_summary.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "caller",
            "tp",
            "fp",
            "fn",
            "precision",
            "recall",
            "f1",
            "gt_concordance"
        ]
    )
    writer.writeheader()
    writer.writerows(rows)
PY
    """
}
