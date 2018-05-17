from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from backend.search import Basic
import json

#/home/hishamsajid/Documents/FlaskFront/backend

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index2.html', title='Home', user=user, posts=posts)

@app.route('/search')
def search():
	return render_template('search.html', title='Search')

@app.route('/login', methods =['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  

        return redirect(url_for('search'))
        
    return render_template('login.html', title = 'Sign In', form=form)
