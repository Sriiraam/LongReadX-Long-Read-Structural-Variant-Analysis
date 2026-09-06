import streamlit as st
import plotly.express as px

from utils.loaders import load_csv
from utils.paths import SV_TABLE
from utils.styles import apply_global_style, hero


st.set_page_config(page_title="SV Explorer", layout="wide")
apply_global_style()

hero(
    "LONGREADX • STRUCTURAL VARIANTS",
    "Interactive SV Explorer",
    "Explore high-confidence Sniffles2 deletions and insertions across the "
    "selected HG002 chromosome 20 interval."
)

df = load_csv(SV_TABLE)

left, right = st.columns(2)

with left:
    svtypes = st.multiselect(
        "SV type",
        sorted(df["svtype"].unique()),
        default=sorted(df["svtype"].unique())
    )

with right:
    region = st.multiselect(
        "Genomic context",
        sorted(df["region_class"].unique()),
        default=sorted(df["region_class"].unique())
    )

plot = df[
    df["svtype"].isin(svtypes)
    & df["region_class"].isin(region)
].copy()

c1, c2, c3 = st.columns(3)

c1.metric("Displayed SVs", f"{len(plot):,}")
c2.metric("Median SV size", f'{plot["svlen"].median():,.0f} bp')
c3.metric("Maximum SV size", f'{plot["svlen"].max():,.0f} bp')

fig = px.histogram(
    plot,
    x="svlen",
    color="svtype",
    nbins=50,
    log_y=True,
    labels={"svlen": "SV length (bp)"}
)
fig.update_layout(title="Structural-variant size distribution")
st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(
    plot,
    x="pos",
    y="svlen",
    color="svtype",
    hover_data=["genes", "region_class", "support"],
    labels={
        "pos": "chr20 position",
        "svlen": "SV length (bp)"
    }
)
fig.update_layout(title="SV genomic position and size")
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Structural variant table")

st.dataframe(
    plot.sort_values("pos"),
    use_container_width=True,
    hide_index=True
)
