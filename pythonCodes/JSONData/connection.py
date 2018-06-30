#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

localhost = '127.0.0.1'
port = '9000'

class Connection:
    def __init__(self):
        self.connection = self.estabilish_connection(localhost, port)

    def estabilish_connection(self, localhost, port):
        url = 'http://{}:{}/status'.format(localhost, port)
        try:
            connection = requests.get(url)
            if connection:
                print("Connected to server!")
            return True
        except Exception as error:
            print("Could not connect to server!")
            print(error)
            return False
