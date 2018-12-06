# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://pafable.com")
# bsobject = BeautifulSoup(html.read(),"html.parser")
# print(bsobject.h1)

import os

def create_project_dir(dir):
    if not os.path.exists(dir):
        print('Creating the directory ' + dir)
        os.makedirs(dir)

create_project_dir('thesite')