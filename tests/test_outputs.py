from pathlib import Path
import sqlite3

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "results" / "summary"
BENCH = ROOT / "results" / "benchmarking"


def test_final_files_exist():
    files = [
        SUMMARY / "longreadx_structural_variants.csv",
        SUMMARY / "sv_type_summary.csv",
        SUMMARY / "gene_overlap_summary.csv",
        SUMMARY / "longreadx.db",
        BENCH / "benchmark_summary.csv",
    ]

    for path in files:
        assert path.exists()
        assert path.stat().st_size > 0


def test_structural_variants():
    df = pd.read_csv(
        SUMMARY / "longreadx_structural_variants.csv"
    )

    assert len(df) > 0
    assert set(df["svtype"]).issubset({"DEL", "INS"})
    assert (df["svlen"].abs() >= 50).all()


def test_region_classification():
    df = pd.read_csv(
        SUMMARY / "longreadx_structural_variants.csv"
    )

    assert set(df["region_class"]).issubset(
        {"GENIC", "INTERGENIC"}
    )

    assert (
        (df["region_class"] == "GENIC").sum()
        +
        (df["region_class"] == "INTERGENIC").sum()
        ==
        len(df)
    )


def test_benchmark_metrics():
    df = pd.read_csv(
        BENCH / "benchmark_summary.csv"
    )

    assert set(df["caller"]) == {"sniffles2", "cutesv"}

    for metric in ["precision", "recall", "f1"]:
        assert df[metric].between(0, 1).all()


def test_database():
    db = SUMMARY / "longreadx.db"

    con = sqlite3.connect(db)

    tables = {
        x[0]
        for x in con.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
    }

    expected = {
        "structural_variants",
        "gene_overlaps",
        "sv_type_summary",
        "gene_overlap_summary",
        "benchmark_summary",
    }

    assert expected.issubset(tables)

    csv_count = len(
        pd.read_csv(
            SUMMARY / "longreadx_structural_variants.csv"
        )
    )

    db_count = con.execute(
        "SELECT COUNT(*) FROM structural_variants"
    ).fetchone()[0]

    con.close()

    assert db_count == csv_count
