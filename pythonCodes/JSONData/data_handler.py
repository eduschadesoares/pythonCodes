#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from connection import Connection
from interface import Interface

class Data:
    def start_program(self):

        def list_musics():
            music_data = self.connection.get_music_list()
            band_data = self.connection.get_band_list()
            for music in music_data:
                music_list = {
                    'music_name': music['name'],
                    'music_duration': music['duration'],
                    'music_release': music['release'],
                }
                for band in band_data:
                    if music['id'] == band['id']:
                        music_list['music_band'] = band['name']

                self.interface.list_music_view(music_list)

            self.interface.click_to_continue_view()
            menu()


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
            choice = self.interface.menu_view()
            if choice is 1:
                list_musics()
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
            else:
                menu()
        menu()

    def __init__(self):
        self.connection = Connection()
        self.interface = Interface()
