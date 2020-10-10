import requests
from bs4 import BeautifulSoup


data = requests.get('https://www.python.org/')
page = data.text
soup = BeautifulSoup(page, 'html.parser')
head = soup.head
root = soup.html


div = root.findAll('div', class_='medium-widget event-widget last')
events_list = []
for news in div:
    if news.find('div', class_='shrubbery'):
        events_list.append(news.text)

print(events_list[0])

