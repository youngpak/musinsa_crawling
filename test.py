from urllib.request import urlretrieve,Request
from urllib.parse import quote_plus    
from bs4 import BeautifulSoup as BS    
from selenium import webdriver  
import urllib.parse
import os

i_URL = f'https://www.musinsa.com/app/styles/lists?use_yn_360=&style_type=formal&brand=&model=&tag_no=&max_rt=&min_rt=&display_cnt=60&list_kind=big&sort=date&page=1'


driver=webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get(i_URL)
html = driver.page_source
soup = BS(html,features="html.parser")


img = soup.find_all('div',{'class':"right_contents hover_box"} )

list=[]
img_folder_path='C:\\Users\\PC\\OneDrive\\바탕 화면\\wearther\\m_formal'

if not os.path.isdir(img_folder_path):
    os.mkdir(img_folder_path)


for data in img:
    list.extend(data.find_all('li'))

i=1
base_url='https://'
for li in list:
    img=li.find('img')
    img_src=img['src']
    url_join = urllib.parse.urljoin(base=base_url, url=img_src,allow_fragments=True)
    urllib.request.urlretrieve(url_join,'./m_formal/{}{}'.format(str(i),'.jpg'))
    i+=1

# i_list = []
# count = 1

# print("Searching...")
# for i in img:
#    try:
#       i_list.append(i.attrs["src"])
#    except KeyError:
#       i_list.append(i.attrs["data-src"])

# print("Downloading...")
# for i in i_list:
#    urlretrieve(i,"images/"+keyword+str(count)+".jpg")
#    count+=1

# driver.close()
# print("FINISH")