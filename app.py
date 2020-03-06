import os
from os import path
from flask import Flask, flash, render_template, redirect, request, url_for, session
from bson.objectid import ObjectId

# Creating instance of Flask
APP = Flask(__name__)
APP.secret_key = "HackathonSecret7"


@APP.route('/')
def index():
    """ Main page where users can choose where to go"""
    return render_template('pages/index.html')


@APP.route('/carol_shaw_bio')
def cs_bio():
    """ Main page where users can choose where to go"""
    return render_template('pages/cs_bio.html')


@APP.route('/carol_shaw_work')
def cs_work():
    """ Main page where users can choose where to go"""
    return render_template('pages/cs_work.html')


@APP.route('/carol_shaw_work')
def cs_game():
    """ Main page where users can choose where to go"""
    return render_template('pages/cs_game.html')

@APP.route('/gender_equality')
def equality():
    """ Main page where users can choose where to go"""
    return render_template('pages/equality.html')

if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True) 

