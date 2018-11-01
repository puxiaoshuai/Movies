from .. import db
from app.home.froms import RegistForm
from app.home.models import User
from app.spider.net_movies import MovieTop
from . import home  # 必须从点导入
from flask import url_for, flash, session, current_app
from flask import render_template, redirect, request
import json
from flask_sqlalchemy import SQLAlchemy


@home.route("/user/<name>")
def index(name):
    return "<h2>大家好我是</h2>：%s" % name


@home.route("/agent")
def agent():
    user_agent = request.headers.get("User-Agent")
    return render_template('home/mine.html', name=user_agent)


@home.route("/")
def htmltest():
    list = ["Python", "Java", "C++"]

    def hello():
        return "我是方法"

    return render_template("home/home.html", data={"name": "蒲小帅"}, hello=hello(), listdata=list)


@home.route('/register', methods=["GET", "POST"])
def register():
    form = RegistForm(request.form)
    if request.method == "POST":
        if form.validate():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None:
                user = User(username=form.username.data)
                db.session.add(user)
                db.session.commit()

                session['username'] = form.username.data
                form.username.data = ''
                flash("注册成功")
                return redirect(url_for('home.agent'))
            else:
                flash("该用户已经注册")
                return redirect(url_for('home.agent'))

        else:
            flash(form.errors)

    return render_template('home/register.html')
    # if request.method == "POST":
    #     if request.form['username'] == 'puhao' or request.form['password'] == '123456':
    #         flash("登录成功")
    #         return redirect(url_for('home.agent'))
    #     else:
    #         flash("登录失败")
    # return render_template('home/register.html')


# api  这就算写接口了


@home.route("/news", methods=['GET'])
def start():
    data = [{'name': 'puxiaoshuai'}, {'age': 25}, {'address': u"成都"}]
    print(type(json.dumps(data)))  # 把对象转成字符串
    data1 = '[{"name": "puxiaoshuai"}, {"age": 25}, {"address": "成都"}]'
    print(type(json.loads(data1)))  # 把字符串转 对象
    print(json.loads(data1))
    return json.dumps(data)


@home.route('/movies/<page>', methods=["GET"])
def movies(page):
    movies = MovieTop()
    result = movies.getMovies(page)
    print(result)
    return render_template('home/movies.html', result=result)
