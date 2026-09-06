from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_core_files_exist():
    required = [
        "main.nf",
        "nextflow.config",
        "docker/Dockerfile",
        "scripts/annotate_sv.py",
        "scripts/make_sv_bed.py",
        "scripts/build_sv_summary.py",
        "streamlit_app/app.py",
    ]

    for item in required:
        assert (ROOT / item).exists(), f"Missing: {item}"


def test_nextflow_modules_exist():
    modules = [
        "read_qc.nf",
        "minimap2_align.nf",
        "bam_qc.nf",
        "sniffles2.nf",
        "cutesv.nf",
        "sv_filter.nf",
        "truvari_bench.nf",
        "benchmark_summary.nf",
        "sv_annotation.nf",
        "sv_summary.nf",
    ]

    for module in modules:
        assert (ROOT / "workflow" / "modules" / module).exists()


def test_streamlit_data_exist():
    required = [
        "read_stats.csv",
        "coverage.csv",
        "flagstat.txt",
        "longreadx_structural_variants.csv",
        "sv_type_summary.csv",
        "gene_overlap_summary.csv",
        "benchmark_summary.csv",
        "benchmark_by_type.csv",
        "benchmark_by_size.csv",
    ]

    for item in required:
        path = ROOT / "streamlit_app" / "data" / item
        assert path.exists(), f"Missing dashboard data: {item}"
        assert path.stat().st_size > 0


def test_dashboard_pages_exist():
    pages = list((ROOT / "streamlit_app" / "pages").glob("*.py"))
    assert len(pages) >= 7
