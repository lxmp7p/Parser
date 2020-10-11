import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
from proxyChecker import check_proxy


proxy_type = input("Выберите необходимый тип прокси: \n 1)HTTP \n 2)HTTPS \n 3)SOCKS4 \n 4)SOCKS5 \nВаш выбор: ")
proxy_type_dict = [{'type': 'http', 'id': '1'},{'type': 'https', 'id': '2'},{'type': 'socks4', 'id': '3'},{'type': 'socks5', 'id': '4'},]
for i in proxy_type_dict:
    if(i.get('id') == proxy_type):
        proxy_type = i.get('type')
print("Ожидайте!")
data = requests.get('https://top-proxies.ru/free_proxy.php', headers={'User-Agent': UserAgent().chrome})
page = data.text
soup = BeautifulSoup(page, 'html.parser')
table = soup.tbody
line = table.findAll('td')
c = 0
f = ''
proxy = []
temp = {}
for i in line:
    if c<5:
        temp[c] = str(i.text)
        c += 1
    if c==5:
        proxy.append(temp)
        temp = {}
        c = 0

for i in proxy:
    try:
        if (i.get(2) == proxy_type):
            check_proxy(i.get(2),i.get(1))
    except Exception as e:
        raise e

