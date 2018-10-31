from flask import render_template
from datetime import timedelta

from app import app_task




# app_task.config['DEBUG']读取，必须大写

@app_task.errorhandler(404)
def page_not_found(e):
    return render_template('error_page/error404.html'), 404


if __name__ == '__main__':
    #生产环境，不加载默认的
    app_task.run(port=1000)
