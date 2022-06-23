import urllib.request
import urllib.parse

base_url='https://'
url_join = urllib.parse.urljoin(base=base_url, url="//image.msscdn.net/images/style/list/l_3_2022062214302100000008217.jpg",allow_fragments=True)
#url='https://image.msscdn.net/images/style/list/l_3_2022062214302100000008217.jpg'

#urllib.request.urlretrieve(url_join,'댄디2.jpg')

print(url_join)
