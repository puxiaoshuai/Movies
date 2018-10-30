from httpUtils import HTTP


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
    def search_by_key(cls, key_word, count=15, start=0):
        httputils = HTTP()
        url1 = cls.key_url.format(key_word, start, count)
        result = httputils.get(url1)
        # result dict
        return result
