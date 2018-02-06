import json
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
            tds = tr('a', rel="bookmark")
            mytry = tr.find('p')
            # print(mytry)
            mlist[tds[0].string] = {
                "日期": tds[1].string,
                "简介": mytry.get_text()
            }


# 利用数据结构展示并输出结果
def printMyList(mList):
    # indent=1是格式化的模式,ensure_ascii=False解决编码问题
    jsonDumpsIndentStr = json.dumps(mList, indent=1,ensure_ascii=False)
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
    with open(filename, 'w') as f: f.write(json.dumps(mlist, indent=1,ensure_ascii=False))


if __name__ == "__main__":
    mlist = load("info.json")
    url = "https://www.llss.fun/wp/"
    html = getHTMLText(url)
    fillMyList(mlist, html)
    printMyList(mlist)
    save("info.json", mlist)
