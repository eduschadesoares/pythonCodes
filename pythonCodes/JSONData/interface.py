#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Interface:

    def menu(self):
        print("Menu")
        print("1 - Listar Músicas")
        print("2 - Listar Bandas")
        print("3 - Listar Gêneros")
        print("4 - Listar Gravadoras")
        print("5 - Listar Playlists")

        choice = int(input())
        return choice