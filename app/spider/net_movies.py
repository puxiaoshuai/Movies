from app.libs.httpUtils import HTTP



class MovieTop:
    url="http://api.douban.com/v2/movie/top250?start={}&count={}"
    @classmethod
    def getMovies(cls,page):
        https=HTTP()
        url=cls.url.format(cls.culculate_start(page),10)
        result=https.get(url)
        data=cls.create_json(result)
        return  data

    @staticmethod
    def culculate_start(page):
        a=int(page)-1
        b=a*10
        return b

    def create_json(shuju):
        sub = shuju["subjects"]
        listData=[]

        for x in sub:
            oneMoves = {}
            oneMoves["title"]=x["title"]
            gen=' '.join(x["genres"])
            oneMoves["genres"]=gen
            oneMoves["icon"]=x["images"]["large"]
            cats=x["casts"]
            names=[]
            for i in cats:
                name=i["name"]
                names.append(name)
            zhuyan='- '.join(names)
            oneMoves["zhuyan"]=zhuyan
            listData.append(oneMoves)
        return listData



