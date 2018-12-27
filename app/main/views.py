# -*- coding: utf-8 -*-
#import uuid

from flask import render_template, flash
#from .forms import UserForm
#from ..models import User
#from app import db

#导入蓝本 main
#from . import main

# @main.route('/')
# def index():
#     return render_template('index.html')

#@main.route('/', methods=['GET', 'POST'])
# def signin():
#     form = UserForm()
#     if form is None:
#         flash('Should input username and password')
#     elif  form.validate_on_submit():
#         user = User(username=form.username.data, password=form.password.data)
#         db.session.add(user)
#         try:
#             db.session.commit()
#             flash('User created !')
#         except:
#             db.session.rollback()
#             flash('User create failed')
#     return render_template('index.html', form=form)