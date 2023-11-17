# -*- coding: utf-8 -*-
import datetime
import click

from watchlist import app, db
from watchlist.models import User, Movie, Actor, MovieActorRelation


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    name = 'Grey Li'

    movies=[
        {'id': '1001', 'title': '战狼2', 'release_date': datetime.datetime(2017, 7, 27), 'country': '中国', 'genre': '战争', 'year': 2017},
    ]
    actors=[
        {'id': '2001', 'name': '吴京', 'gender': '男', 'country': '中国'},
    ]
    relations=[
        {'id': '1', 'movie_id': '1001', 'actor_id': '2001', 'relation_type': '主演'}
    ]

    user = User(name=name)
    db.session.add(user)
    # 创建电影实例
    for m in movies:
        movie = Movie(id=m['id'], title=m['title'], release_date=m['release_date'], country=m['country'], genre=m['genre'], year=m['year'])
        db.session.add(movie)

    # 创建演员实例
    for a in actors:
        actor = Actor(id=a['id'], name=a['name'], gender=a['gender'], country=a['country'])
        db.session.add(actor)

    # 创建电影演员关系实例
    for r in relations:
        relation = MovieActorRelation(id=r['id'], movie_id=r['movie_id'], actor_id=r['actor_id'], relation_type=r['relation_type'])
        db.session.add(relation)

    db.session.commit()
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')