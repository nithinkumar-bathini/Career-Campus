import streamlit as st
from data.content import INTERVIEW
from database import db

def render(user):
    uid = user["id"]
    st.title("🎯 Interview Preparation")
    known = db.known_questions(uid)
    total = sum(len(v) for v in INTERVIEW.values())
    st.progress(len(known & {q for v in INTERVIEW.values() for q, _ in v}) / total, text="Overall interview progress")
    cat = st.selectbox("Category", list(INTERVIEW))
    qs = INTERVIEW[cat]
    st.caption(f"{sum(q in known for q, _ in qs)}/{len(qs)} known in {cat}")
    for i, (q, a) in enumerate(qs):
        with st.expander(("✅ " if q in known else "❓ ") + q):
            if st.toggle("Show answer", key=f"ans_{cat}_{i}"):
                st.info(a)
            if q in known:
                if st.button("Practice again", key=f"pa_{cat}_{i}"):
                    db.set_known(uid, q, False)
                    st.rerun()
            elif st.button("Mark as known", key=f"mk_{cat}_{i}", type="primary"):
                db.set_known(uid, q, True)
                st.rerun()
    st.info("Tip: answer out loud first, then reveal the answer.")
