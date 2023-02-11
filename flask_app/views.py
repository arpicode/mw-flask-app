from flask import Flask
from flask import render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt

from . import app
from .data import Articles
from .classes.RegisterForm import RegisterForm
from .classes.DataBase import DataBase


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm(request.form)
    if request.method == 'POST' and register_form.validate():
        name = str(register_form.name.data)
        email = str(register_form.email.data)
        username = str(register_form.username.data)
        password = sha256_crypt.encrypt(str(register_form.password.data))

        db = DataBase()
        db.connect()
        sql = "INSERT INTO users (name, email, username, password) VALUES(?, ?, ?, ?)"
        params = (name, email, username, password)
        db.query(sql=sql, params=params)
        db.close()

        flash('You are now registered and can log in.', 'success')
        return redirect(url_for('home'))

    return render_template('register.html.j2', form=register_form)
