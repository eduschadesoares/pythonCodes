#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class File:

    def readFile(self):
        file = open("source.txt", "r")
        data = file.readlines()
        return data

    def writeFile(self, word):
        file = open("source.txt", "a")
        file.writelines(word + os.linesep)
        file.close()
