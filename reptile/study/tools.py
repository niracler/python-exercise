import requests


def getHTMLText(url="http://www.llss.pw/wp/"):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 不是200,引发HTTPError异常
        r.encoding = r.apparent_encoding  # 转编码,假如编码有问题，可以试试
        return r.text
    except:
        return "产生异常"
# CREATE TABLE pages (id BIGINT(7) NOT NULL AUTO_INCREMENT, title VARCHAR(200), content VARCHAR(10000),url VARCHAR(200), img_url VARCHAR(200) , cteated TIMESTAMP DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY(id))