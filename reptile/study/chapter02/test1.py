from bs4 import BeautifulSoup

from reptile.study.tools import getHTMLText

html = getHTMLText()
bsObj = BeautifulSoup(html, "html.parser")
# print(bsObj)

# 下面，我们来学查找特定的标签
# 标签，以及特定属性,限定标签
articles = bsObj.find_all("article", {"class":"post"})

for article in articles:
    print(article.get_text())