CS50 Todo App

A multi-user Todo Web Application built with Flask, SQLite, and Bootstrap for CS50 final project.

Manage your tasks efficiently with important and completed status, user authentication, and a clean responsive UI.

🔹 Features

User registration and login with email and password

Add, view, and manage personal todos

Mark todos as completed or important

View todos filtered by Important or Completed

Delete todos

User profile page

Logout functionality


🔹 Technologies Used

Python 3.13

Flask

Flask-WTF (Forms)

Flask-Session

SQLAlchemy

SQLite

Bootstrap 5

Jinja2 Templates

🔹 Project Structure

project/
├─ src/
│  ├─ templates/       # HTML templates
│  │  ├─ index.html
│  │  ├─ tasks.html
│  │  ├─ important.html
│  │  ├─ completed.html
│  │  ├─ register.html
│  │  ├─ login.html
│  │  ├─ profile.html
│  ├─ static/          # CSS, JS, images
│  │  ├─ styles/
│  │  └─ js/
│  ├─ __init__.py      # Flask app factory
│  ├─ routes.py        # Blueprint routes
│  └─ forms.py         # WTForms
├─ app.py              # Entry point
├─ todo.db             # SQLite database
├─ requirements.txt    # Python dependencies
└─ README.md           # This file

🔹 Installation

1 - Clone the repository:
git clone https://github.com/yourusername/cs50-todo.git
cd cs50-todo
