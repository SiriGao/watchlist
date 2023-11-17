# -*- coding: utf-8 -*-
import click

from watchlist import app, db
from watchlist.models import User, Movie


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
    movies = [
        {'title': '战狼2', 'year': '2017'},
        {'title': '哪吒之魔童降世', 'year': '2019'},
        {'title': '流浪地球', 'year': '2019'},
        {'title': '复仇者联盟4', 'year': '2019'},
        {'title': '红海行动', 'year': '2018'},
        {'title': '唐人街探案2', 'year': '2018'},
        {'title': '我不是药神', 'year': '2018'},
        {'title': '中国机长', 'year': '2019'},
        {'title': '速度与激情8', 'year': '2017'},
        {'title': '西虹市首富', 'year': '2018'},
        {'title': '速度与激情9', 'year': '2021'},
        {'title': '长津湖', 'year': '2021'},
        {'title': '你好，李焕英', 'year': '2021'},
        {'title': '我和我的家乡', 'year': '2020'},
        {'title': '姜子牙', 'year': '2020'},
        {'title': '八佰', 'year': '2020'},
        {'title': '捉妖记2', 'year': '2018'},
        {'title': '复仇者联盟3', 'year': '2018'},
        
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

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