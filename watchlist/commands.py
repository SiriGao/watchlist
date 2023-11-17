# -*- coding: utf-8 -*-
import datetime
import click

from watchlist import app, db
from watchlist.models import MovieBox, User, Movie, Actor, MovieActorRelation


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

    name = 'Siri Gao'

    movies = [
    {'id': '1001', 'title': '战狼2', 'release_date': datetime.datetime(2017, 7, 27), 'country': '中国', 'genre': '战争', 'year': 2017},
    {'id': '1002', 'title': '哪吒之魔童降世', 'release_date': datetime.datetime(2019, 7, 26), 'country': '中国', 'genre': '动画', 'year': 2019},
    {'id': '1003', 'title': '流浪地球', 'release_date': datetime.datetime(2019, 2, 5), 'country': '中国', 'genre': '科幻', 'year': 2019},
    {'id': '1004', 'title': '复仇者联盟4', 'release_date': datetime.datetime(2019, 4, 24), 'country': '美国', 'genre': '科幻', 'year': 2019},
    {'id': '1005', 'title': '红海行动', 'release_date': datetime.datetime(2018, 2, 16), 'country': '中国', 'genre': '战争', 'year': 2018},
    {'id': '1006', 'title': '唐人街探案2', 'release_date': datetime.datetime(2018, 2, 16), 'country': '中国', 'genre': '喜剧', 'year': 2018},
    {'id': '1007', 'title': '我不是药神', 'release_date': datetime.datetime(2018, 7, 5), 'country': '中国', 'genre': '喜剧', 'year': 2018},
    {'id': '1008', 'title': '中国机长', 'release_date': datetime.datetime(2019, 9, 30), 'country': '中国', 'genre': '剧情', 'year': 2019},
    {'id': '1009', 'title': '速度与激情8', 'release_date': datetime.datetime(2017, 4, 14), 'country': '美国', 'genre': '动作', 'year': 2017},
    {'id': '1010', 'title': '西虹市首富', 'release_date': datetime.datetime(2018, 7, 27), 'country': '中国', 'genre': '喜剧', 'year': 2018},
    {'id': '1011', 'title': '复仇者联盟3', 'release_date': datetime.datetime(2018, 5, 11), 'country': '美国', 'genre': '科幻', 'year': 2018},
    {'id': '1012', 'title': '捉妖记2', 'release_date': datetime.datetime(2018, 2, 16), 'country': '中国', 'genre': '喜剧', 'year': 2018},
    {'id': '1013', 'title': '八佰', 'release_date': datetime.datetime(2020, 8, 21), 'country': '中国', 'genre': '战争', 'year': 2020},
    {'id': '1014', 'title': '姜子牙', 'release_date': datetime.datetime(2020, 10, 1), 'country': '中国', 'genre': '动画', 'year': 2020},
    {'id': '1015', 'title': '我和我的家乡', 'release_date': datetime.datetime(2020, 10, 1), 'country': '中国', 'genre': '剧情', 'year': 2020},
    {'id': '1016', 'title': '你好，李焕英', 'release_date': datetime.datetime(2021, 2, 12), 'country': '中国', 'genre': '喜剧', 'year': 2021},
    {'id': '1017', 'title': '长津湖', 'release_date': datetime.datetime(2021, 9, 30), 'country': '中国', 'genre': '战争', 'year': 2021},
    {'id': '1018', 'title': '速度与激情9', 'release_date': datetime.datetime(2021, 5, 21), 'country': '中国', 'genre': '动作', 'year': 2021}
]

    
    actors = [
    {'id': '2001', 'name': '吴京', 'gender': '男', 'country': '中国'},
    {'id': '2002', 'name': '饺子', 'gender': '男', 'country': '中国'},
    {'id': '2003', 'name': '屈楚萧', 'gender': '男', 'country': '中国'},
    {'id': '2004', 'name': '郭帆', 'gender': '男', 'country': '中国'},
    {'id': '2005', 'name': '乔罗素', 'gender': '男', 'country': '美国'},
    {'id': '2006', 'name': '小罗伯特·唐尼', 'gender': '男', 'country': '美国'},
    {'id': '2007', 'name': '克里斯·埃文斯', 'gender': '男', 'country': '美国'},
    {'id': '2008', 'name': '林超贤', 'gender': '男', 'country': '中国'},
    {'id': '2009', 'name': '张译', 'gender': '男', 'country': '中国'},
    {'id': '2010', 'name': '黄景瑜', 'gender': '男', 'country': '中国'},
    {'id': '2011', 'name': '陈思诚', 'gender': '男', 'country': '中国'},
    {'id': '2012', 'name': '王宝强', 'gender': '男', 'country': '中国'},
    {'id': '2013', 'name': '刘昊然', 'gender': '男', 'country': '中国'},
    {'id': '2014', 'name': '文牧野', 'gender': '男', 'country': '中国'},
    {'id': '2015', 'name': '徐峥', 'gender': '男', 'country': '中国'},
    {'id': '2016', 'name': '刘伟强', 'gender': '男', 'country': '中国'},
    {'id': '2017', 'name': '张涵予', 'gender': '男', 'country': '中国'},
    {'id': '2018', 'name': 'F·加里·格雷', 'gender': '男', 'country': '美国'},
    {'id': '2019', 'name': '范·迪塞尔', 'gender': '男', 'country': '美国'},
    {'id': '2020', 'name': '杰森·斯坦森', 'gender': '男', 'country': '美国'},
    {'id': '2021', 'name': '闫非', 'gender': '男', 'country': '中国'},
    {'id': '2022', 'name': '沈腾', 'gender': '男', 'country': '中国'},
    {'id': '2023', 'name': '安东尼·罗素', 'gender': '男', 'country': '美国'},
    {'id': '2024', 'name': '克里斯·海姆斯沃斯', 'gender': '男', 'country': '美国'},
    {'id': '2025', 'name': '许诚毅', 'gender': '男', 'country': '中国'},
    {'id': '2026', 'name': '梁朝伟', 'gender': '男', 'country': '中国'},
    {'id': '2027', 'name': '白百何', 'gender': '女', 'country': '中国'},
    {'id': '2028', 'name': '井柏然', 'gender': '男', 'country': '中国'},
    {'id': '2029', 'name': '管虎', 'gender': '男', 'country': '中国'},
    {'id': '2030', 'name': '王千源', 'gender': '男', 'country': '中国'},
    {'id': '2031', 'name': '姜武', 'gender': '男', 'country': '中国'},
    {'id': '2032', 'name': '宁浩', 'gender': '男', 'country': '中国'},
    {'id': '2033', 'name': '葛优', 'gender': '男', 'country': '中国'},
    {'id': '2034', 'name': '范伟', 'gender': '男', 'country': '中国'},
    {'id': '2035', 'name': '贾玲', 'gender': '女', 'country': '中国'},
    {'id': '2036', 'name': '张小斐', 'gender': '女', 'country': '中国'},
    {'id': '2037', 'name': '陈凯歌', 'gender': '男', 'country': '中国'},
    {'id': '2038', 'name': '徐克', 'gender': '男', 'country': '中国'},
    {'id': '2039', 'name': '易烊千玺', 'gender': '男', 'country': '中国'},
    {'id': '2040', 'name': '林诣彬', 'gender': '男', 'country': '美国'},
    {'id': '2041', 'name': '米歇尔·罗德里格兹', 'gender': '女', 'country': '美国'}
]

    relations = [
    {'id': '1', 'movie_id': '1001', 'actor_id': '2001', 'relation_type': '主演'},
    {'id': '10', 'movie_id': '1005', 'actor_id': '2008', 'relation_type': '导演'},
    {'id': '11', 'movie_id': '1005', 'actor_id': '2009', 'relation_type': '主演'},
    {'id': '12', 'movie_id': '1005', 'actor_id': '2010', 'relation_type': '主演'},
    {'id': '13', 'movie_id': '1006', 'actor_id': '2011', 'relation_type': '导演'},
    {'id': '14', 'movie_id': '1006', 'actor_id': '2012', 'relation_type': '主演'},
    {'id': '15', 'movie_id': '1006', 'actor_id': '2013', 'relation_type': '主演'},
    {'id': '16', 'movie_id': '1007', 'actor_id': '2014', 'relation_type': '导演'},
    {'id': '17', 'movie_id': '1007', 'actor_id': '2015', 'relation_type': '主演'},
    {'id': '18', 'movie_id': '1008', 'actor_id': '2016', 'relation_type': '导演'},
    {'id': '19', 'movie_id': '1008', 'actor_id': '2017', 'relation_type': '主演'},
    {'id': '2', 'movie_id': '1001', 'actor_id': '2001', 'relation_type': '导演'},
    {'id': '20', 'movie_id': '1009', 'actor_id': '2018', 'relation_type': '导演'},
    {'id': '21', 'movie_id': '1009', 'actor_id': '2019', 'relation_type': '主演'},
    {'id': '22', 'movie_id': '1009', 'actor_id': '2020', 'relation_type': '主演'},
    {'id': '23', 'movie_id': '1010', 'actor_id': '2021', 'relation_type': '导演'},
    {'id': '24', 'movie_id': '1010', 'actor_id': '2022', 'relation_type': '主演'},
    {'id': '25', 'movie_id': '1011', 'actor_id': '2023', 'relation_type': '导演'},
    {'id': '26', 'movie_id': '1011', 'actor_id': '2006', 'relation_type': '主演'},
    {'id': '27', 'movie_id': '1011', 'actor_id': '2024', 'relation_type': '主演'},
    {'id': '28', 'movie_id': '1012', 'actor_id': '2025', 'relation_type': '导演'},
    {'id': '29', 'movie_id': '1012', 'actor_id': '2026', 'relation_type': '主演'},
    {'id': '3', 'movie_id': '1002', 'actor_id': '2002', 'relation_type': '导演'},
    {'id': '30', 'movie_id': '1012', 'actor_id': '2027', 'relation_type': '主演'},
    {'id': '31', 'movie_id': '1012', 'actor_id': '2028', 'relation_type': '主演'},
    {'id': '32', 'movie_id': '1013', 'actor_id': '2029', 'relation_type': '导演'},
    {'id': '33', 'movie_id': '1013', 'actor_id': '2030', 'relation_type': '主演'},
    {'id': '34', 'movie_id': '1013', 'actor_id': '2009', 'relation_type': '主演'},
    {'id': '35', 'movie_id': '1013', 'actor_id': '2031', 'relation_type': '主演'},
    {'id': '36', 'movie_id': '1015', 'actor_id': '2032', 'relation_type': '导演'},
    {'id': '37', 'movie_id': '1015', 'actor_id': '2015', 'relation_type': '导演'},
    {'id': '38', 'movie_id': '1015', 'actor_id': '2011', 'relation_type': '导演'},
    {'id': '39', 'movie_id': '1015', 'actor_id': '2015', 'relation_type': '主演'},
    {'id': '4', 'movie_id': '1003', 'actor_id': '2001', 'relation_type': '主演'},
    {'id': '40', 'movie_id': '1015', 'actor_id': '2033', 'relation_type': '主演'},
    {'id': '41', 'movie_id': '1015', 'actor_id': '2034', 'relation_type': '主演'},
    {'id': '42', 'movie_id': '1016', 'actor_id': '2035', 'relation_type': '导演'},
    {'id': '43', 'movie_id': '1016', 'actor_id': '2035', 'relation_type': '主演'},
    {'id': '44', 'movie_id': '1016', 'actor_id': '2036', 'relation_type': '主演'},
    {'id': '45', 'movie_id': '1016', 'actor_id': '2022', 'relation_type': '主演'},
    {'id': '46', 'movie_id': '1017', 'actor_id': '2037', 'relation_type': '导演'},
    {'id': '47', 'movie_id': '1017', 'actor_id': '2038', 'relation_type': '导演'},
    {'id': '48', 'movie_id': '1017', 'actor_id': '2008', 'relation_type': '导演'},
    {'id': '49', 'movie_id': '1017', 'actor_id': '2001', 'relation_type': '主演'},
    {'id': '5', 'movie_id': '1003', 'actor_id': '2003', 'relation_type': '主演'},
    {'id': '50', 'movie_id': '1017', 'actor_id': '2039', 'relation_type': '主演'},
    {'id': '51', 'movie_id': '1018', 'actor_id': '2040', 'relation_type': '导演'},
    {'id': '52', 'movie_id': '1018', 'actor_id': '2019', 'relation_type': '主演'},
    {'id': '53', 'movie_id': '1018', 'actor_id': '2041', 'relation_type': '主演'},
    {'id': '6', 'movie_id': '1003', 'actor_id': '2004', 'relation_type': '导演'},
    {'id': '7', 'movie_id': '1004', 'actor_id': '2005', 'relation_type': '导演'},
    {'id': '8', 'movie_id': '1004', 'actor_id': '2006', 'relation_type': '主演'},
    {'id': '9', 'movie_id': '1004', 'actor_id': '2007', 'relation_type': '主演'}
]

    
    box_data = [
        {'movie_id': '1001', 'box': 56.84},
        {'movie_id': '1002', 'box': 50.15},
        {'movie_id': '1003', 'box': 46.86},
        {'movie_id': '1004', 'box': 42.5},
        {'movie_id': '1005', 'box': 36.5},
        {'movie_id': '1006', 'box': 33.97},
        {'movie_id': '1007', 'box': 31},
        {'movie_id': '1008', 'box': 29.12},
        {'movie_id': '1009', 'box': 26.7},
        {'movie_id': '1010', 'box': 25.47},
        {'movie_id': '1011', 'box': 23.9},
        {'movie_id': '1012', 'box': 22.37},
        {'movie_id': '1013', 'box': 30.1},
        {'movie_id': '1014', 'box': 16.02},
        {'movie_id': '1015', 'box': 28.29},
        {'movie_id': '1016', 'box': 54.13},
        {'movie_id': '1017', 'box': 53.48},
        {'movie_id': '1018', 'box': 13.92},
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

    # 添加票房数据
    for b in box_data:
        box = MovieBox(movie_id=b['movie_id'], box=b['box'])
        db.session.add(box)

    

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