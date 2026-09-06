import streamlit as st


def apply_global_style():
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1400px;
        }

        .hero {
            padding: 2rem 2.2rem;
            border-radius: 20px;
            border: 1px solid rgba(128,128,128,.22);
            margin-bottom: 1.4rem;
        }

        .eyebrow {
            font-size: .82rem;
            font-weight: 700;
            letter-spacing: .12em;
            opacity: .65;
            margin-bottom: .45rem;
        }

        .hero-title {
            font-size: 2.35rem;
            font-weight: 750;
            line-height: 1.05;
            margin-bottom: .65rem;
        }

        .hero-subtitle {
            font-size: 1.02rem;
            opacity: .78;
            max-width: 900px;
        }

        div[data-testid="stMetric"] {
            border: 1px solid rgba(128,128,128,.20);
            border-radius: 14px;
            padding: 14px;
        }

        h1, h2, h3 {
            letter-spacing: -0.02em;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero(eyebrow, title, subtitle):
    st.markdown(
        f"""
        <div class="hero">
            <div class="eyebrow">{eyebrow}</div>
            <div class="hero-title">{title}</div>
            <div class="hero-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
