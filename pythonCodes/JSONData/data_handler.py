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
                    if music['band'] == band['id']:
                        music_list['music_band'] = band['name']

                self.interface.list_music_view(music_list)

            self.interface.click_to_continue_view()
            menu()


        def listBands():
            band_data = self.connection.get_band_list()
            genre_data = self.connection.get_genre_list()
            record_data = self.connection.get_record_list()
            for band in band_data:
                band_list = {
                    'band_name': band['name'],
                }
                for genre in genre_data:
                    if band['genre'] == genre['id']:
                        band_list['band_genre'] = genre['name']
                for record in record_data:
                    if band['record'] == record['id']:
                        band_list['band_record'] = record['name']
                self.interface.list_band_view(band_list)

            self.interface.click_to_continue_view()
            menu()

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
