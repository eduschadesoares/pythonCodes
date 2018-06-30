#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from connection import Connection
from interface import Interface

class Data:
    def start_program(self):

        def listMusics():
            data = self.connection.get_music_list()
            print(data)

        def listBands():
            data = self.connection.get_band_list()
            print(data)

        def listGenres():
            data = self.connection.get_genre_list()
            print(data)

        def listRecords():
            data = self.connection.get_record_list()
            print(data)

        def listPlaylists():
            data = self.connection.get_playlist_list()
            print(data)

        def menu():
            choice = self.interface.menu()
            if choice is 1:
                listMusics()
            elif choice is 2:
                listBands()
            elif choice is 3:
                listGenres()
            elif choice is 4:
                listRecords()
            elif choice is 5:
                listPlaylists()
            elif choice is 0:
                exit()

            menu()

        menu()

    def __init__(self):
        self.connection = Connection()
        self.interface = Interface()
