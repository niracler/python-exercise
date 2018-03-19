import json
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 不是200,引发HTTPError异常
        # r.encoding = r.apparent_encoding  # 转编码,假如编码有问题，可以试试
        r.encoding = "UTF-8"
        # print(r.encoding)
        return r.text
    except:
        return "产生异常"


# 将我要的信息放到相应的数据结构中
def fillMyList(article_list, html):
    soup = BeautifulSoup(html, "html.parser")

    try:
        for article in soup.find_all("article"):  # 找到所有的文章
            if isinstance(article, bs4.element.Tag):  # 判断是否是标签
                article_info = {}  # 创建对应的文章对象信息字典

                article_bookmark = article('a', rel="bookmark")
                article_info["日期"] = article_bookmark[1].string
                article_info["网址"] = article_bookmark[0]["href"]

                article_img = article.find('img')
                article_info["图片"] = article_img["src"]
                # urlretrieve(article_info["图片"], article_info["图片"].split("/")[-1])
                picture = requests.get(article_info["图片"], timeout=30, headers=headers)
                fp = open("img/" + article_info["图片"].split("/")[-1], 'wb')
                fp.write(picture.content)
                fp.close()

                article_intro = article.find('p')
                article_info["简介"] = article_intro.get_text()

                article_list[article_bookmark[0].string] = article_info

                # test
                # print(article_bookmark[0]["href"])
    except:
        return "产生异常"


# 利用数据结构展示并输出结果
def printMyList(mList):
    # indent=1是格式化的模式,ensure_ascii=False解决编码问题
    jsonDumpsIndentStr = json.dumps(mList, indent=1, ensure_ascii=False)
    print(jsonDumpsIndentStr)


# 读档
def load(filename):
    try:
        with open(filename) as f:
            mlist = json.load(f)
    except:
        mlist = {}
    return mlist


# 存档
def save(filename, mlist):
    with open(filename, 'w') as f: f.write(json.dumps(mlist, indent=1, ensure_ascii=False))


def driver(url, filename):
    mlist = {}
    html = getHTMLText(url)
    fillMyList(mlist, html)
    # printMyList(mlist)
    save(filename, mlist)
    print(url + " in " + filename)


if __name__ == "__main__":
    url = "https://www.llss.fun/wp/page/" + str(500)
    driver(url, "info/info.json")
