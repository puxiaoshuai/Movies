from app.libs.httpUtils import HTTP
from flask import  current_app

class YushuBook:

    isbn_url = "https://api.douban.com/v2/book/isbn/{}"
    key_url = "http://t.yushu.im/v2/book/search?q={}&start={}&count={}"

    @classmethod
    def search_by_isbn(cls, isbn_key):
        url = cls.isbn_url.format(isbn_key)
        httputils = HTTP()
        result = httputils.get(url)
        # result dict
        return result

    @classmethod
    def search_by_key(cls, key_word, page=1):

        httputils = HTTP()
        url1 = cls.key_url.format(key_word, current_app.config['PRE_PAGE'],cls.culculate_start(page) )
        result = httputils.get(url1)
        # result dict
        return result
    @staticmethod
    def culculate_start(page):
        return (page - 1) * current_app.config['PRE_PAGE']
