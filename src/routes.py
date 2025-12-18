from flask import Blueprint, render_template, redirect, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
from src.models import User, Todo
from src.forms import RegistrationForm, LoginForm, TodoForm


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    if 'user_id' not in session:
        return redirect('/login')

    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(
            title=form.title.data,
            user_id=session['user_id']
        )
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todos = Todo.query.filter_by(user_id=session['user_id']).all()
    return render_template('tasks.html', form=form, todos=todos)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html', form=form)



@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            return redirect('/')
    return render_template('login.html', form=form)


@main.route('/complete/<int:id>')
def complete(id):
    todo = Todo.query.get_or_404(id)
    todo.is_completed = not todo.is_completed
    db.session.commit()
    return redirect('/')


@main.route('/important/<int:id>')
def important(id):
    todo = Todo.query.get_or_404(id)
    todo.is_important = not todo.is_important
    db.session.commit()
    return redirect('/')


@main.route('/important')
def important_todos():
    todos = Todo.query.filter_by(
        user_id=session['user_id'],
        is_important=True
    ).all()
    return render_template('important.html', todos=todos)


@main.route('/completed')
def completed_todos():
    todos = Todo.query.filter_by(
        user_id=session['user_id'],
        is_completed=True
    ).all()
    return render_template('completed.html', todos=todos)


@main.route('/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    if 'user_id' not in session:
        return redirect('/login')

    todo = Todo.query.get_or_404(id)

    if todo.user_id != session['user_id']:
        return redirect('/')

    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@main.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/login')

    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)

@main.route('/logout')
def logout():
    session.clear()  
    return redirect('/login')
