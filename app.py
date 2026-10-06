"""Career Campus - run with: streamlit run app.py"""
import streamlit as st

st.set_page_config(page_title="Career Campus", page_icon="🎓", layout="wide")

from components.sidebar import render_sidebar
from components.styles import inject_css
from database import db
from views import courses, dashboard, interview, quizzes, resume

db.init_db()
inject_css()

def landing():
    st.markdown('<div class="hero"><h1>🎓 Career Campus</h1><p>Learn. Practice. Prepare. Get Career Ready.</p>'
                '<p>Courses, quizzes and progress tracking in one place.</p></div>', unsafe_allow_html=True)
    cols = st.columns(4)
    for col, f in zip(cols, ["📚 Learn Skills", "📝 Take Quizzes", "📊 Track Progress", "🏆 Earn XP"]):
        col.markdown(f'<div class="card"><b>{f}</b></div>', unsafe_allow_html=True)
    t1, t2 = st.tabs(["Login", "Create account"])
    with t1:
        with st.form("login"):
            email, pw = st.text_input("Email"), st.text_input("Password", type="password")
            if st.form_submit_button("Login", type="primary"):
                user = db.login(email, pw)
                if user:
                    st.session_state.uid = user["id"]
                    st.rerun()
                st.error("Incorrect email or password.")
    with t2:
        with st.form("register"):
            name, email = st.text_input("Full name"), st.text_input("Email", key="re")
            pw, pw2 = st.text_input("Password", type="password", key="rp"), st.text_input("Confirm password", type="password")
            if st.form_submit_button("Register", type="primary"):
                if pw != pw2:
                    st.error("Passwords do not match.")
                else:
                    ok, msg = db.register(name, email, pw)
                    (st.success if ok else st.error)(msg)

if "uid" not in st.session_state:
    landing()
else:
    user = db.get_user(st.session_state.uid)
    render_sidebar(user)
    {"Dashboard": dashboard, "Courses": courses, "Quizzes": quizzes, "Interview Prep": interview, "Resume Builder": resume}[st.session_state.get("nav", "Dashboard")].render(user)
