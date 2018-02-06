import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 不是200,引发HTTPError异常
        # r.encoding = r.apparent_encoding # 转编码,假如编码有问题，可以试试
        return r.text
    except:
        return "产生异常"


# 将我要的信息放到相应的数据结构中
def fillMyList(mlist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find_all("article"):
        if isinstance(tr, bs4.element.Tag):
            tds = tr('a',rel="bookmark")
            mlist.append([tds[0].string, tds[1].string])

# 利用数据结构展示并输出结果
def printMyList(uList):
    for i in mlist:
        print(i[0], i[1], "\n")

if __name__ == "__main__":
    mlist = []
    url = "https://www.llss.fun/wp/"
    html = getHTMLText(url)
    # print(getHTMLText(url)[:1000])
    fillMyList(mlist, html)
    printMyList(mlist)
