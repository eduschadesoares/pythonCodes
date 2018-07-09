#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fileHandler import File

class Controller:
    def start(self):
        data = self.file.readFile()




        def insertWord():
            word = str(input("Word to insert: "))
            self.file.writeFile(word)

        insertWord()

    def __init__(self):
        self.file = File()
