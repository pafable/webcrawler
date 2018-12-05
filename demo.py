from urllib.request import urlopen

html = urlopen("http://pafable.com")
print(html.read())