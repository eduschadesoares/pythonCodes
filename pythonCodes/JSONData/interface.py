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
        print('╠┅▶ ⌨ Pressione enter para continuar')
        none = input()

    def finish_message(self):
        print("║")
        print("╚┅▶ O programa será encerrado! ㋡")

    def incorrect_value_message(self):
        print("╠┅▶  Valor incorreto")

    def invalid_value_message(self):
        print("╠┅▶  Valor inválido")

    def try_again_message(self):
        print("╠┅▶  Tente novamente!")

    def menu_get_post(self):
        print("╠════════════════════════╗")
        print("║          MENU          ║")
        print("╠═════╤══════════════════╣")
        print("║  1  │       GET        ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  2  │       POST       ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  0  │       EXIT       ║")
        print("╠═════╧══════════════════╝")
        print("╠┅▶ ⌨  Escolha uma opção:", end="")
        try:
            choice = int(input())
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            elif choice == 0:
                return 0
            else:
                return -1
        except ValueError:
            return -1

    def menu_get(self):
        print("╠════════════════════════╗")
        print("║        MENU GET        ║")
        print("╠═════╤══════════════════╣")
        print("║  1  │      Músicas     ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  2  │      Bandas      ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  3  │      Gêneros     ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  4  │    Gravadoras    ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  5  │     Playlists    ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  6  │      Voltar      ║")
        print("╠═════╧══════════════════╝")
        print("╠┅▶ ⌨  Escolha uma opção:", end="")
        try:
            choice = int(input())
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            elif choice == 3:
                return 3
            elif choice == 4:
                return 4
            elif choice == 5:
                return 5
            elif choice == 6:
                return 6
            else:
                return -1
        except ValueError:
            return -1

    def menu_post(self):
        print("╠════════════════════════╗")
        print("║        MENU POST       ║")
        print("╠═════╤══════════════════╣")
        print("║  1  │ Inserir Músicas  ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  2  │ Inserir Bandas   ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  3  │ Inserir Gêneros  ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  4  │Inserir Gravadora ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  5  │Inserir Playlists ║")
        print("╠━━━━━┿━━━━━━━━━━━━━━━━━━╣")
        print("║  6  │      Voltar      ║")
        print("╠═════╧══════════════════╝")
        print("╠┅▶ ⌨  Escolha uma opção:", end="")
        try:
            choice = int(input())
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            elif choice == 3:
                return 3
            elif choice == 4:
                return 4
            elif choice == 5:
                return 5
            elif choice == 6:
                return 6
            elif choice == 0:
                return 0
            else:
                return -1
        except ValueError:
            return -1
