#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

localhost = '127.0.0.1'
port = '9000'

# params = {'localhost': localhost, 'port': port}

session = 'musics'

url = 'http://{}:{}/{}'.format(localhost, port, session)

data = requests.get(url).json()

print(data)
