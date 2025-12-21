
# Todo App 
### Video Demo : https://youtu.be/n4ux5Ee4np4?si=uZXihAmjVf1Wxs0Y

#### Description :
This project is a simple Todo application built to help users manage their daily tasks efficiently. The application allows users to create an account, log in, and manage their own personal todo list.

Each user can add new tasks, mark them as completed or important, and delete tasks when they are no longer needed. All todos are user-specific, meaning each user can only see and manage their own tasks.


## Features

- User registration and login with email and password
- Add, view, and manage personal todos
- Mark todos as completed or important
- View todos filtered by Important or Completed
- Delete todos
- User profile page
- Logout functionality


## Tech Stack

- Python 3.13
- Flask
- Flask-WTF (Forms)
- Flask-Session
- SQLAlchemy
- SQLite
- Bootstrap 5
- Jinja2 Templates


## Installation

Install my-project with npm

```bash
  git clone https://github.com/HosseinTavalaei/cs50-final-project.git
```
    
## Running the App

1 - Initialize the database (if needed):

```bash
  from src import db
  db.create_all()
```

2 - Run the Flask app:

```bash
  flask run
```
3 - Open your browser at:

```bash
http://127.0.0.1:5000
```
## Usage
- Register a new user with firstname, lastname, email, and password

- Login using email and password

- Add todos in the Tasks page

- Mark todos as completed or important using the buttons

- View filtered todos in Important or Completed pages
 
- Delete todos if needed
 
- Logout to end the session
## Notes

- Passwords are hashed using Werkzeug security

- User sessions are stored securely using Flask-Session
 
- Only the owner of a todo can modify or delete it
 
- Sidebar automatically highlights the active page