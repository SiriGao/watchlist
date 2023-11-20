# -*- coding: utf-8 -*-
import datetime
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user

from watchlist import app, db
from watchlist.models import Actor, MovieActorRelation, MovieBox, User, Movie


from flask import request, url_for, redirect, flash


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        title = request.form.get('title')  # 传入表单对应输入字段的 name 值
        #year = request.form.get('year')
        release_date = request.form.get('release_date')
        country = request.form.get('country')
        genre = request.form.get('genre')

        # 验证数据
        if not title or len(title) > 60:
            flash('Invalid Input.')  # 显示错误提示
            return redirect(url_for('index'))  # 重定向回主页
        
        try:
            release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d').date()
            year = release_date.year  # 从 release_date 提取年份
        except ValueError:
            flash('Invalid release date format.')
            return redirect(url_for('index'))
        
        # 保存表单数据到数据库
        movie = Movie(title=title, year=year, release_date=release_date, country=country, genre=genre) # 创建记录
        db.session.add(movie)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('Movie added.')  # 显示成功创建的提示
        return redirect(url_for('index'))  # 重定向回主页
    
    
    # 获取搜索和筛选参数
    search_query = request.args.get('search', '')
    filter_country = request.args.get('country')
    filter_genre = request.args.get('genre')
    filter_year = request.args.get('year')

    # 构建基础查询
    query = Movie.query

    # 应用搜索条件  # 应用筛选条件
    if search_query:
        query = query.filter(Movie.title.contains(search_query))
    if filter_country:
            query = query.filter(Movie.country == filter_country)
    if filter_genre:
            query = query.filter(Movie.genre == filter_genre)
    if filter_year:
            query = query.filter(Movie.year == filter_year)
    

    movies = query.all()

    return render_template('index.html', movies=movies)
    

@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == 'POST':
        title = request.form['title']
        #year = request.form['year']
        release_date = request.form.get('release_date')
        country = request.form.get('country')
        genre = request.form.get('genre')

        if not title  or  len(title) > 60:
            flash('Invalid Input.')
            return redirect(url_for('edit', movie_id=movie_id))
        
        try:
            # 将字符串转换为日期对象，并从中提取年份
            release_date_obj = datetime.datetime.strptime(release_date, '%Y-%m-%d').date()
            year = release_date_obj.year
        except ValueError:
            flash('Invalid release date format.')
            return redirect(url_for('edit', movie_id=movie_id))
        
        
        # 更新电影信息
        movie.title = title
        movie.release_date = release_date_obj
        movie.year = str(year)  # 更新年份字段
        movie.country = country
        movie.genre = genre


        db.session.commit()
        flash('Movie updated.')
        return redirect(url_for('index'))

    return render_template('edit.html', movie=movie)


@app.route('/movie/delete/<int:movie_id>', methods=['POST'])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 20:
            flash('Invalid input.')
            return redirect(url_for('settings'))

        user = User.query.first()
        user.name = name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('index'))

    return render_template('settings.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()

        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('index'))

        flash('Invalid username or password.')
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('index'))


@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    actors = MovieActorRelation.query.filter_by(movie_id=movie_id).join(Actor, MovieActorRelation.actor_id == Actor.id).all()
    box_office = MovieBox.query.filter_by(movie_id=movie_id).first()

    return render_template('movie_detail.html', movie=movie, actors=actors, box_office=box_office)

# @app.route('/movies_with_box_office')
# def movies_with_box_office():
#     # 假设 MovieBox 模型包含对 Movie 的引用
#     movies = Movie.query.all()
#     movies_box_office = {movie.id: MovieBox.query.filter_by(movie_id=movie.id).first() for movie in movies}

#     return render_template('movies_with_box_office.html', movies=movies, movies_box_office=movies_box_office)

@app.route('/movies_with_box_office')
def movies_with_box_office():
    movies = Movie.query.all()
    movie_data = [
        {
            "title": movie.title,
            "box_office": MovieBox.query.filter_by(movie_id=movie.id).first().box if MovieBox.query.filter_by(movie_id=movie.id).first() else 0
        }
        for movie in movies
    ]

    # 按票房从高到低排序
    movie_data.sort(key=lambda x: x['box_office'], reverse=True)

    return render_template('movies_with_box_office.html', movie_data=movie_data)


@app.route('/actors')
def actors():
    actors = Actor.query.all()
    return render_template('actors.html', actors=actors)


@app.route('/movie_boxes')
def movie_boxes():
    movies = Movie.query.all()
    movie_boxes = {movie.id: MovieBox.query.filter_by(movie_id=movie.id).first() for movie in movies}

    return render_template('movie_boxes.html', movies=movies, movie_boxes=movie_boxes)


@app.route('/movie_actor_relations')
def movie_actor_relations():
    relations = MovieActorRelation.query.join(Movie, MovieActorRelation.movie_id == Movie.id).join(Actor, MovieActorRelation.actor_id == Actor.id).all()
    return render_template('movie_actor_relations.html', relations=relations)



