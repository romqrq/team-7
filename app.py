import os
from os import path
from flask import Flask, flash, render_template, redirect, request, url_for, session
from bson.objectid import ObjectId

# Creating instance of Flask
APP = Flask(__name__)
APP.secret_key = "HackathonSecret7"


@APP.route('/')
def user_home():
    """ Main page where users can choose where to go"""
    return render_template('pages/index.html')


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)