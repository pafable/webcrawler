from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pafable.com")
bsobject = BeautifulSoup(html.read(),"html.parser")
print(bsobject.h1)