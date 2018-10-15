from flask import Flask

app_task = Flask(__name__)
app_task.debug = True

from app.home import home as home_buleprint
from app.admin import admin as admin_buleprint

app_task.register_blueprint(home_buleprint)
app_task.register_blueprint(admin_buleprint, url_prefix="/admin")
