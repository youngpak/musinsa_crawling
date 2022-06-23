from urllib.request import Request, urlopen,urlretrieve
import os
from bs4 import BeautifulSoup
from pprint import pprint
import urllib3

req = Request('https://www.musinsa.com/app/styles/lists', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup= BeautifulSoup(webpage, "html.parser")


img = soup.find_all('div',{'class':"right_contents hover_box"} )

list=[]
img_folder_path='C:\\Users\\PC\\OneDrive\\바탕 화면\\wearther\\images'

if not os.path.isdir(img_folder_path):
    os.mkdir(img_folder_path)

for data in img:
    list.extend(data.find_all('li'))

i=1
for li in list:
    img=li.find('img')
    img_src=img['src']
    urlretrieve(img_src,'./images/{}{}'.format(str(i),'.jpg'))
    i+=1

