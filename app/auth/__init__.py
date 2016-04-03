#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Zhou'
"""
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views