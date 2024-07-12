from flask import Flask, flash,render_template, url_for, redirect
from pblog.forms import RegistrationForm, LoginForm
from pblog.models import User, Post
from pblog import app

posts = [
    {
        'author': 'Jayesh Suthar',
        'title': 'My first Blog Post😎',
        'content': 'First post content',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Krishna Suthar',
        'title': 'Micro-bio👾',
        'content': 'A lot of Micro-biology is going around us but we have to take look closer to see it!',
        'date_posted': 'April 21, 2024'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
