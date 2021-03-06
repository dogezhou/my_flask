#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Zhou'
"""
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import os
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app.models import User, Role, Post, Comment, Vote, Tag, TagBelong

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post, Comment=Comment, Vote=Vote, Tag=Tag, TagBelong=TagBelong)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
