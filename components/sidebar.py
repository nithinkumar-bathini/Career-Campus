import streamlit as st

PAGES = {"Dashboard": "🏠", "Courses": "📚", "Quizzes": "📝", "Interview Prep": "🎯", "Resume Builder": "📄"}

def render_sidebar(user):
    with st.sidebar:
        st.title("🎓 Career Campus")
        level, xp = user["xp"] // 100 + 1, user["xp"] % 100
        st.caption(f"👤 {user['name']}  ·  Level {level}")
        st.progress(xp / 100, text=f"{xp}/100 XP")
        st.radio("Navigate", list(PAGES), key="nav", format_func=lambda p: f"{PAGES[p]}  {p}")
        if st.button("Log out", use_container_width=True):
            st.session_state.clear()
            st.rerun()
