#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Interface:

    def list_music_view(self, music_list):
        print('Nome - {}'.format(music_list['music_name']), end=' ')
        print('Banda - {}'.format(music_list['music_band']), end=' ')
        print('Duração - {}'.format(music_list['music_duration']), end=' ')
        print('Lançamento - {}'.format(music_list['music_release']), end=' ')
        print('')

    def list_band_view(self, band_list):
        print('Nome - {}'.format(band_list['band_name']))
        print('Gênero - {}'.format(band_list['band_genre']))
        print('Gravadora - {}'.format(band_list['band_record']))
        print('')

    def list_genre_view(self, genre_list):
        print('Nome - {}'.format(genre_list['genre_name']))
        print('')

    def list_record_view(self, record_list):
        print('Nome - {}'.format(record_list['record_name']))
        print('')

    def list_playlist_view(self, playlist_list):
        print('')
        print('Playlist - {}'.format(playlist_list['playlist_name']))

    def list_playlist_music_view(self, music, band):
        print('Música - {} - {}'
              ''.format(music, band))

    def click_to_continue_view(self):
        print('Pressione enter para continuar')
        none = input()

    def menu_view(self):
        print("Menu")
        print("1 - Listar Músicas")
        print("2 - Listar Bandas")
        print("3 - Listar Gêneros")
        print("4 - Listar Gravadoras")
        print("5 - Listar Playlists")
        print("0 - Sair")

        choice = int(input())
        return choice