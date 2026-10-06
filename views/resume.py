from html import escape as e
import streamlit as st

THEMES = {"Modern (indigo)": "#4f46e5", "Classic (black)": "#1f2937", "Emerald (green)": "#047857"}
FIELDS = ["name", "email", "phone", "location", "linkedin", "github", "summary", "education", "skills",
          "projects", "experience", "certs", "achievements"]

def lines(text):
    return [x.strip() for x in text.splitlines() if x.strip()]


# ---- skills are grouped into categories automatically ----
SKILL_GROUPS = {
    "Programming Languages": "python java c c++ c# sql go rust kotlin swift r matlab php",
    "Web Technologies": "html css javascript js typescript html5 css3 xml json rest api",
    "Frameworks & Libraries": "opencv bootstrap numpy pandas django flask react node.js nodejs angular vue tensorflow pytorch scikit-learn matplotlib streamlit spring express tailwind jquery",
    "Tools": "git github vs code vscode mysql workbench postman docker jupyter linux figma jira excel power bi tableau pycharm eclipse mysql postgresql mongodb sqlite oracle",
    "Core CS": "oop data structures dbms operating systems os computer networks networking algorithms dsa system design",
    "Soft Skills": "time management communication adaptability team collaboration teamwork leadership problem solving critical thinking creativity",
}
SKILL_CAT = {}
for _cat, _words in SKILL_GROUPS.items():
    for _w in _words.split():
        SKILL_CAT[_w] = _cat
# multi-word skills must be matched as phrases
for _phrase, _cat in [("vs code", "Tools"), ("mysql workbench", "Tools"), ("power bi", "Tools"), ("data structures", "Core CS"),
                      ("operating systems", "Core CS"), ("computer networks", "Core CS"), ("system design", "Core CS"),
                      ("time management", "Soft Skills"), ("team collaboration", "Soft Skills"),
                      ("problem solving", "Soft Skills"), ("critical thinking", "Soft Skills"), ("node.js", "Frameworks & Libraries")]:
    SKILL_CAT[_phrase] = _cat
for _junk in ("vs", "code", "mysql workbench".split()[1], "data", "structures", "operating", "systems", "computer", "networks",
              "time", "management", "team", "collaboration", "problem", "solving", "critical", "thinking", "power", "bi", "design", "system", "workbench"):
    SKILL_CAT.pop(_junk, None)

def classify_skills(text):
    """'Python, Git' -> {'Programming Languages': ['Python'], 'Tools': ['Git']}.
    A line like 'Databases: MySQL, MongoDB' is used as a custom category."""
    groups = {}
    for line in text.splitlines():
        if ":" in line:
            label, rest = line.split(":", 1)
            items = [x.strip(" .") for x in rest.split(",") if x.strip(" .")]
            groups.setdefault(label.strip(), []).extend(items)
        else:
            for tok in line.split(","):
                tok = tok.strip(" .")
                if tok:
                    groups.setdefault(SKILL_CAT.get(tok.lower(), "Other Skills"), []).append(tok)
    ordered = {c: groups.pop(c) for c in SKILL_GROUPS if c in groups}
    ordered.update(groups)
    return {c: list(dict.fromkeys(v)) for c, v in ordered.items()}

def skills_html(text):
    return "".join(f'<div style="margin:4px 0;line-height:1.6"><b>{e(cat)}:</b> {e(", ".join(items))}</div>'
                   for cat, items in classify_skills(text).items())

def project_blocks(text):
    """Blank line separates projects. First line = bold title, other lines = bullet points."""
    blocks, cur = [], []
    for ln in text.splitlines():
        if ln.strip():
            cur.append(ln.strip())
        elif cur:
            blocks.append(cur)
            cur = []
    if cur:
        blocks.append(cur)
    out = ""
    for b in blocks:
        out += f'<div style="font-weight:700;margin-top:10px">{e(b[0])}</div>'
        out += bullets([x.lstrip("-•* ").strip() for x in b[1:] if x.lstrip("-•* ").strip()])
    return out

def section(title, inner, color):
    if not inner:
        return ""
    return (f'<div style="margin-top:22px"><div style="font-size:14px;font-weight:700;letter-spacing:1.5px;color:{color};'
            f'border-bottom:2px solid {color};padding-bottom:4px;margin-bottom:8px">{title.upper()}</div>{inner}</div>')

def bullets(items):
    return "<ul style='margin:0;padding-left:20px;line-height:1.6'>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>" if items else ""

def build_html(d):
    c = THEMES.get(d.get("theme"), "#4f46e5")
    contact = " &nbsp;•&nbsp; ".join(e(d[k]) for k in ["email", "phone", "location", "linkedin", "github"] if d.get(k))
    chips = skills_html(d["skills"])
    summary = f"<p style='margin:0;line-height:1.6'>{e(d['summary'])}</p>" if d["summary"].strip() else ""
    body = (section("Professional Summary", summary, c) + section("Education", bullets(lines(d["education"])), c)
            + section("Skills", chips, c) + section("Projects", project_blocks(d["projects"]), c)
            + section("Experience", bullets(lines(d["experience"])), c) + section("Certifications", bullets(lines(d["certs"])), c)
            + section("Achievements", bullets(lines(d["achievements"])), c))
    return (f'<div style="font-family:Arial,Helvetica,sans-serif;max-width:800px;margin:12px auto;background:#fff;color:#222;'
            f'box-shadow:0 4px 24px rgba(0,0,0,.18);border-radius:8px;overflow:hidden">'
            f'<div style="background:{c};color:#fff;padding:28px 34px"><div style="font-size:32px;font-weight:700">{e(d["name"])}</div>'
            f'<div style="margin-top:8px;font-size:13px;opacity:.95">{contact}</div></div>'
            f'<div style="padding:8px 34px 30px;font-size:14px">{body}</div></div>')

def render(user):
    st.title("📄 Resume Builder")
    R = st.session_state.setdefault("rdata", {})
    if st.session_state.get("resume_view") and R.get("name"):
        view(R)
    else:
        form(user, R)

def form(user, R):
    st.caption("Fill in your details, then click **Generate Resume**. Leave sections empty to skip them.")
    with st.form("resume_form"):
        names = list(THEMES)
        theme = st.selectbox("Template", names, index=names.index(R["theme"]) if R.get("theme") in names else 0)
        g = lambda k, dflt="": R.get(k, dflt)
        c1, c2 = st.columns(2)
        d = {"name": c1.text_input("Full name *", g("name", user["name"])), "email": c2.text_input("Email *", g("email", user["email"])),
             "phone": c1.text_input("Phone", g("phone")), "location": c2.text_input("Location", g("location")),
             "linkedin": c1.text_input("LinkedIn", g("linkedin")), "github": c2.text_input("GitHub", g("github"))}
        d["summary"] = st.text_area("Career objective / summary", g("summary"), height=90)
        d["education"] = st.text_area("Education (one per line)", g("education"), height=90, placeholder="B.Tech CSE, ABC University, 2021-2025, CGPA 8.5")
        d["skills"] = st.text_area("Skills (comma separated - they are grouped automatically)", g("skills"), height=90,
                                   placeholder="Python, SQL, HTML, CSS, JavaScript, NumPy, Pandas, Git, GitHub, OOP, Communication")
        d["projects"] = st.text_area("Projects - title on the first line, then one point per line. Leave a blank line between projects.",
                                     g("projects"), height=170,
                                     placeholder="Career Campus - Learning Platform\nBuilt courses, quizzes and a resume builder using Streamlit\nStored user progress in SQLite\n\nWeather App\nFetched live data from an API\nDisplayed charts using Plotly")
        d["experience"] = st.text_area("Experience / internships (one per line)", g("experience"), height=90)
        d["certs"] = st.text_area("Certifications (one per line)", g("certs"), height=70)
        d["achievements"] = st.text_area("Achievements (one per line)", g("achievements"), height=70)
        go = st.form_submit_button("✨ Generate Resume", type="primary", use_container_width=True)
    if go:
        if not d["name"].strip() or "@" not in d["email"]:
            st.error("Please enter your name and a valid email.")
        else:
            R.update(d, theme=theme)
            st.session_state.resume_view = True
            st.rerun()

def view(R):
    st.success("🎉 Your resume is ready!")
    b1, b2 = st.columns([1, 3])
    if b1.button("✏️ Edit details"):
        st.session_state.resume_view = False
        st.rerun()
    html = build_html(R)
    b2.download_button("⬇ Download resume (HTML)", html, file_name=f"{R['name'].replace(' ', '_')}_resume.html", mime="text/html", type="primary")
    st.components.v1.html(html, height=900, scrolling=True)
    st.caption("For a PDF: open the downloaded file in your browser → Print → Save as PDF. The layout is plain text-based, so it is ATS-friendly.")
