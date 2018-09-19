#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json

client_id = ''
client_secret = ''
scopes = 'user-read-private%20user-read-email'

url = 'https://accounts.spotify.com/authorize/?client_id=' + client_id + '&response_type=code&redirect_uri=' + '127.0.0.1' + '&scope=' + scopes + '&state=34fFs29kd09'

url2 = '	https://api.spotify.com/v1/me/top/artists'

r = requests.get(url)
r2 = requests.get(url2)

print(r.text)
# print(r.text)
