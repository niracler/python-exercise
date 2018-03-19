from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.baidu.com")

# 现在用Beautiful库都是要这样，加上"html.parser"
bsObject = BeautifulSoup(html.read(), "html.parser")

# 拿出该对象的头标签
print(bsObject.head)