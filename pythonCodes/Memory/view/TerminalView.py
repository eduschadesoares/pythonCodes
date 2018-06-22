#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Terminal interface here

class View():

    #Basic Messagens
    def programStartMessage(self):
        print("Inicializando o \"Elefante\"")

    def programFinishMessage(self):
        print("O programa será fechado!")

    #I/O Messages

    def insertMemValueMessage(self):
        print("Insira o tamanho da memória em KB. Insira 0 para finalizar:", end=" ")
        mem_Size = int(input())
        return mem_Size


    #Alert Messages

    def errorMessage(self):
        print("Incorrect value!")

    def tryAgainMessage(self):
        print("Try again!")
