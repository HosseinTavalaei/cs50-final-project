
# Todo App 
### Video Demo : https://youtu.be/n4ux5Ee4np4?si=uZXihAmjVf1Wxs0Y

#### Description :
This project is a simple yet functional Todo application designed to help users organize and manage their daily tasks in an efficient and user-friendly way. The application focuses on providing essential task management features while maintaining a clean and easy-to-use interface.

The application starts with a Login page, where users can authenticate using their registered credentials. If a user does not already have an account, they can navigate to the Sign Up page to create a new one. After successful registration, the user is redirected back to the login page to sign in. This authentication system ensures that each user has a secure and private workspace.

Once logged in, users gain access to their personal todo dashboard. On this page, users can create new todo tasks, which are stored in the database and associated only with the currently logged-in user. This means that each user can only view, edit, or delete their own tasks, ensuring data privacy and separation between users.

Users can manage their tasks by marking them as completed once they are finished, or marking them as important to highlight high-priority tasks. The application provides dedicated sections for Completed Tasks and Important Tasks, making it easy for users to filter and review their tasks based on their status.

Additionally, users can delete tasks that are no longer needed, keeping their task list clean and organized. A Logout feature is also included, allowing users to securely exit the application and return to the login page.

This project is built using HTML, CSS, and Bootstrap for the frontend to ensure a responsive and visually clean user interface. The backend is developed using Python and Flask, handling routing, authentication, and business logic. SQLite is used as the database to store user information and todo data in a lightweight and efficient manner.

Overall, this project demonstrates fundamental concepts of web development such as user authentication, CRUD operations, session management, and database integration using Flask.


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