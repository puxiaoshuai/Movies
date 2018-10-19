from . import admin #必须从点导入


@admin.route("/")
def index():
    return "<h1 style='color:red'>我是后台界面数据</h1>"
