import streamlit as st
import plotly.express as px

from utils.loaders import load_csv
from utils.paths import BENCHMARK
from utils.styles import apply_global_style, hero


st.set_page_config(page_title="Caller Comparison", layout="wide")
apply_global_style()

hero(
    "LONGREADX • CALLER COMPARISON",
    "Sniffles2 vs cuteSV",
    "Quantitative comparison of two long-read structural-variant callers "
    "against the same GIAB HG002 benchmark."
)

df = load_csv(BENCHMARK).copy()

for col in ["precision", "recall", "f1", "gt_concordance"]:
    df[col] *= 100

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

fig = px.bar(
    df,
    x="caller",
    y=["precision", "recall", "f1"],
    barmode="group",
    labels={
        "value": "Performance (%)",
        "caller": "SV caller"
    }
)

fig.update_layout(title="Overall benchmark performance")
st.plotly_chart(fig, use_container_width=True)

fig = px.bar(
    df,
    x="caller",
    y=["tp", "fp", "fn"],
    barmode="group",
    labels={"value": "Variant count"}
)

fig.update_layout(title="TP / FP / FN comparison")
st.plotly_chart(fig, use_container_width=True)

st.success(
    "Sniffles2 was retained as the primary caller because it achieved "
    "higher recall and F1 while maintaining comparable precision."
)
