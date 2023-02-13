from flask import Flask
from flask import render_template, flash, redirect, url_for, session, request, logging
from functools import wraps
from passlib.hash import sha256_crypt

from . import app
from .data import Articles
from .classes.RegisterForm import RegisterForm
from .classes.DataBase import DataBase
from flask_app.classes.models.User import User


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please log in.', 'danger')
            return redirect(url_for('login'))
    return wrap


@app.route("/")
def home() -> str:
    return render_template('home.html.j2')


@app.route("/about")
def about() -> str:
    return render_template('about.html.j2')


@app.route('/articles')
def articles() -> str:
    return render_template('articles.html.j2', articles=Articles())


@app.route('/articles/<string:id>')
def article(id) -> str:
    return render_template('article.html.j2', id=id)


@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html.j2')


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm(request.form)
    if request.method == 'POST' and register_form.validate():
        User.insert_user(form=register_form)
        flash('You are now registered and can login.', 'success')
        return redirect(url_for('home'))

    return render_template('register.html.j2', form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # testing without using wtforms
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = User.get_user_by_username(username=username)

        if result != None and sha256_crypt.verify(password, result['password']):
            user = result['username']
            session['logged_in'] = True
            session['username'] = user
            flash(f'You are now logged in as {user}.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Bad credentials.', 'danger')

    return render_template('login.html.j2')


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out.', 'success')
    return redirect(url_for('login'))
