#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Terminal interface here

class View():

    #ALERT MESSAGES
    def errorMessage(self):
        print("Incorrect value!")
    def tryAgainMessage(self):
        print("Try again!")

    #CHOICES
    def showMemoriesChosen(self):
        print("Displaying memories")
    def insertProcessChosen(self):
        print("Insert a process")
    def removeProcessChosen(self):
        print("Remove a process")


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
    def successfullyCreatedMemoryMessage(self):
        print("Memórias criadas com sucesso!")

    #DISPLAY INFORMATION MESSAGES


    #MENU
    def menuMessage(self):
        print("")
        print(" MENU")
        print(" 1 - Mostrar Memórias")
        print(" 2 - Inserir Processo")
        print(" 3 - Remover Processo")
        print(" 0 - Sair")
        print("Insira a opção:", end="")
        try:
            choice = int(input())

            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            elif choice == 3:
                return 3
            elif choice == 0:
                return 0
            else:
                return -1

        except:
            print("Valor irregular")
            return -1
