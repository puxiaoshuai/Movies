from flask import Flask
from flask_migrate import Migrate
from app.secure import IS_TRUE, SECRET_KEY
from flask_sqlalchemy import SQLAlchemy
app_task = Flask(__name__)

app_task.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:puhao@localhost/movies"
app_task.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False# true的时候，控制台能打印出信息
app_task.config['SQLALCHEMY_ECHO'] = IS_TRUE
db = SQLAlchemy(app_task)
migrate=Migrate(app=app_task,db=db)
app_task.config['TEMPLATES_AUTO_RELOAD'] = IS_TRUE
app_task.config['SECRET_KEY'] = SECRET_KEY
app_task.config['DEBUG'] = IS_TRUE
from app.home import home as home_buleprint
from app.admin import admin as admin_buleprint
app_task.register_blueprint(home_buleprint)
app_task.register_blueprint(admin_buleprint, url_prefix="/ad")
