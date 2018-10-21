from flask import render_template

from app import app_task

from flask_bootstrap import Bootstrap

Bootstrap(app_task)


@app_task.errorhandler(404)
def page_not_found(e):
    return render_template('error_page/error404.html'), 404


if __name__ == '__main__':
    app_task.run()
