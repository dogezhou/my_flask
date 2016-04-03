#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Zhou'
"""
from flask import Flask, request
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'  # 邮件服务器
app.config['MAIL_PORT'] = 25   # 端口
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '1243992216@qq.com'  #os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = 'piclhewyljorhgbb'   #os.environ.get('MAIL_PASSWORD') # qq:piclhewyljorhgbb
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <1243992216@qq.com>'
app.config['FLASKY_ADMIN'] = 'doge.zhou@outlook.com' #os.environ.get('FLASKY_ADMIN')


mail = Mail(app)


@app.route("/")
def index():
    msg = Message("Hello",
                  sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=["doge.zhou@outlook.com"])
    msg.body = "测试body"
    msg.html = "<b>测试html</b> body"
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)