from urllib.request import urlopen

html = urlopen("http://www.baidu.com")
print(html.read())