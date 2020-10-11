import requests
import threading
import datetime
from fake_useragent import UserAgent
import time
start_time=time.time()


def check_proxy(type_proxy, ip):
	url = 'https://vk.com/'
	if (type_proxy=='http'):
		url = 'http://www.biglongnow.com/'
	if (type_proxy=='https'):
		url = 'https://vk.com/'
	proxies = [{
    	type_proxy: ip,
	},]
	for proxy in proxies:
		try:
			response = requests.post(url, proxies={type_proxy: proxy.get(type_proxy)},  headers={'User-Agent': UserAgent().chrome})
			if str(response.status_code) == '200':
				print(proxy.get(type_proxy))
		except requests.exceptions.ProxyError:
			break;
