import streamlit as st

from utils.loaders import load_csv
from utils.paths import READ_STATS
from utils.styles import apply_global_style, hero


st.set_page_config(page_title="Long-Read QC", layout="wide")
apply_global_style()

hero(
    "LONGREADX • READ QC",
    "PacBio HiFi Read Quality",
    "Input-read yield, length distribution summary and base-quality metrics."
)

df = load_csv(READ_STATS)
r = df.iloc[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Reads", f'{int(r["num_seqs"]):,}')
c2.metric("Total bases", f'{r["sum_len"]/1e6:.1f} Mb')
c3.metric("Mean length", f'{r["avg_len"]:,.0f} bp')
c4.metric("N50", f'{int(r["N50"]):,} bp')

c1, c2, c3, c4 = st.columns(4)

c1.metric("Minimum", f'{int(r["min_len"]):,} bp')
c2.metric("Maximum", f'{int(r["max_len"]):,} bp')
c3.metric("Q20 bases", f'{r["Q20(%)"]:.1f}%')
c4.metric("Q30 bases", f'{r["Q30(%)"]:.1f}%')

st.markdown("### Read-length quartiles")

q1, q2, q3 = st.columns(3)

q1.metric("Q1", f'{int(r["Q1"]):,} bp')
q2.metric("Median", f'{int(r["Q2"]):,} bp')
q3.metric("Q3", f'{int(r["Q3"]):,} bp')

st.markdown("### Additional metrics")
st.dataframe(df, use_container_width=True, hide_index=True)
