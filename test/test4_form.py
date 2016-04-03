#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Zhou'
"""
from datetime import datetime
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',
                                current_time=datetime.utcnow())
    elif request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        return ('<h1>欢迎%s</h1>' % name).decode()


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)