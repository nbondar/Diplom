from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def main():
    user = { 'login': '' }

    return render_template("main.html",
        title = 'Bullshit')


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html",
        title = 'Dashboard')

@app.route('/profile')
def Profile():
    return render_template("profile.html",
        title = 'Profile')


@app.route('/login') 
def login():
 form = LoginForm()
 if form.validate_on_submit():
        flash('Login requested for login="' + form.login.data + '", password="' + form.password.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/dashboard')
 return render_template('login.html',
    title = 'Sign In !',
    form = form,
    providers = app.config['LOGIN_PASS'])


@app.route('/Registration') 
def Register():
 form = RegisterForm()
 return render_template('register.html',
    title = 'Register!)',
    form = form)