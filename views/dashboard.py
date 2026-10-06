import pandas as pd
import plotly.express as px
import streamlit as st
from components.styles import stat_card
from data.content import COURSES
from database import db

def course_progress(uid, course):
    total = len(COURSES[course]["lessons"])
    return len(db.done_lessons(uid, course)) / total if total else 0

def open_course(uid, course):
    """Button callback: jump to the course page, at the first unfinished lesson."""
    done = db.done_lessons(uid, course)
    titles = [t for t, _ in COURSES[course]["lessons"]]
    st.session_state.open_course = course
    st.session_state.lesson_idx = next((i for i, t in enumerate(titles) if t not in done), 0)
    st.session_state.nav = "Courses"

def render(user):
    uid = user["id"]
    st.title(f"Welcome back, {user['name']}! 👋")
    st.caption("Continue learning and move closer to your career goals.")
    mine = [c for c in db.enrolled(uid) if c in COURSES]
    hist = db.quiz_history(uid)
    prog = {c: course_progress(uid, c) for c in mine}
    avg_prog = sum(prog.values()) / len(prog) if prog else 0
    quiz_avg = sum(h["score"] / h["total"] for h in hist) / len(hist) if hist else 0
    readiness = round((avg_prog * 0.6 + quiz_avg * 0.4) * 100)

    cols = st.columns(4)
    for col, (label, val) in zip(cols, [("Courses enrolled", len(mine)), ("Overall progress", f"{avg_prog:.0%}"),
                                        ("Quiz average", f"{quiz_avg:.0%}"), ("Career readiness", f"{readiness}%")]):
        stat_card(col, label, val)

    st.subheader("Continue learning")
    if not mine:
        st.info("You haven't enrolled yet. Open **Courses** to start your first course!")
    for c in mine:
        with st.container(border=True):
            done, total = len(db.done_lessons(uid, c)), len(COURSES[c]["lessons"])
            st.markdown(f"**{COURSES[c]['icon']} {c}** - {done}/{total} lessons")
            st.progress(prog[c])
            st.button("Continue →", key=f"cont_{c}", on_click=open_course, args=(uid, c))

    left, right = st.columns(2)
    with left:
        st.subheader("Quiz performance")
        if hist:
            df = pd.DataFrame(hist)
            df["pct"] = df.score / df.total * 100
            df["attempt"] = range(1, len(df) + 1)
            st.plotly_chart(px.line(df, x="attempt", y="pct", markers=True, range_y=[0, 100]), use_container_width=True)
        else:
            st.caption("Take a quiz to see your chart.")
    with right:
        st.subheader("Recent activity")
        acts = db.recent_activity(uid)
        for a in acts:
            st.write(f"✓ {a['text']}")
        if not acts:
            st.caption("No activity yet.")
