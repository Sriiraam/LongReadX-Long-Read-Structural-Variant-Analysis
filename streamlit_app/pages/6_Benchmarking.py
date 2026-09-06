import streamlit as st
import plotly.express as px

from utils.loaders import load_csv
from utils.paths import BENCHMARK_TYPE, BENCHMARK_SIZE
from utils.styles import apply_global_style, hero


st.set_page_config(page_title="Benchmarking", layout="wide")
apply_global_style()

hero(
    "LONGREADX • GIAB BENCHMARKING",
    "SV-Type and Size-Stratified Performance",
    "Performance against HG002 GIAB v5.0q truth using Truvari, restricted "
    "to the benchmarkable chromosome 20 interval."
)

types = load_csv(BENCHMARK_TYPE).copy()
sizes = load_csv(BENCHMARK_SIZE).copy()

for col in ["precision", "recall", "f1"]:
    types[col] *= 100
    sizes[col] *= 100

st.markdown("### Performance by SV type")

fig = px.bar(
    types,
    x="svtype",
    y="f1",
    color="caller",
    barmode="group",
    text_auto=".2f",
    labels={"f1": "F1 (%)", "svtype": "SV Type"}
)
st.plotly_chart(fig, use_container_width=True)

st.dataframe(
    types,
    use_container_width=True,
    hide_index=True
)

st.markdown("### Performance by SV size")

order = ["50–99 bp", "100–999 bp", "≥1000 bp"]


fig = px.bar(
    sizes,
    x="size_bin",
    y="f1",
    color="caller",
    barmode="group",
    text_auto=".2f",
    category_orders={"size_bin": order},
    labels={"f1": "F1 (%)", "size_bin": "SV size"}
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(
    sizes,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Formal benchmarking is limited to structural variants ≥50 bp "
    "and to GIAB benchmarkable regions."
)
