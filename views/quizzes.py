import time
import streamlit as st
from data.content import COURSES, LESSON_QUIZ, QUIZZES
from database import db

def render(user):
    st.title("📝 Quizzes")
    course = st.selectbox("Course", list(COURSES))
    sets = {t: q for (c, t), q in LESSON_QUIZ.items() if c == course}   # one quiz per lesson
    if QUIZZES.get(course):
        sets["General quiz (all topics)"] = QUIZZES[course]
    if not sets:
        st.warning("No quiz questions for this course yet.")
        return
    name = st.selectbox("Lesson quiz", list(sets))
    qs, key = sets[name], f"{course}|{name}"
    s = st.session_state.get("quiz")
    if not s or s["key"] != key:        # new quiz selected -> start fresh
        s = st.session_state.quiz = {"key": key, "i": 0, "ans": [], "t": time.time(), "done": False}

    if not s["done"]:
        i = s["i"]
        st.progress(i / len(qs), text=f"Question {i + 1} of {len(qs)}")
        pick = st.radio(f"**{qs[i][0]}**", qs[i][1], index=None, key=f"r_{key}_{i}")
        last = i == len(qs) - 1
        if st.button("Finish quiz" if last else "Next →", type="primary", disabled=pick is None):
            s["ans"].append(pick)
            if last:
                s["done"] = True
                s["score"] = sum(a == q[2] for a, q in zip(s["ans"], qs))
                s["secs"] = int(time.time() - s["t"])
                db.save_quiz(user["id"], f"{course}: {name}", s["score"], len(qs))
            else:
                s["i"] += 1
            st.rerun()
        return

    pct = s["score"] / len(qs)
    st.success(f"Score: {s['score']}/{len(qs)} ({pct:.0%}) · Time: {s['secs']}s · +20 XP")
    if pct == 1:
        st.balloons()
    for a, q in zip(s["ans"], qs):
        if a != q[2]:
            st.error(f"❌ {q[0]}  \nYour answer: {a} · Correct: **{q[2]}**. {q[3]}")
    if st.button("Retry this quiz"):
        del st.session_state["quiz"]
        for i in range(len(qs)):
            st.session_state.pop(f"r_{key}_{i}", None)
        st.rerun()
