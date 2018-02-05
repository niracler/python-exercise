import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()#不是200,引发HTTPError异常
        # r.encoding = r.apparent_encoding # 转编码,假如编码有问题，可以试试
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://www.llss.fun/wp/"
    print(getHTMLText(url))