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

    def get_music_list(self):
        search = 'musics'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        data = requests.get(url).json()
        return data

    def get_band_list(self):
        search = 'bands'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        data = requests.get(url).json()
        return data

    def get_genre_list(self):
        search = 'genres'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        data = requests.get(url).json()
        return data

    def get_record_list(self):
        search = 'records'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        data = requests.get(url).json()
        return data

    def get_playlist_list(self):
        search = 'playlists'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        data = requests.get(url).json()
        return data

    def get_music_list(self):
        search = 'musics'
        url = 'http://{}:{}/{}'.format(localhost, port, search)
        data = requests.get(url).json()
        return data