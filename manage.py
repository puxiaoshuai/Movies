from flask import render_template
from datetime import timedelta

from app import app_task

app_task.config.from_object('config')  # 载入配置文件
app_task.config['TEMPLATES_AUTO_RELOAD'] = app_task.config['IS_TRUE']
app_task.config['SECRET_KEY'] = app_task.config["SECRET_KEY"]


# app_task.config['DEBUG']读取，必须大写

@app_task.errorhandler(404)
def page_not_found(e):
    return render_template('error_page/error404.html'), 404


if __name__ == '__main__':
    #生产环境，不加载默认的
    app_task.run(debug=app_task.config['IS_TRUE'])
