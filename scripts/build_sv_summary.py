#!/usr/bin/env python3

import argparse
import json
import sqlite3
from pathlib import Path

import pandas as pd


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sv", required=True)
    p.add_argument("--overlaps", required=True)
    p.add_argument("--benchmark", required=True)
    p.add_argument("--outdir", required=True)
    p.add_argument("--database", required=True)
    args = p.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    sv = pd.read_csv(args.sv)

    overlap_cols = [
        "chrom", "sv_start", "sv_end", "sv_index", "svtype_overlap", "svlen_overlap",
        "gene_chrom", "gene_start", "gene_end", "gene_id", "gene_name", "gene_type"
    ]

    if Path(args.overlaps).stat().st_size > 0:
        overlaps = pd.read_csv(
            args.overlaps,
            sep="\t",
            header=None,
            names=overlap_cols
        )

        if overlaps.shape[1] != 12:
            raise ValueError(
                f"Expected 12 BEDTools overlap columns, found {overlaps.shape[1]}"
            )

        gene_summary = (
            overlaps.groupby("sv_index")
            .agg(
                genes=("gene_name", lambda x: ";".join(sorted(set(map(str, x))))),
                gene_ids=("gene_id", lambda x: ";".join(sorted(set(map(str, x))))),
                gene_types=("gene_type", lambda x: ";".join(sorted(set(map(str, x))))),
                gene_overlap_count=("gene_name", "nunique")
            )
            .reset_index()
        )
    else:
        overlaps = pd.DataFrame(columns=overlap_cols)
        gene_summary = pd.DataFrame(
            columns=["sv_index", "genes", "gene_ids", "gene_types", "gene_overlap_count"]
        )

    sv = sv.reset_index().rename(columns={"index": "sv_index"})
    final = sv.merge(gene_summary, on="sv_index", how="left")

    final["genes"] = final["genes"].fillna("INTERGENIC")
    final["gene_ids"] = final["gene_ids"].fillna(".")
    final["gene_types"] = final["gene_types"].fillna(".")
    final["gene_overlap_count"] = final["gene_overlap_count"].fillna(0).astype(int)

    final["region_class"] = final["gene_overlap_count"].apply(
        lambda n: "GENIC" if n > 0 else "INTERGENIC"
    )

    final.to_csv(
        outdir / "longreadx_structural_variants.csv",
        index=False
    )

    svtype_summary = (
        final.groupby("svtype")
        .agg(
            sv_count=("sv_index", "count"),
            median_sv_length=("svlen", "median"),
            mean_sv_length=("svlen", "mean"),
            max_sv_length=("svlen", "max")
        )
        .reset_index()
    )

    svtype_summary.to_csv(
        outdir / "sv_type_summary.csv",
        index=False
    )

    gene_overlap_summary = pd.DataFrame([{
        "total_svs": len(final),
        "genic_svs": int((final["region_class"] == "GENIC").sum()),
        "intergenic_svs": int((final["region_class"] == "INTERGENIC").sum()),
        "unique_overlapped_genes": int(
            overlaps["gene_name"].nunique() if len(overlaps) else 0
        )
    }])

    gene_overlap_summary.to_csv(
        outdir / "gene_overlap_summary.csv",
        index=False
    )

    benchmark = pd.read_csv(args.benchmark)

    db = sqlite3.connect(args.database)

    final.to_sql(
        "structural_variants",
        db,
        if_exists="replace",
        index=False
    )

    overlaps.to_sql(
        "gene_overlaps",
        db,
        if_exists="replace",
        index=False
    )

    svtype_summary.to_sql(
        "sv_type_summary",
        db,
        if_exists="replace",
        index=False
    )

    gene_overlap_summary.to_sql(
        "gene_overlap_summary",
        db,
        if_exists="replace",
        index=False
    )

    benchmark.to_sql(
        "benchmark_summary",
        db,
        if_exists="replace",
        index=False
    )

    db.close()

    print(f"Final SVs: {len(final)}")
    print(
        "Genic SVs:",
        int((final["region_class"] == "GENIC").sum())
    )
    print(
        "Unique genes:",
        overlaps["gene_name"].nunique() if len(overlaps) else 0
    )


if __name__ == "__main__":
    main()
