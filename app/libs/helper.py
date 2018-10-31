
def is_isbn(word):
    """
    http://t.yushu.im/v2/book/search?q={}&start={}&count={}
    https://api.douban.com/v2/book/isbn/{isbn}
     q，普通关键字，isbn
     page
     #isbn13.13个数字组成
     #isbn10 10个0-9，包含-
    :return:
    假条件最好放前面
   ，耗时等放后面    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace("-", "")
    if '-' in word and len(short_q) == 10 and short_q.isdight:
        isbn_or_key = 'isbn'
    return isbn_or_key