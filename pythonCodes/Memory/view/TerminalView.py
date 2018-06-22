#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Terminal interface here

class View():

    #BASIC MESSAGES
    def programStartMessage(self):
        print("Inicializando o \"Elefante\"")

    def programFinishMessage(self):
        print("O programa será fechado!")

    #I/O MESSAGES

    def insertMemValueMessage(self):
        print("Insira o tamanho da memória em KB. Insira 0 para finalizar:", end=" ")
        mem_Size = int(input())
        return mem_Size

    #SECCESS MESSAGES
    def successCreateMemoryMessage(self):
        print("Memórias criadas com sucesso!")

    #ALERT MESSAGES

    def errorMessage(self):
        print("Incorrect value!")

    def tryAgainMessage(self):
        print("Try again!")

    #MENU
    def menuMessage(self):
        print(" 1 - Mostrar Memórias")
        print(" 2 - Inserir Processo")
        print(" 3 - Remover Processo")
        print(" 0 - Sair")
