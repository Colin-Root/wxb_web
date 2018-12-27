from flask import app
#from app import db
from flask_sqlalchemy import SQLAlchemy
import os
import sys
from flask import Flask
import click


# db = SQLAlchemy(app)
# WIN = sys.platform.startswith('win')
# if WIN: #如果是Windows系统，使用三个斜线
#     prefix = 'sqlite:///'
# else: #使用四个斜线
#     prefix = 'sqlite:////'

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.path.join(app.root_path,'data.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
#
# class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     name = db.Column(db.String(20))  # 名字
#
#
# class Movie(db.Model):  # 表名将会是 movie
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     title = db.Column(db.String(60))  # 电影标题
#     year = db.Column(db.String(4))  # 电影年份
#
# @app.cli.command()  # 注册为命令
# @click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
# def initdb(drop):
#     """Initialize the database."""
#     if drop:  # 判断是否输入了选项
#         db.drop_all()
#     db.create_all()
#     click.echo('Initialized database.')  # 输出提示信息
#
# @app.cli.command()
# def forge():
#     """Generate fake data."""
#     db.create_all()
#
#     # 全局的两个变量移动到这个函数内
#     name = 'Grey Li'
#     movies = [
#         {'title': 'My Neighbor Totoro', 'year': '1988'},
#         {'title': 'Dead Poets Society', 'year': '1989'},
#         {'title': 'A Perfect World', 'year': '1993'},
#         {'title': 'Leon', 'year': '1994'},
#         {'title': 'Mahjong', 'year': '1996'},
#         {'title': 'Swallowtail Butterfly', 'year': '1996'},
#         {'title': 'King of Comedy', 'year': '1999'},
#         {'title': 'Devils on the Doorstep', 'year': '1999'},
#         {'title': 'WALL-E', 'year': '2008'},
#         {'title': 'The Pork of Music', 'year': '2012'},
#     ]
#
#     user = User(name=name)
#     db.session.add(user)
#     for m in movies:
#         movie = Movie(title=m['title'], year=m['year'])
#         db.session.add(movie)
#
#     db.session.commit()
#     click.echo('Done.')
#
#
#
#
#
#
#
#
#
# class Developer(db.Model):
#     __tablename__ = 'developers'
#     id = db.Column(db.Integer, primary_key=True)
#     dev_key = db.Column(db.String(40), unique=True, index=True)
#     platform = db.Column(db.String(50))
#     platform_id = db.Column(db.String(40), unique=True)
#     username = db.Column(db.String(150), index=True)
#     integrations = db.relationship('Integration', backref='developer')
#     channels = db.relationship('Channel', backref='developer')
#
# class Integration(db.Model):
#     __tablename__ = 'integrations'
#     id = db.Column(db.Integer, primary_key=True)
#     integration_id = db.Column(db.String(40), unique=True)
#     name = db.Column(db.String(100))
#     description = db.Column(db.String(150))
#     icon = db.Column(db.String(150))
#     channel = db.Column(db.String(150))
#     token = db.Column(db.String(150))
#     developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'))
#
# class Channel(db.Model):
#     __tablename__ = 'channels'
#     id = db.Column(db.Integer, primary_key=True)
#     developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'))
#     channel = db.Column(db.String(150))
#
#     def __repr__(self):
#         return '<Channel %r>' % self.channel
#
# class User(db.model):
#     __tablename__ = 'users'
#     id = db.column(db.Integer, primary_key=True)
#     username = db.column(db.String(50), unique=True)
#     password = db.column(db.String(100))
#
#     def __repr__(self):
#         return '<User %r>'  % self.username