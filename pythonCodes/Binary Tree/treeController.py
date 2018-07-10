#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fileHandler import File
from tree import Tree

import getch, keyboard, os



class Controller:

    def start(self):
        tree = Tree("example")
        def get_words():
            data = self.file.readFile()
            if data:
                root = True
                for line in data:
                    line = line.rstrip('\n')  # Remove \n
                    tree.insert(line)
                tree.printTree()
            else:
                print("Sem palavras")


        def find_words():
            word = []
            while True:
                char = getch.getch()
                os.system('clear')
                try:
                    if char == '\n':
                        break
                    word.append(char)
                    tree.searchTree(word)
                except Exception as error:
                    print(error)
                    break
            # print(word)




        """def insertWord():
            word = str(input("Word to insert: "))
            self.file.writeFile(word)

            # data = self.file.readFile()
            # print(data) """

        get_words()
        find_words()
        # insertWord()

    def __init__(self):
        self.file = File()
