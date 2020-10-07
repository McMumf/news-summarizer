from urllib.request import urlopen
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.cnn.com/2020/10/06/politics/trump-ends-stimulus-talks/index.html"

page = urlopen(url)

print(page)