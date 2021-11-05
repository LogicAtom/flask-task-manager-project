""" import the os """
import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return render_template('index.html', name='Jerry')


@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)


@app.route('/books/<genre>/')
def books(genre):
    return "All Books in {} category".format(genre)


if __name__ == "__main__":
    manager.run()
