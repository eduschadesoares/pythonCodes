#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def connect():
    url = 'https://www.pythoncentral.io/how-to-get-a-substring-from-a-string-in-python-slicing-strings/'

    r = requests.get(url)

    soup = BeautifulSoup(r.content)

    p_words = soup.p

    for p in p_words:
        print("aqui", p)

connect()