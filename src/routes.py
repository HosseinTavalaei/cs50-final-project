from src import app
from src.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect


@app.route('/')
@app.route('/tasks')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        flash(f'The user created for {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        if form.email.data == 'example@gmail.com' and form.password.data == '123456':
            flash('you have been logged in !', 'success')
            return redirect(url_for('home'))
        else:
            flash('invalid username or password', 'danger')
    return render_template('login.html', title='Login', form=form)
