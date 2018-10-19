from . import home  # 必须从点导入
from flask import request
from flask import render_template


@home.route("/user/<name>")
def index(name):
    return "<h2>大家好我是</h2>：%s" % name


@home.route("/agent")
def test1():
    user_agent = request.headers.get("User-Agent")
    return "<p>你的浏览器是%s</p>" % user_agent


@home.route("/")
def htmltest():
    return render_template("home/test.html", data={"name": "蒲小帅"})
