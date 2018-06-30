#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Interface:

    def list_music_view(self, music_list):
        print('Nome - {}'.format(music_list['music_name']))
        print('Banda - {}'.format(music_list['music_band']))
        print('Duração - {}'.format(music_list['music_duration']))
        print('Lançamento - {}'.format(music_list['music_release']))
        print('')

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

        choice = int(input())
        return choice