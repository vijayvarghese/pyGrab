import urllib.request
from bs4 import BeautifulSoup as bsp
import requests

samp_url = "https://pngtree.com/so/"

item_ = input("Enter item name :  ")
url = samp_url+str(item_)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
que = urllib.request.Request(url, headers = headers)
req = urllib.request.urlopen(que)

html_par = bsp(req.read(),"html.parser")

oru_li = html_par.findAll("li",{"class": "li-box search_keyword_statis_js"})
count = 0
for index,li in enumerate(oru_li):
    filename_ = str(index+1)+".jpeg"
    try:
        r = requests.get(li.div.a["data-media"])
        with open(filename_, 'wb') as outfile:
            outfile.write(r.content)
        print(str(li.div.a["data-media"]),"Downloaded Sucessfuly !!")
        count += 1
    except:
        pass
    
print("Total",count,"files downloaded")

