#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Zhou'
"""
from app.models import Permission
from flask import Blueprint

main = Blueprint('main', __name__)

# 避免循环导入依赖，放到末尾
from . import views, errors


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)