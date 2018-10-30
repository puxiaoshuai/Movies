from flask import Blueprint

home = Blueprint("home", __name__)
import app.home.home_views
import app.home.book_views
