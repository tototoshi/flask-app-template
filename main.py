# coding: utf-8
import os
from flask import Flask
from flask import request
from flask import render_template
from flask import g
from flask import redirect
from flask import flash
from flask import url_for
from sqlalchemy import create_engine

app = Flask(__name__)

@app.before_request
def connect_db():
#    g.db = create_engine("postgresql://ocalhost/yourdb")
    pass

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.config.update({'DEBUG': True })
    app.run(use_reloader=False)
