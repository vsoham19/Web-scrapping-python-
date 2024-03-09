import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.com/"

#by using request we will get the html content

r = requests.get(url)
htmlContent = r.content
print(htmlContent)

#to parse this html content we will use bs4

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

#get the title of content
title = soup.title
print(title)

#get the paragaraph
p = soup.find_all('p')
print(p)

anchor = soup.find_all('a')
print(anchor)

#traversing the tree

link = soup.a
#parent is the ascendent tag of a link, they can get iterated because they have a element within them called as siblings
for parent in link.parents:
    print(parent.name)
#sibling is a descendent of the parent and cannot be iterated
sibling = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
#here both b and c tag are child tags
print(sibling.prettify)

#In this program I have used general tags of bs4 on how to scrap the content of the website 

