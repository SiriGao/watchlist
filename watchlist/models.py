# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from watchlist import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

'''
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
'''
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 注意这里使用了 String
    title = db.Column(db.String(60))  # 调整为与数据库中的列名匹配
    release_date = db.Column(db.DateTime)  # 新增
    country = db.Column(db.String(20))  # 新增
    genre = db.Column(db.String(10))  # 新增
    year = db.Column(db.Integer)  # 更新为 Integer 类型

class MovieBox(db.Model):
    movie_id = db.Column(db.String(10), db.ForeignKey('movie.id'), primary_key=True)
    box = db.Column(db.Float)
    # 建立与 Movie 模型的关系
    movie = db.relationship('Movie', backref=db.backref('box_info', uselist=False))


class Actor(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(2), nullable=False)
    country = db.Column(db.String(20))

class MovieActorRelation(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    movie_id = db.Column(db.String(10), db.ForeignKey('movie.id'), nullable=False)
    actor_id = db.Column(db.String(10), db.ForeignKey('actor.id'), nullable=False)
    relation_type = db.Column(db.String(20))

    movie = db.relationship('Movie', backref=db.backref('relations', lazy=True))
    actor = db.relationship('Actor', backref=db.backref('relations', lazy=True))

from flask import Flask
from watchlist import app

@app.template_filter('to_date_string')
def to_date_string(value):
    return value.strftime('%Y-%m-%d') if value else ''


