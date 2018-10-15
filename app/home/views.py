from . import home
from flask import template_rendered


@home.route("/")
def index():
    return "我是前台页面"
