from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ben'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Sydney'
        },
        {
            'author': {'username': 'Lauren'},
            'body': 'The avengers movie was so cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    # return render_template('index.html', user=user, posts=posts)