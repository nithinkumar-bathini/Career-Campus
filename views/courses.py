import streamlit as st
from data.content import COURSES
from database import db

def catalog(user):
    st.title("📚 Courses")
    q = st.text_input("Search courses", placeholder="e.g. python")
    cats = ["All"] + sorted({c["category"] for c in COURSES.values()})
    cat = st.selectbox("Category", cats)
    mine = db.enrolled(user["id"])
    def hay(n, c):  # search name, category, keywords and lesson titles
        return " ".join([n, c["category"], c.get("keywords", "")] + [t for t, _ in c["lessons"]]).lower()
    shown = [n for n, c in COURSES.items() if q.strip().lower() in hay(n, c) and cat in ("All", c["category"])]
    if not shown:
        st.warning("No courses match your search.")
    cols = st.columns(3)
    for i, name in enumerate(shown):
        c = COURSES[name]
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {c['icon']} {name}")
                st.caption(f"{c['level']} · {len(c['lessons'])} lessons · {c['category']}")
                if name in mine:
                    done = len(db.done_lessons(user["id"], name))
                    st.progress(done / len(c["lessons"]))
                    if st.button("Continue →", key=f"go_{name}", use_container_width=True):
                        st.session_state.open_course = name
                        st.session_state.lesson_idx = 0
                        st.rerun()
                elif st.button("Enroll", key=f"en_{name}", type="primary", use_container_width=True):
                    db.enroll(user["id"], name)
                    st.session_state.open_course = name
                    st.session_state.lesson_idx = 0
                    st.rerun()

def lesson_view(user, name):
    course, uid = COURSES[name], user["id"]
    lessons = course["lessons"]
    done = db.done_lessons(uid, name)
    if st.button("← All courses"):
        st.session_state.open_course = None
        st.rerun()
    st.title(f"{course['icon']} {name}")
    st.progress(len(done) / len(lessons), text=f"{len(done)}/{len(lessons)} lessons complete")
    titles = [t for t, _ in lessons]
    idx = min(st.session_state.get("lesson_idx", 0), len(titles) - 1)
    nav, body = st.columns([1, 3])
    with nav:
        pick = st.radio("Lessons", range(len(titles)), index=idx,
                        format_func=lambda i: f"{'✓' if titles[i] in done else '○'} {titles[i]}")
        if pick != idx:
            st.session_state.lesson_idx = pick
            st.rerun()
    with body:
        title, text = lessons[idx]
        st.header(title)
        st.markdown(text)
        b1, b2, b3 = st.columns(3)
        if b1.button("← Previous", disabled=idx == 0):
            st.session_state.lesson_idx = idx - 1
            st.rerun()
        if b2.button("✅ Mark complete", type="primary", disabled=title in done):
            db.complete_lesson(uid, name, title)
            st.toast("+10 XP")
            st.rerun()
        if b3.button("Next →", disabled=idx == len(titles) - 1):
            st.session_state.lesson_idx = idx + 1
            st.rerun()

def render(user):
    name = st.session_state.get("open_course")
    lesson_view(user, name) if name in COURSES else catalog(user)
