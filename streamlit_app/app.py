import streamlit as st
import plotly.express as px

from utils.loaders import load_csv
from utils.paths import (
    READ_STATS,
    COVERAGE,
    SV_TYPE_SUMMARY,
    GENE_SUMMARY,
    BENCHMARK,
)
from utils.styles import apply_global_style, hero


st.set_page_config(
    page_title="LongReadX",
    page_icon="🧬",
    layout="wide"
)

apply_global_style()

hero(
    "LONGREADX • PACBIO HIFI STRUCTURAL VARIANTS",
    "Long-Read Structural Variant Analysis",
    "A reproducible PacBio HiFi workflow for structural-variant discovery, "
    "GIAB benchmarking, genomic annotation and workflow engineering."
)

reads = load_csv(READ_STATS).iloc[0]
coverage = load_csv(COVERAGE).iloc[0]
svtypes = load_csv(SV_TYPE_SUMMARY)
genes = load_csv(GENE_SUMMARY).iloc[0]
bench = load_csv(BENCHMARK)

sniff = bench.loc[bench["caller"] == "sniffles2"].iloc[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric("HiFi reads", f'{int(reads["num_seqs"]):,}')
c2.metric("Read N50", f'{int(reads["N50"]):,} bp')
c3.metric("Mean depth", f'{coverage["meandepth"]:.2f}×')
c4.metric("Sniffles2 F1", f'{sniff["f1"]*100:.2f}%')

c1, c2, c3, c4 = st.columns(4)

c1.metric("Final SVs", f'{int(svtypes["sv_count"].sum()):,}')
c2.metric("Genic SVs", f'{int(genes["genic_svs"]):,}')
c3.metric("Genes overlapped", f'{int(genes["unique_overlapped_genes"]):,}')
c4.metric("Benchmark precision", f'{sniff["precision"]*100:.2f}%')

st.markdown("## Structural variant landscape")

left, right = st.columns(2)

with left:
    fig = px.bar(
        svtypes,
        x="svtype",
        y="sv_count",
        text="sv_count",
        labels={
            "svtype": "SV Type",
            "sv_count": "Number of SVs"
        }
    )
    fig.update_layout(title="Primary Sniffles2 SV calls")
    st.plotly_chart(fig, use_container_width=True)

with right:
    region_df = {
        "Region": ["Genic", "Intergenic"],
        "SVs": [
            int(genes["genic_svs"]),
            int(genes["intergenic_svs"])
        ]
    }

    fig = px.pie(
        region_df,
        names="Region",
        values="SVs",
        hole=0.55,
        title="Genomic context"
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("## Benchmark overview")

display = bench.copy()
display["precision"] *= 100
display["recall"] *= 100
display["f1"] *= 100
display["gt_concordance"] *= 100

fig = px.bar(
    display,
    x="caller",
    y=["precision", "recall", "f1"],
    barmode="group",
    labels={"value": "Performance (%)", "caller": "Caller"}
)
st.plotly_chart(fig, use_container_width=True)

st.info(
    "Benchmarking uses HG002 GIAB v5.0q GRCh38 structural-variant truth "
    "within the selected chr20:20,000,001–40,000,000 interval."
)
