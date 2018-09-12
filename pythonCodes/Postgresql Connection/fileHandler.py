#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class File:

    def readNome(self):
        file = open("nome.txt", "r")
        nome = file.readlines()
        file.close()
        return nome

    def readSobrenome(self):
        file = open("sobrenome.txt", "r")
        sobrenome = file.readlines()
        file.close()
        return sobrenome
