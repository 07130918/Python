import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.python.org')
soup = BeautifulSoup(html.text, 'lxml')

title = soup.find_all('title')
print(title[0].text)


intro = soup.find_all('div', {'class': 'introduction'})
print(intro[0].text)
go = soup.find_all('button', {'class': 'search-button'})
print(go[0].text)
