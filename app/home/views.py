from app.home.froms import RegistForm
from . import home  # 必须从点导入
from flask import request, url_for
from flask import render_template,redirect,flash



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
@home.route('/register',methods=["GET","POST"])
def register():
    if request.method=="GET":
        form =RegistForm()
        return  render_template("home/register.html",form=form)
    elif request.method=="POST":
        form=RegistForm()
        if form.validate_on_submit():
            name=form.username.data
            pwd=form.password.data
            return redirect(url_for('agent'))
        else:
            return  render_template("home/register.html",form=form)
