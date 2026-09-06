import re
import streamlit as st

from utils.loaders import load_csv, load_text
from utils.paths import COVERAGE, FLAGSTAT
from utils.styles import apply_global_style, hero


st.set_page_config(page_title="Alignment QC", layout="wide")
apply_global_style()

hero(
    "LONGREADX • ALIGNMENT",
    "minimap2 Alignment Quality",
    "Alignment performance after independent PacBio HiFi realignment using "
    "the minimap2 map-hifi preset."
)

coverage = load_csv(COVERAGE).iloc[0]
flagstat = load_text(FLAGSTAT)

primary_match = re.search(
    r"(\d+) \+ \d+ primary mapped \(([0-9.]+)%",
    flagstat
)

total_match = re.search(
    r"(\d+) \+ \d+ in total",
    flagstat
)

mapped_match = re.search(
    r"(\d+) \+ \d+ mapped \(([0-9.]+)%",
    flagstat
)

primary_rate = float(primary_match.group(2)) if primary_match else 0
total = int(total_match.group(1)) if total_match else 0
mapped_rate = float(mapped_match.group(2)) if mapped_match else 0

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total alignments", f"{total:,}")
c2.metric("Primary mapped", f"{primary_rate:.2f}%")
c3.metric("Mean depth", f'{coverage["meandepth"]:.2f}×')
c4.metric("Breadth ≥1×", f'{coverage["coverage"]:.2f}%')

c1, c2, c3 = st.columns(3)

c1.metric("Overall mapped", f"{mapped_rate:.2f}%")
c2.metric("Mean MAPQ", f'{coverage["meanmapq"]:.1f}')
c3.metric("Covered bases", f'{int(coverage["covbases"]):,}')

st.markdown("### samtools flagstat")
st.code(flagstat)
