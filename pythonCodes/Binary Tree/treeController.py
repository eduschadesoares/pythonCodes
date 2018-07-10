#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fileHandler import File
from tree import Tree


class Controller:

    def start(self):
        def getWords():
            data = self.file.readFile()
            if data:
                root = True
                for line in data:
                    line = line.rstrip('\n')  # Remove \n
                    if root:
                        tree = Tree(line)
                        root = False
                    else:
                        tree.insert(line)
                tree.printTree()
            else:
                print("Sem palavras")

        """def insertWord():
            word = str(input("Word to insert: "))
            self.file.writeFile(word)

            # data = self.file.readFile()
            # print(data) """

        getWords()

        # insertWord()

    def __init__(self):
        self.file = File()
