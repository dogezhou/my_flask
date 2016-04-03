#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Zhou'
"""

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('<h1>这个文档携带cookie！</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
