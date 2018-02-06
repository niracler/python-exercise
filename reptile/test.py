import requests
from bs4 import BeautifulSoup
import bs4


# 获取HTML页面的函数
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 提取网页内容中信息到合适的数据结构
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser") # 煲一个靓汤
    for tr in soup.find('tbody').children:   # 遍历tbody标签的孩纸
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td') # 找到里面的td标签
            print(tds)
            ulist.append([tds[0].string, tds[1].string, tds[2].string])# 将内容放入


# 利用数据结构展示并输出结果
def printUnivList(uList, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u = uList[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    # print(html[:1111])
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)

if __name__ == '__main__':
    main()
