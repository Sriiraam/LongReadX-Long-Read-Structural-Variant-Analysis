import streamlit as st
import plotly.express as px

from utils.loaders import load_csv
from utils.paths import TRACE
from utils.styles import apply_global_style, hero


st.set_page_config(page_title="Engineering", layout="wide")
apply_global_style()

hero(
    "LONGREADX • WORKFLOW ENGINEERING",
    "Pipeline Engineering & Performance",
    "Nextflow DSL2 orchestration, reproducibility, modular SV analysis and "
    "execution-performance tracking."
)

st.markdown("### Engineering stack")

stack = {
    "Component": [
        "Workflow orchestration",
        "Long-read alignment",
        "BAM processing",
        "Primary SV caller",
        "Comparison caller",
        "Benchmarking",
        "Gene overlap",
        "Structured storage",
        "Containerization",
        "Testing",
        "Dashboard",
    ],
    "Technology": [
        "Nextflow DSL2",
        "minimap2",
        "samtools",
        "Sniffles2",
        "cuteSV",
        "Truvari",
        "BEDTools + GENCODE",
        "SQLite",
        "Docker",
        "pytest",
        "Streamlit + Plotly",
    ],
}

st.dataframe(stack, use_container_width=True, hide_index=True)

if TRACE.exists():

    try:
        trace = load_csv(TRACE)

        st.markdown("### Nextflow execution trace")
        st.dataframe(trace, use_container_width=True, hide_index=True)

        if "process" in trace.columns and "duration" in trace.columns:

            fig = px.bar(
                trace,
                x="process",
                y="duration",
                labels={
                    "process": "Process",
                    "duration": "Duration"
                }
            )

            fig.update_layout(title="Process runtime")
            st.plotly_chart(fig, use_container_width=True)

    except Exception:
        st.info("Nextflow trace is available but could not be charted.")

else:
    st.info(
        "Nextflow trace will be included after the final clean workflow run."
    )

st.markdown("### Workflow modules")

st.code(
"""READ_QC
MINIMAP2_ALIGN
BAM_QC
SNIFFLES2
CUTESV
FILTER_SNIFFLES2
FILTER_CUTESV
TRUVARI_SNIFFLES2
TRUVARI_CUTESV
BENCHMARK_SUMMARY
SV_ANNOTATION
SV_SUMMARY"""
)
