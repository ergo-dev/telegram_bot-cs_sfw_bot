import requests
import re
from bs4 import BeautifulSoup
import nltk
# '''from urllib '''import urlopen

# URL = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
# HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'accept': '*/*'}
#
# def get_html(url, params=None):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.findAll('tr')
#
#     peoples = []
#     for item in items:
#         peoples.append({
#             'title': item.find('tr')
#         })
#     print(peoples)
#
# def parse():
#     html = get_html(URL)
#     if html.status_code == 200:
#         print(html.text)
#     else:
#         print('Error')
#
# parse()

URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
URLKA_2 = 'http://cs.sfw.so/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

full_page1 = requests.get(URLKA_1, headers=headers)
full_page2 = requests.get(URLKA_2, headers=headers)
soup1 = BeautifulSoup(full_page1.content, 'html.parser')
soup2 = BeautifulSoup(full_page2.content, 'html.parser')
convert1 = soup1.findAll("tr")
# convert2 = soup1.findAll("img", {"class": 'img-polaroid'})
# convertP = soup1.findAll("tr", {"class": "context-menu-one"})
peoples = convert1[-2].text
map_text = convert1[-3].text
# print(peoples)
# print(map_text)
peoples = str(peoples)
peoples = re.sub(r"[Игроки:]", "", peoples)
peoples = peoples.strip()
print(peoples)
map_text = str(map_text)
map_text = re.sub(r'[Карт:]', '', map_text)
map_text = map_text.strip()
print(map_text)
print(convert2)
# map_photo = convert2
# players = convertP
# anonymous = convertP[::]
# anonymous = anonymous
# convert2 = urlopen(URLKA_1).read()
# raw = nltk.clean_html(convert2)
# print(raw)
# print(anonymous)