from flask import Flask
from app.home import home as home_buleprint
from app.admin import admin as admin_buleprint
from app.secure import IS_TRUE,SECRET_KEY
from flask_sqlalchemy import SQLAlchemy

app_task = Flask(__name__)
app_task.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:puhao@localhost/movies"
db=SQLAlchemy(app_task)
app_task.config['TEMPLATES_AUTO_RELOAD'] = IS_TRUE
app_task.config['SECRET_KEY'] = SECRET_KEY
app_task.config['DEBUG'] = IS_TRUE
app_task.register_blueprint(home_buleprint)
app_task.register_blueprint(admin_buleprint, url_prefix="/ad")
