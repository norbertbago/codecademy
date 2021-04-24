import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html','html.parser')
soup = BeautifulSoup(webpage.content)

# print(soup)
print(soup.p)
print(soup.p.string)

