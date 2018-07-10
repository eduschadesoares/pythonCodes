#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from fileHandler import File
import re


def connect():
    # url = 'https://www.pythoncentral.io/how-to-get-a-substring-from-a-string-in-python-slicing-strings/'
    url = 'https://imasters.com.br/back-end/aprendendo-sobre-web-scraping-em-python-utilizando-beautifulsoup'

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    for i in range(50):
        p_words = soup.find_all('p')[i].get_text()

        all_words = re.split('[. ,]', p_words)

        #print(all_words)

        file = File()
        for i in all_words:
            file.writeFile(i)
            print(i)

   # print(p_words)

#     for p in p_words:
#       print("aqui", p)

connect()