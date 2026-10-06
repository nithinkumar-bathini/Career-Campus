"""Courses, quizzes and interview questions. Add more here; the app picks them up automatically."""
import random

def C(icon, level, cat, lessons):
    return {"icon": icon, "level": level, "category": cat, "lessons": lessons}

COURSES = {
 "Python": C("🐍", "Beginner", "Programming", [
  ("What is Python?", "Python is a readable, general-purpose language used in web, data and AI.\n\n```python\nprint('Hello, Career Campus!')\n```\n**Key points**\n- Easy syntax, huge libraries\n- Run files with `python file.py`"),
  ("Variables & Data Types", "Variables store values.\n\n```python\nname = 'Asha'\nage = 21\nskills = ['Python', 'SQL']\n```\n**Key points**\n- Types: int, float, str, bool, list, dict\n- `type(x)` shows a type"),
  ("Conditions & Loops", "```python\nfor n in range(1, 4):\n    print(n, 'even' if n % 2 == 0 else 'odd')\n```\n**Key points**\n- `if/elif/else` decide\n- `for`/`while` repeat"),
  ("Functions", "```python\ndef square(x):\n    return x * x\nprint(square(5))\n```\n**Key points**\n- `def` defines, `return` gives back a value"),
  ("Lists & Dictionaries", "```python\nnums = [3, 1, 2]\nnums.sort()\nuser = {'name': 'Asha', 'age': 21}\nprint(user['name'])\n```\n**Key points**\n- Lists are ordered; dicts map keys to values"),
 ]),
 "Java": C("☕", "Intermediate", "Programming", [
  ("Java Basics", "Java is compiled to bytecode and runs on the JVM.\n\n```java\npublic class Main {\n  public static void main(String[] a) {\n    System.out.println(\"Hello\");\n  }\n}\n```"),
  ("Variables & Control Flow", "```java\nint age = 20;\nif (age >= 18) System.out.println(\"Adult\");\nfor (int i = 0; i < 3; i++) System.out.println(i);\n```"),
  ("Classes & Objects", "```java\nclass Student {\n  String name;\n  Student(String n) { name = n; }\n}\nStudent s = new Student(\"Ravi\");\n```\n**Key points**\n- OOP: encapsulation, inheritance, polymorphism, abstraction"),
 ]),
 "C": C("🔧", "Beginner", "Programming", [
  ("Introduction to C", "```c\n#include <stdio.h>\nint main() {\n  printf(\"Hello\\n\");\n  return 0;\n}\n```\nC is fast and close to the hardware."),
  ("Data Types & Operators", "```c\nint a = 5; float b = 2.5; char c = 'A';\nprintf(\"%d\", a + 2);\n```"),
  ("Pointers", "A pointer stores a memory address.\n\n```c\nint x = 10;\nint *p = &x;\nprintf(\"%d\", *p);\n```"),
 ]),
 "JavaScript": C("🟨", "Beginner", "Web Development", [
  ("JS Basics", "```javascript\nlet name = 'Asha';\nconst year = 2026;\nconsole.log(`Hi ${name}`);\n```\n- `let`/`const` are block-scoped"),
  ("Functions & Arrays", "```javascript\nconst add = (a, b) => a + b;\n[1,2,3].map(n => n * 2);\n```"),
  ("DOM Manipulation", "```javascript\ndocument.querySelector('h1').textContent = 'Hello';\n```\nThe DOM lets JavaScript change the page."),
 ]),
 "HTML & CSS": C("🌐", "Beginner", "Web Development", [
  ("HTML Basics", "```html\n<h1>Hello</h1>\n<p>My first page.</p>\n<a href=\"https://example.com\">Link</a>\n```"),
  ("CSS Styling", "```css\nh1 { color: #4f46e5; text-align: center; }\n```"),
  ("Flexbox Layout", "```css\n.row { display: flex; gap: 12px; justify-content: space-between; }\n```"),
 ]),
 "SQL": C("🗄️", "Beginner", "Database", [
  ("Intro to Databases", "A database stores data in tables of rows and columns. SQL is the language used to query it."),
  ("SELECT Queries", "```sql\nSELECT name, age FROM students WHERE age > 18 ORDER BY name;\n```"),
  ("JOINs", "```sql\nSELECT s.name, c.title\nFROM students s\nJOIN courses c ON c.id = s.course_id;\n```\n- INNER JOIN keeps matches only; LEFT JOIN keeps all left rows"),
  ("Aggregates & GROUP BY", "```sql\nSELECT course_id, COUNT(*) FROM students GROUP BY course_id;\n```"),
 ]),
 "Django": C("🎸", "Intermediate", "Web Development", [
  ("Django Setup", "```bash\npip install django\ndjango-admin startproject mysite\npython manage.py runserver\n```\nDjango follows the MTV pattern."),
  ("Models & Migrations", "```python\nclass Post(models.Model):\n    title = models.CharField(max_length=100)\n```\n```bash\npython manage.py makemigrations\npython manage.py migrate\n```"),
  ("Views & URLs", "```python\n# views.py\ndef home(request):\n    return HttpResponse('Hi')\n# urls.py\npath('', views.home)\n```"),
 ]),
 "Flask": C("🧪", "Beginner", "Web Development", [
  ("Hello Flask", "```python\nfrom flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home():\n    return 'Hello'\n```"),
  ("Templates", "```python\nreturn render_template('index.html', name='Asha')\n```\nJinja2 fills `{{ name }}` in HTML."),
  ("Forms & Requests", "```python\n@app.route('/login', methods=['POST'])\ndef login():\n    email = request.form['email']\n```"),
 ]),
 "Data Analysis (Pandas)": C("📊", "Intermediate", "Data & AI", [
  ("DataFrames", "```python\nimport pandas as pd\ndf = pd.read_csv('data.csv')\nprint(df.head())\n```"),
  ("Cleaning Data", "```python\ndf = df.dropna()\ndf['age'] = df['age'].astype(int)\n```"),
  ("Grouping & Summaries", "```python\ndf.groupby('city')['sales'].mean()\n```"),
 ]),
 "Git & GitHub": C("🔀", "Beginner", "Tools", [
  ("Git Basics", "```bash\ngit init\ngit add .\ngit commit -m \"first commit\"\n```"),
  ("Branches & Merging", "```bash\ngit checkout -b feature\ngit checkout main\ngit merge feature\n```"),
  ("GitHub Workflow", "```bash\ngit remote add origin <url>\ngit push -u origin main\n```\nPull requests let teammates review code."),
 ]),
}

_QZ = {
 "Python": [("Which keyword defines a function?", "def", ["function", "fun", "define"], "`def` starts a function."),
            ("What does len('abc') return?", "3", ["2", "4", "Error"], "It counts characters."),
            ("Which type is immutable?", "tuple", ["list", "dict", "set"], "Tuples cannot change.")],
 "Java": [("Which method starts a Java program?", "main", ["start", "run", "init"], "`main` is the entry point."),
          ("Which keyword creates an object?", "new", ["create", "make", "object"], "`new` allocates an object."),
          ("Java source compiles to?", "Bytecode", ["Machine code only", "Plain text", "Assembly"], "The JVM runs bytecode.")],
 "C": [("Which header provides printf?", "stdio.h", ["stdlib.h", "string.h", "math.h"], "printf lives in stdio.h."),
       ("What does & give in C?", "Address of a variable", ["Its value", "Its size", "Its type"], "& is address-of."),
       ("C arrays start at index?", "0", ["1", "-1", "2"], "Arrays are zero-indexed.")],
 "JavaScript": [("Which keyword is block-scoped?", "let", ["var", "int", "dim"], "let/const are block-scoped."),
                ("What is 3 === '3'?", "false", ["true", "undefined", "error"], "=== checks type and value."),
                ("Which method adds to an array's end?", "push", ["pop", "shift", "add"], "push appends.")],
 "HTML & CSS": [("Which tag is the largest heading?", "<h1>", ["<h6>", "<head>", "<title>"], "h1 is top-level."),
                ("Which tag creates a link?", "<a>", ["<link>", "<href>", "<url>"], "<a href> makes links."),
                ("Which CSS makes a flex container?", "display: flex", ["flex: on", "layout: flex", "position: flex"], "Use display: flex.")],
 "SQL": [("Which clause filters rows?", "WHERE", ["ORDER BY", "GROUP", "LIMIT"], "WHERE filters rows."),
         ("Which JOIN keeps only matches?", "INNER", ["LEFT", "RIGHT", "FULL"], "INNER returns matches only."),
         ("Which function counts rows?", "COUNT", ["SUM", "TOTAL", "NUM"], "COUNT(*) counts rows.")],
 "Django": [("Django follows which pattern?", "MTV", ["MVC only", "MVVM", "MVP"], "Model-Template-View."),
            ("Which command starts a project?", "django-admin startproject", ["django new", "python create", "pip startproject"], "Use django-admin startproject."),
            ("Which file maps URLs to views?", "urls.py", ["models.py", "admin.py", "apps.py"], "urls.py holds routes.")],
 "Flask": [("Which decorator defines a route?", "@app.route", ["@app.url", "@route.app", "@flask.path"], "@app.route maps URLs."),
           ("Which function renders a template?", "render_template", ["show_html", "render_page", "template()"], "Flask's render_template."),
           ("Flask is a...", "Micro web framework", ["Database", "Browser", "Operating system"], "Lightweight framework.")],
 "Data Analysis (Pandas)": [("Main 2D structure in pandas?", "DataFrame", ["Array", "Tensor", "Tuple"], "DataFrame = table."),
                            ("Which shows the first rows?", "head()", ["top()", "first()", "start()"], "df.head() shows 5 rows."),
                            ("Which drops missing values?", "dropna()", ["removena()", "clean()", "delna()"], "dropna() removes NaNs.")],
 "Git & GitHub": [("Which command saves a snapshot?", "git commit", ["git save", "git push", "git add"], "commit records changes."),
                  ("Which uploads commits to a remote?", "git push", ["git pull", "git clone", "git fetch"], "push uploads."),
                  ("Which copies a repository?", "git clone", ["git copy", "git init", "git fork"], "clone downloads a repo.")],
}

def _mk(q, right, wrong, why):
    opts = [right] + wrong
    random.Random(q).shuffle(opts)   # stable order per question
    return (q, opts, right, why)

QUIZZES = {k: [_mk(*t) for t in v] for k, v in _QZ.items()}

INTERVIEW = {
 "Python": [("Explain list vs tuple.", "Lists are mutable; tuples are immutable and slightly faster. Use tuples for fixed data."),
            ("What is a decorator?", "A function that wraps another function to add behaviour, applied with @name."),
            ("What is the difference between `is` and `==`?", "`==` compares values; `is` compares object identity."),
            ("What are *args and **kwargs?", "They accept any number of positional and keyword arguments.")],
 "SQL": [("INNER JOIN vs LEFT JOIN?", "INNER returns matching rows only; LEFT returns all left rows plus matches."),
         ("What is a primary key?", "A column (or set) that uniquely identifies each row and cannot be NULL."),
         ("WHERE vs HAVING?", "WHERE filters rows before grouping; HAVING filters groups after aggregation.")],
 "Web Development": [("What is the box model?", "Content, padding, border and margin make up every element's box."),
                     ("Explain GET vs POST.", "GET fetches data and is idempotent; POST sends data to create or change something."),
                     ("What is REST?", "An API style using HTTP methods on resource URLs, with stateless requests.")],
 "HR": [("Tell me about yourself.", "Give present, past, future in 60-90 seconds, focused on the role."),
        ("What are your strengths and weaknesses?", "Name a real strength with proof; a real weakness with how you're improving it."),
        ("Why should we hire you?", "Match your skills and projects to their needs, with one concrete result."),
        ("Where do you see yourself in 5 years?", "Show growth in the field and commitment to learning, not a fixed title.")],
}

# ======================= EXTRA CONTENT (deeper lessons, more quiz + interview questions) =======================
COURSES["Python"]["lessons"] += [
 ("Operators", "Operators work on values.\n\n```python\nprint(7 // 2, 7 % 2, 2 ** 3)   # 3 1 8\nprint(5 > 3 and not False)     # True\n```\n**Key points**\n- Arithmetic: `+ - * / // % **`\n- Comparison: `== != < >`; logical: `and or not`\n\n**Practice:** Print the remainder of 17 divided by 5."),
 ("Strings", "Strings are text, and you can slice and format them.\n\n```python\ns = 'Career Campus'\nprint(s.upper(), s[0:6], len(s))\nprint(f'Hi {s}')\n```\n**Key points**\n- Strings are immutable\n- Methods: `split`, `join`, `strip`, `replace`\n\n**Practice:** Reverse a string using slicing (`s[::-1]`)."),
 ("Tuples & Sets", "```python\npoint = (3, 4)          # tuple: fixed\ntags = {'py', 'sql', 'py'}  # set: unique -> {'py','sql'}\nprint('py' in tags)\n```\n**Key points**\n- Tuples are immutable; sets remove duplicates\n- Sets support union `|` and intersection `&`\n\n**Practice:** Remove duplicates from `[1,2,2,3]`."),
 ("Modules & Packages", "A module is a `.py` file you can import.\n\n```python\nimport math\nfrom random import randint\nprint(math.sqrt(16), randint(1, 6))\n```\n**Key points**\n- Install packages with `pip install name`\n- A package is a folder of modules\n\n**Practice:** Print today's date using `datetime`."),
 ("Exception Handling", "```python\ntry:\n    n = int(input('Number: '))\n    print(10 / n)\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')\nexcept ValueError:\n    print('Enter digits only')\nfinally:\n    print('Done')\n```\n**Key points**\n- `try` runs code, `except` handles errors, `finally` always runs\n\n**Practice:** Handle a missing key in a dictionary."),
 ("OOP: Classes & Objects", "```python\nclass Student:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        return f'Hi, {self.name}'\n\nprint(Student('Asha').greet())\n```\n**Key points**\n- `__init__` sets up the object; `self` is the instance\n- Inheritance: `class B(A):`\n\n**Practice:** Create a `Car` class with a `drive()` method."),
 ("File Handling", "```python\nwith open('notes.txt', 'w') as f:\n    f.write('hello')\nwith open('notes.txt') as f:\n    print(f.read())\n```\n**Key points**\n- Modes: `r` read, `w` write, `a` append\n- `with` closes the file automatically\n\n**Practice:** Count the lines in a text file."),
 ("Comprehensions & Lambdas", "```python\nsquares = [n * n for n in range(5)]\nevens = [n for n in range(10) if n % 2 == 0]\ndouble = lambda x: x * 2\nprint(squares, evens, double(4))\n```\n**Key points**\n- Comprehensions build lists in one line\n- `lambda` makes small anonymous functions\n\n**Practice:** Build a list of the cubes of 1-5."),
]

_MORE_QZ = {
 "Python": [("What does range(3) produce?", "0, 1, 2", ["1, 2, 3", "0, 1, 2, 3", "3 only"], "range stops before the end value."),
            ("Which gives the type of x?", "type(x)", ["typeof(x)", "kind(x)", "x.type"], "Use type()."),
            ("How do you start a comment?", "#", ["//", "/*", "--"], "# begins a comment."),
            ("What is 7 // 2?", "3", ["3.5", "4", "2"], "// is floor division."),
            ("Which block always runs?", "finally", ["except", "else only", "catch"], "finally runs regardless of errors.")],
 "Java": [("Which keyword inherits a class?", "extends", ["inherits", "super", "import"], "Use `extends`."),
          ("Which is NOT a primitive type?", "String", ["int", "char", "boolean"], "String is a class."),
          ("Which keyword prevents overriding?", "final", ["static", "const", "private"], "final blocks overriding."),
          ("What does JVM stand for?", "Java Virtual Machine", ["Java Visual Method", "Joint Variable Model", "Java Version Manager"], "It runs bytecode.")],
 "C": [("Which function allocates memory dynamically?", "malloc", ["alloc", "new", "create"], "malloc is in stdlib.h."),
       ("C strings end with?", "'\\0'", ["'\\n'", "';'", "' '"], "The null terminator."),
       ("Which loop tests after the body?", "do-while", ["for", "while", "foreach"], "do-while runs at least once."),
       ("What does sizeof return?", "Size in bytes", ["Length of string", "Address", "Type name"], "It gives memory size.")],
 "JavaScript": [("Which parses JSON text?", "JSON.parse", ["JSON.stringify", "JSON.object", "parse.JSON"], "parse converts text to object."),
                ("What does typeof null return?", "object", ["null", "undefined", "number"], "A historic quirk of JS."),
                ("Which declares a constant?", "const", ["let", "var", "final"], "const can't be reassigned."),
                ("Which method filters an array?", "filter", ["select", "where", "find all"], "filter returns matching items.")],
 "HTML & CSS": [("Which attribute gives image alt text?", "alt", ["title", "src", "name"], "alt helps accessibility."),
                ("Which selector targets an id?", "#id", [".id", "*id", "@id"], "# selects ids, . selects classes."),
                ("Which tag holds visible page content?", "<body>", ["<head>", "<meta>", "<title>"], "body is the visible area."),
                ("Which property adds space inside the border?", "padding", ["margin", "gap only", "spacing"], "padding is inside, margin outside.")],
 "SQL": [("Which statement adds a row?", "INSERT", ["ADD", "APPEND", "PUT"], "INSERT INTO table ..."),
         ("Which keyword removes duplicates?", "DISTINCT", ["UNIQUE ONLY", "DEDUP", "SINGLE"], "SELECT DISTINCT col."),
         ("Which sorts descending?", "ORDER BY col DESC", ["SORT col DESC", "GROUP BY col DESC", "ARRANGE col"], "ORDER BY ... DESC."),
         ("Which statement changes existing rows?", "UPDATE", ["MODIFY", "CHANGE", "ALTER ROW"], "UPDATE ... SET ... WHERE.")],
 "Django": [("Which command applies migrations?", "python manage.py migrate", ["python manage.py apply", "django migrate", "python migrate.py"], "migrate updates the DB."),
            ("Where is Django's admin by default?", "/admin/", ["/dashboard/", "/manage/", "/root/"], "Enabled in urls.py."),
            ("Which field stores short text?", "CharField", ["TextBox", "StringType", "VarChar"], "CharField needs max_length."),
            ("Django's ORM lets you...", "Query the DB with Python", ["Style pages", "Run JS", "Host servers"], "ORM = object-relational mapper.")],
 "Flask": [("Which command runs Flask in dev?", "flask run", ["flask start", "python flask", "run flask"], "Use `flask run`."),
           ("Which object holds form data?", "request", ["response", "app", "template"], "request.form[...]"),
           ("Which engine renders Flask templates?", "Jinja2", ["Mustache", "Twig", "EJS"], "Jinja2 is Flask's default."),
           ("Which method sends JSON?", "jsonify", ["to_json", "dumps_page", "send_obj"], "jsonify returns a JSON response.")],
 "Data Analysis (Pandas)": [("Which selects column 'age'?", "df['age']", ["df.age()", "df(age)", "df->age"], "Use square brackets."),
                            ("Which gives summary statistics?", "describe()", ["summary()", "stats()", "report()"], "df.describe()."),
                            ("Which combines tables on a key?", "merge()", ["link()", "stick()", "attach()"], "pd.merge(a, b, on='id')."),
                            ("Which shows column types and nulls?", "info()", ["types()", "schema()", "meta()"], "df.info().")],
 "Git & GitHub": [("Which shows changed files?", "git status", ["git show", "git list", "git changes"], "status shows the working tree."),
                  ("Which file lists ignored paths?", ".gitignore", [".gitkeep", "ignore.txt", ".gitconfig"], "Put patterns in .gitignore."),
                  ("Which downloads and merges remote changes?", "git pull", ["git push", "git init", "git stash"], "pull = fetch + merge."),
                  ("Which shows commit history?", "git log", ["git history", "git past", "git commits"], "git log lists commits.")],
}
for _k, _v in _MORE_QZ.items():
    QUIZZES[_k] += [_mk(*t) for t in _v]

_MORE_IV = {
 "Python": [("What is a generator?", "A function using `yield` that produces values lazily, saving memory."),
            ("Explain Python's GIL.", "The Global Interpreter Lock lets only one thread run Python bytecode at a time; use multiprocessing for CPU-bound work."),
            ("What is a list comprehension?", "A compact way to build a list: `[x*x for x in range(5)]`."),
            ("Mutable vs immutable types?", "Lists, dicts, sets can change in place; ints, strings, tuples cannot.")],
 "SQL": [("What is normalization?", "Organising tables to reduce redundancy, e.g. 1NF, 2NF, 3NF."),
         ("What is an index?", "A structure that speeds up lookups at the cost of extra storage and slower writes."),
         ("DELETE vs TRUNCATE vs DROP?", "DELETE removes chosen rows; TRUNCATE empties a table; DROP removes the table itself.")],
 "Web Development": [("What is CORS?", "A browser rule controlling which origins may call your API."),
                     ("Cookies vs localStorage?", "Cookies are sent with every request; localStorage stays in the browser only.")],
 "HR": [("Describe a failure and what you learned.", "Use STAR, own the mistake, and end on the lesson and the fix."),
        ("How do you handle pressure or deadlines?", "Prioritise, break work into steps, communicate early, and give an example.")],
 "Java": [("Abstract class vs interface?", "Abstract classes can hold state and code; interfaces define contracts a class can implement many of."),
          ("What is the JVM, JRE and JDK?", "JVM runs bytecode; JRE = JVM + libraries; JDK = JRE + dev tools."),
          ("What is garbage collection?", "Automatic freeing of memory for objects that are no longer reachable.")],
 "JavaScript": [("var vs let vs const?", "var is function-scoped; let/const are block-scoped; const can't be reassigned."),
                ("What is a closure?", "A function that remembers variables from the scope where it was created."),
                ("What is the event loop?", "It runs queued callbacks and promises after the current call stack is empty.")],
 "Data Structures": [("Array vs linked list?", "Arrays give O(1) index access; linked lists give cheap inserts but O(n) access."),
                     ("Stack vs queue?", "Stack is LIFO; queue is FIFO."),
                     ("What is Big-O?", "A way to describe how runtime or memory grows with input size.")],
}
for _k, _v in _MORE_IV.items():
    INTERVIEW.setdefault(_k, []).extend(_v)

# ======================= NEW COURSES WITH PER-LESSON QUIZZES =======================
LESSON_QUIZ = {}   # (course, lesson title) -> list of quiz questions for that lesson

def add_course(name, icon, level, cat, keywords, lessons):
    COURSES[name] = {"icon": icon, "level": level, "category": cat, "keywords": keywords,
                     "lessons": [(t, x) for t, x, _ in lessons]}
    for t, _, qs in lessons:
        LESSON_QUIZ[(name, t)] = [_mk(*q) for q in qs]

add_course("Generative AI", "🤖", "Beginner", "Data & AI", "gen ai genai llm chatgpt claude gpt prompt rag ai", [
 ("What is Generative AI?", "Generative AI creates new content - text, images, code, audio - by learning patterns from huge datasets.\n\n**Examples:** Claude, ChatGPT, Gemini (text); Stable Diffusion, DALL·E (images).\n\n**Key points**\n- It generates, rather than only classifies\n- Built on large neural networks called *foundation models*",
  [("What does generative AI do?", "Creates new content", ["Only sorts data", "Only stores files", "Only classifies images"], "It generates text, images, code and more."),
   ("Foundation models are...", "Large models trained on broad data", ["Small rule-based scripts", "Databases", "Web browsers"], "They can be adapted to many tasks."),
   ("Which is an image-generation model?", "Stable Diffusion", ["MySQL", "Git", "Flask"], "Stable Diffusion generates images.")]),
 ("How LLMs Work", "Large Language Models split text into **tokens** and learn to predict the next token using a **transformer** neural network.\n\n```text\n'Career Campus is' -> predicts: 'great'\n```\n**Key points**\n- Training: learn patterns from lots of text\n- Inference: generate one token at a time\n- Context window = how much text the model can see",
  [("LLMs mainly predict...", "The next token", ["The user's mood", "Database rows", "Screen colours"], "Generation = repeated next-token prediction."),
   ("Text is split into...", "Tokens", ["Pixels", "Tables", "Packets"], "Tokens are pieces of words."),
   ("Which architecture powers most LLMs?", "Transformer", ["Decision tree", "Linked list", "Hash map"], "Transformers use attention.")]),
 ("Prompt Engineering", "A good prompt gives **role, context, task and format**.\n\n```text\nYou are a career coach. Given my resume below, suggest 3 improvements as bullet points.\n```\n**Key points**\n- Be specific and clear\n- *Few-shot*: include example inputs and outputs\n- Ask for step-by-step reasoning on hard tasks",
  [("Few-shot prompting means...", "Giving examples in the prompt", ["Training for hours", "Using fewer words", "Deleting context"], "Examples guide the output."),
   ("A good prompt should be...", "Clear and specific", ["As vague as possible", "One word only", "Random"], "Specific prompts get better answers."),
   ("Which sets the model's overall behaviour?", "System prompt", ["Browser cache", "Hostname", "File path"], "System prompts set role and rules.")]),
 ("Using LLM APIs", "Call a model from Python with an API key stored in an environment variable.\n\n```python\nimport os, anthropic\nclient = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))\nr = client.messages.create(model='claude-sonnet-5-5', max_tokens=300,\n    messages=[{'role': 'user', 'content': 'Explain RAG simply'}])\nprint(r.content[0].text)\n```\n**Key points**\n- Never hard-code API keys\n- `temperature` controls randomness; `max_tokens` limits length",
  [("Where should API keys be stored?", "Environment variables", ["In source code", "In public repos", "In HTML"], "Keep secrets out of code."),
   ("What does temperature control?", "Randomness of output", ["Server heat", "Internet speed", "File size"], "Higher = more varied."),
   ("An LLM API request usually sends...", "Messages / a prompt", ["A CSS file", "A database dump", "Only images"], "You send messages, get text back.")]),
 ("Embeddings & RAG", "An **embedding** is a vector of numbers capturing meaning; similar texts have nearby vectors.\n\n**RAG (Retrieval-Augmented Generation):** search your documents, add the best matches to the prompt, then generate.\n\n**Key points**\n- Gives the model fresh, private knowledge\n- Reduces hallucinations\n- Uses a vector database",
  [("An embedding is...", "A vector representing meaning", ["A zip file", "A font", "A password"], "Similar meaning = nearby vectors."),
   ("RAG stands for...", "Retrieval-Augmented Generation", ["Random Answer Generator", "Rapid API Gateway", "Recursive Array Grouping"], "Retrieve, then generate."),
   ("RAG helps reduce...", "Hallucinations", ["Electricity use", "Screen size", "Typing errors"], "Answers are grounded in documents.")]),
 ("Safety & Evaluation", "LLMs can be wrong or misused.\n\n**Key points**\n- *Hallucination*: confident but incorrect output\n- *Prompt injection*: malicious text that overrides instructions\n- Verify important facts and test outputs on real examples\n- Protect private data",
  [("A hallucination is...", "A confident but wrong output", ["A slow response", "A crashed server", "A saved file"], "Models can state false things fluently."),
   ("Best way to check important AI answers?", "Verify with reliable sources", ["Trust blindly", "Ask louder", "Ignore them"], "Always verify critical facts."),
   ("Prompt injection is...", "Malicious text that overrides instructions", ["A CSS bug", "A SQL index", "A GPU feature"], "Treat untrusted text carefully.")]),
])

add_course("Machine Learning", "🧠", "Intermediate", "Data & AI", "ml machine learning ai model scikit-learn sklearn prediction", [
 ("What is Machine Learning?", "ML lets computers learn patterns from data instead of following hand-written rules.\n\n```python\nfrom sklearn.linear_model import LinearRegression\nmodel = LinearRegression().fit([[1],[2],[3]], [2,4,6])\nprint(model.predict([[4]]))   # about 8\n```\n**Key points**\n- A model is a learned function from inputs to outputs",
  [("ML systems learn from...", "Data", ["Hard-coded rules only", "Screen size", "Typing speed"], "They find patterns in data."),
   ("Which library is common for ML in Python?", "scikit-learn", ["Flask", "Django", "Pillow"], "scikit-learn offers many algorithms."),
   ("A model is...", "A learned function from inputs to outputs", ["A database table", "An image file", "A web page"], "It maps features to predictions.")]),
 ("Supervised vs Unsupervised", "- **Supervised:** labelled data. *Regression* predicts numbers; *classification* predicts categories.\n- **Unsupervised:** no labels, e.g. *clustering* similar customers.\n- **Reinforcement:** learn by rewards.",
  [("Supervised learning uses...", "Labelled data", ["No data", "Only images", "Random noise"], "Each example has a known answer."),
   ("Clustering is...", "Unsupervised", ["Supervised", "Not ML", "Always regression"], "It finds groups without labels."),
   ("Predicting a house price is...", "Regression", ["Clustering", "Compression", "Sorting"], "Regression predicts numbers.")]),
 ("Data Preparation", "Good data matters more than fancy models.\n\n```python\nfrom sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n```\n**Key points**\n- Clean or fill missing values\n- Scale numeric features\n- Always keep a test set",
  [("Why split train and test sets?", "To measure performance on unseen data", ["To shrink files", "To remove columns", "To speed up the internet"], "Test data shows real performance."),
   ("Scaling features helps...", "Features contribute comparably", ["Print faster", "Hide data", "Delete rows"], "Different ranges can dominate."),
   ("Missing values are usually...", "Cleaned or imputed", ["Ignored always", "Printed", "Encrypted"], "Handle them before training.")]),
 ("Model Evaluation", "**Classification:** accuracy, precision, recall, confusion matrix.\n**Regression:** mean squared error (MSE).\n\n**Key points**\n- Accuracy can mislead on imbalanced data\n- Choose metrics that match the goal",
  [("Accuracy is...", "Correct predictions / total", ["Total / correct", "Errors only", "Training time"], "Share of correct predictions."),
   ("Which metric suits regression?", "Mean squared error", ["Accuracy", "Confusion matrix", "Recall only"], "MSE measures numeric error."),
   ("A confusion matrix shows...", "Correct vs wrong predictions per class", ["File sizes", "Memory use", "Network speed"], "It breaks down errors.")]),
 ("Overfitting & Next Steps", "**Overfitting:** the model memorises training data and fails on new data.\n\n**Fixes:** more data, simpler model, regularisation, cross-validation.\n\n**Next:** decision trees, random forests, neural networks, deep learning.",
  [("Overfitting means...", "Great on training data, poor on new data", ["Poor on training data", "Too fast", "Too small"], "The model memorised noise."),
   ("A fix for overfitting is...", "More data or regularisation", ["Fewer tests", "Bigger fonts", "Deleting labels"], "Both improve generalisation."),
   ("Cross-validation...", "Tests the model on several data splits", ["Encrypts data", "Compiles code", "Draws charts"], "It gives a steadier estimate.")]),
])
