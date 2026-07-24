# -*- code = utf-8 -*-

from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class=boldest>Extremely bold</b>',features="html.parser")

tag = soup.b 

print(tag) #<b class="boldest">Extremely bold</b>
print(tag.name) #b
print(tag['class']) #['boldest']
print(tag.attrs) #{'class': ['boldest']}