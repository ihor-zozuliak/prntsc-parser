import string
import random
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS


def parse():
    url_part = ''.join((random.choice(string.ascii_lowercase + string.digits) for i in range(6)))
    parse_url = "https://prnt.sc/" + url_part
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    page = urlopen(parse_url)
    soup = BS(page, 'html5lib')
    ext_png = ".png"
    ext_https = "https:"
    image = soup.find_all("img", class_="no-click screenshot-image")
    for i in image:
        img_src = i["src"]
        if img_src.startswith("/"):
            img_src = ext_https + img_src
        if img_src.endswith(ext_png):
            urllib.request.urlretrieve(img_src, 'img/' + url_part + ext_png)
        else:
            urllib.request.urlretrieve(img_src, 'img/' + url_part + '.jpg')
        print(img_src)
        print(url_part)


while True:
    parse()
