#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Zhou'
"""
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return "<h1>Hello World!</h1>" \
           "<p>Your browser is %s</p>" % user_agent


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

if __name__ == '__main__':
    app.run(debug=True)


