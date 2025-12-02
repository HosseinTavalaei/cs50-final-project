from src import app
from flask import render_template, url_for, flash, redirect
from src.forms import RegistrationForm, LoginForm


# @app.route('/')
# def home():
#     form = RegistrationForm()
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'The user created for {form.email.data}!', 'success')
        # return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
