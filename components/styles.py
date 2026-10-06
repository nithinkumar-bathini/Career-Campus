import streamlit as st

def inject_css():
    st.markdown("""<style>
    .block-container{padding-top:1.5rem;max-width:1150px}
    [data-testid=stSidebar]{background:#1e1b4b}
    [data-testid=stSidebar] *{color:#e0e7ff !important}
    .hero{background:linear-gradient(135deg,#4f46e5,#06b6d4);color:#fff;padding:2.2rem;border-radius:20px;margin-bottom:1rem}
    .hero h1,.hero p{color:#fff;margin:.2rem 0}
    .card{border:1px solid rgba(128,128,128,.25);border-radius:16px;padding:1rem 1.2rem;box-shadow:0 2px 8px rgba(0,0,0,.06);margin-bottom:.6rem}
    .stat{font-size:1.8rem;font-weight:700;color:#4f46e5}
    .muted{opacity:.7;font-size:.85rem}
    div.stButton>button{border-radius:10px;font-weight:600}
    </style>""", unsafe_allow_html=True)

def stat_card(col, label, value):
    col.markdown(f'<div class="card"><div class="muted">{label}</div><div class="stat">{value}</div></div>', unsafe_allow_html=True)
