from cs50 import SQL
from flask import Flask
from flask_session import Session


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = '5d4b4a1acdf7c0e4b22f47cef267c9be'

Session(app)

db = SQL("sqlite:///todo.db")