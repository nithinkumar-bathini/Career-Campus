# 🎓 Career Campus

Career Campus is a Python and Streamlit-based learning platform designed to help students learn programming, practice their skills, take quizzes, prepare for interviews, and build their resumes in one place.

## 🚀 Features

### 📊 Dashboard

* Personalized student dashboard
* Shows enrolled courses
* Displays course progress
* Quiz performance tracking
* Career readiness percentage
* Recent learning activity

### 📚 Courses

Career Campus provides multiple programming and development courses, including:

* 🐍 Python
* ☕ Java
* 🔧 C
* 🟨 JavaScript
* 🌐 HTML & CSS
* 🗄️ SQL
* 🎸 Django

Each course contains lessons with:

* Course topics
* Simple explanations
* Code examples
* Lesson completion tracking
* Course progress tracking

### 📝 Quizzes

* Course-based quizzes
* Multiple-choice questions
* Automatic score calculation
* Quiz percentage
* Time tracking
* Quiz history
* Correct answer explanations
* XP rewards

### 🎯 Interview Preparation

* Interview questions organized by category
* Answer viewing option
* Practice questions
* Mark questions as known
* Interview preparation progress tracking

### 📄 Resume Builder

Students can create a resume by entering:

* Personal information
* Career summary
* Education
* Skills
* Projects
* Experience / Internships
* Certifications
* Achievements
* LinkedIn profile
* GitHub profile

The resume builder also provides different templates and allows the generated resume to be downloaded as an HTML file.

### 🏆 Progress & XP System

Career Campus tracks student learning activity and rewards XP for:

* Completing lessons
* Completing quizzes
* Enrolling in courses

This helps students monitor their learning progress and stay motivated.

## 🛠️ Technologies Used

* **Python** – Main programming language
* **Streamlit** – Web application framework
* **SQLite** – Database management
* **Pandas** – Data processing
* **Plotly** – Data visualization
* **HTML & CSS** – Resume and UI styling
* **Git & GitHub** – Version control and project hosting

## 📂 Project Structure

```text
Career-Campus/
│
├── app.py
├── requirements.txt
│
├── components/
│   ├── __init__.py
│   ├── sidebar.py
│   └── styles.py
│
├── data/
│   ├── __init__.py
│   └── content.py
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── views/
│   ├── __init__.py
│   ├── courses.py
│   ├── dashboard.py
│   └── quizzes.py
│
├── content.py
├── db.py
├── interview.py
├── resume.py
└── sidebar.py
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nithinkumar-bathini/Career-Campus.git
```

### 2. Open the Project Folder

```bash
cd Career-Campus
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

## 🗃️ Database

Career Campus uses **SQLite** to store student-related information such as:

* User accounts
* Enrolled courses
* Lesson progress
* Quiz results
* Learning activity
* XP points

The database is created automatically when the application runs.

## 🔐 User Authentication

The application provides:

* User registration
* User login
* Password protection
* Password hashing
* Individual student progress tracking

Each student's course progress and quiz history are stored separately.

## 📈 Learning Flow

The basic learning flow of Career Campus is:

```text
Register / Login
       ↓
   Dashboard
       ↓
     Courses
       ↓
   Select Course
       ↓
     Lessons
       ↓
 Mark Lesson Complete
       ↓
      Quizzes
       ↓
 Track Progress & XP
       ↓
 Interview Preparation
       ↓
   Resume Builder
```

## 🎯 Project Objective

The main objective of Career Campus is to provide students with a simple and user-friendly platform for learning technical skills and preparing for their careers.

Instead of using separate platforms for learning, quizzes, interview preparation, and resume creation, Career Campus brings these features together in a single application.

## 🔮 Future Enhancements

The project can be further improved by adding:

* 🤖 AI-powered mock interviews
* 💻 Coding practice problems
* 🧪 Online coding compiler
* 🏅 Course completion certificates
* 📊 Advanced student analytics
* 🎯 Personalized learning recommendations
* 💼 Job and internship recommendations
* 🤖 AI-powered resume suggestions
* 🌐 Deployment as an online web application
* 📱 Improved responsive design

## 📌 Note About `.venv`

The `.venv` virtual environment is **not included in this GitHub repository** because it contains locally installed Python packages and can contain many files.

It is recommended to create a new virtual environment after cloning the project and install the required packages using:

```bash
pip install -r requirements.txt
```

## 👨‍💻 Project

**Project Name:** Career Campus
**Technology:** Python, Streamlit
**Database:** SQLite
**Purpose:** Student Learning and Career Preparation Platform

## 📜 License

This project is developed for educational purposes.
