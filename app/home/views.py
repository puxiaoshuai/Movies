from . import home  # 必须从点导入
from flask import request
from flask import render_template


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
