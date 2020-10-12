from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, ssl
import re

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def clear_attributes(text):
    temp = text
    temp = re.sub(r'<[^>]*>', '', temp, flags=re.MULTILINE)
    return temp

url = "https://www.cnn.com/2020/10/06/politics/trump-ends-stimulus-talks/index.html"

page = urlopen(url)

soup = BeautifulSoup(page.read(), features="lxml")

#print(soup)

article_text = ""

for div in soup.find_all('div', attrs={'class': 'zn-body__paragraph'}):
    article_text += clear_attributes(str(div))

print(article_text)