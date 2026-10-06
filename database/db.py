"""SQLite storage: users (hashed passwords), enrollments, progress, quiz results, activity, XP."""
import hashlib, secrets, sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("career_campus.db")
XP_REWARD = {"lesson": 10, "quiz": 20}

def conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    with conn() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, pw TEXT, salt TEXT, xp INTEGER DEFAULT 0);
        CREATE TABLE IF NOT EXISTS enrollments(user_id INT, course TEXT, PRIMARY KEY(user_id, course));
        CREATE TABLE IF NOT EXISTS lesson_progress(user_id INT, course TEXT, lesson TEXT, PRIMARY KEY(user_id, course, lesson));
        CREATE TABLE IF NOT EXISTS quiz_results(id INTEGER PRIMARY KEY, user_id INT, course TEXT, score INT, total INT, ts TEXT DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS activity(id INTEGER PRIMARY KEY, user_id INT, text TEXT, ts TEXT DEFAULT CURRENT_TIMESTAMP);
        """)

def _hash(pw, salt):
    return hashlib.pbkdf2_hmac("sha256", pw.encode(), salt.encode(), 100_000).hex()

def register(name, email, pw):
    email = email.strip().lower()
    if not name.strip() or "@" not in email or len(pw) < 6:
        return False, "Enter a name, a valid email and a password of 6+ characters."
    salt = secrets.token_hex(8)
    try:
        with conn() as c:
            c.execute("INSERT INTO users(name,email,pw,salt) VALUES(?,?,?,?)", (name.strip(), email, _hash(pw, salt), salt))
        return True, "Account created - please log in."
    except sqlite3.IntegrityError:
        return False, "That email is already registered."

def login(email, pw):
    with conn() as c:
        u = c.execute("SELECT * FROM users WHERE email=?", (email.strip().lower(),)).fetchone()
    return dict(u) if u and _hash(pw, u["salt"]) == u["pw"] else None

def get_user(uid):
    with conn() as c:
        return dict(c.execute("SELECT id,name,email,xp FROM users WHERE id=?", (uid,)).fetchone())

def log(c, uid, text, xp_key=None):
    c.execute("INSERT INTO activity(user_id,text) VALUES(?,?)", (uid, text))
    if xp_key:
        c.execute("UPDATE users SET xp=xp+? WHERE id=?", (XP_REWARD[xp_key], uid))

def enroll(uid, course):
    with conn() as c:
        cur = c.execute("INSERT OR IGNORE INTO enrollments VALUES(?,?)", (uid, course))
        if cur.rowcount:
            log(c, uid, f"Enrolled in {course}")

def enrolled(uid):
    with conn() as c:
        return [r["course"] for r in c.execute("SELECT course FROM enrollments WHERE user_id=?", (uid,))]

def done_lessons(uid, course):
    with conn() as c:
        return {r["lesson"] for r in c.execute("SELECT lesson FROM lesson_progress WHERE user_id=? AND course=?", (uid, course))}

def complete_lesson(uid, course, lesson):
    """Mark a lesson complete; XP is awarded only the first time."""
    with conn() as c:
        cur = c.execute("INSERT OR IGNORE INTO lesson_progress VALUES(?,?,?)", (uid, course, lesson))
        if cur.rowcount:
            log(c, uid, f"Completed {course}: {lesson}", "lesson")

def save_quiz(uid, course, score, total):
    with conn() as c:
        c.execute("INSERT INTO quiz_results(user_id,course,score,total) VALUES(?,?,?,?)", (uid, course, score, total))
        log(c, uid, f"Quiz {course}: {score}/{total}", "quiz")

def quiz_history(uid):
    with conn() as c:
        return [dict(r) for r in c.execute("SELECT course,score,total,ts FROM quiz_results WHERE user_id=? ORDER BY id", (uid,))]

def recent_activity(uid, n=6):
    with conn() as c:
        return [dict(r) for r in c.execute("SELECT text,ts FROM activity WHERE user_id=? ORDER BY id DESC LIMIT ?", (uid, n))]

# ---- interview questions the user marked as known ----
def _known_table(c):
    c.execute("CREATE TABLE IF NOT EXISTS interview_known(user_id INT, q TEXT, PRIMARY KEY(user_id, q))")

def known_questions(uid):
    with conn() as c:
        _known_table(c)
        return {r["q"] for r in c.execute("SELECT q FROM interview_known WHERE user_id=?", (uid,))}

def set_known(uid, q, known):
    with conn() as c:
        _known_table(c)
        if known:
            cur = c.execute("INSERT OR IGNORE INTO interview_known VALUES(?,?)", (uid, q))
            if cur.rowcount:
                log(c, uid, f"Interview question known: {q[:40]}")
        else:
            c.execute("DELETE FROM interview_known WHERE user_id=? AND q=?", (uid, q))
