
from app.home.froms import SearchForm
from app.home.net_books import YushuBook
from . import home  # 必须从点导入
from flask import request, url_for, flash,jsonify
from flask import render_template, redirect, request
from  helper import is_isbn


#////@home.route("/book/search/<q>/<page>")
#/? &
#request 获取？后面的值
#request 查询参数，POST参数。。等book/search?q="天坛"page=1
@home.route("/book/search")
def search():
    """q=request.args["q"]
    page=request.args["page"]
    """
    form=SearchForm(request.args)
    if form.validate():
        q=form.q.data.strip()
        isbn_or_key = is_isbn(q)
        if isbn_or_key == 'isbn':
            result = YushuBook.search_by_isbn(isbn_or_key)
        else:
            result = YushuBook.search_by_key(isbn_or_key)
        return jsonify(result)
    else:
        return jsonify(form.errors)




