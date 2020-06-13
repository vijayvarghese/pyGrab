import urllib.request
from bs4 import BeautifulSoup as bsp
from os.path import join

samp_url = "https://pngtree.com/so/"


item_ = input("Enter item name :  ")
url = samp_url+str(item_)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
que = urllib.request.Request(url, headers = headers)
req = urllib.request.urlopen(que)

html_par = bsp(req.read(),"html.parser")
oru_li = html_par.findAll("li",{"class":"li-box search_keyword_statis_js"})



for index,li in enumerate(oru_li):
    filename_ = str(index+1)+".jpeg"
    path = r""# set a path to store the Downloaded images
    filename_path = join(path,filename_)
    


    urllib.request.urlretrieve(str(li.img["data-original"]),filename_path)
    print(str(li.img["data-original"]),"Downloaded Sucessfuly !!")


