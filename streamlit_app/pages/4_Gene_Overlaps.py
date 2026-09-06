import pandas as pd
import streamlit as st
import plotly.express as px

from utils.loaders import load_csv
from utils.paths import SV_TABLE, GENE_SUMMARY
from utils.styles import apply_global_style, hero


st.set_page_config(page_title="Gene Overlaps", layout="wide")
apply_global_style()

hero(
    "LONGREADX • GENOMIC ANNOTATION",
    "SV–Gene Overlap Analysis",
    "Gene-level interpretation of structural variants using GENCODE v49 "
    "GRCh38 chromosome 20 annotations."
)

df = load_csv(SV_TABLE)
summary = load_csv(GENE_SUMMARY).iloc[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total SVs", f'{int(summary["total_svs"]):,}')
c2.metric("Genic SVs", f'{int(summary["genic_svs"]):,}')
c3.metric("Intergenic SVs", f'{int(summary["intergenic_svs"]):,}')
c4.metric(
    "Unique genes",
    f'{int(summary["unique_overlapped_genes"]):,}'
)

genic = df[df["region_class"] == "GENIC"].copy()

genes = []

for value in genic["genes"].dropna():
    for gene in str(value).split(";"):
        if gene and gene != "INTERGENIC":
            genes.append(gene)

counts = (
    pd.Series(genes, name="gene")
    .value_counts()
    .head(20)
    .reset_index()
)

counts.columns = ["gene", "sv_count"]

if len(counts):
    fig = px.bar(
        counts.sort_values("sv_count"),
        x="sv_count",
        y="gene",
        orientation="h",
        labels={"sv_count": "Overlapping SVs", "gene": "Gene"}
    )
    fig.update_layout(title="Top genes overlapped by structural variants")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("### Genic structural variants")

st.dataframe(
    genic[
        [
            "chrom",
            "pos",
            "end",
            "svtype",
            "svlen",
            "genes",
            "gene_types",
            "support"
        ]
    ],
    use_container_width=True,
    hide_index=True
)
