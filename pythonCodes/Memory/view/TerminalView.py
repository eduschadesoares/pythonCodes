#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Terminal interface here

class View():

    #ALERT MESSAGES
    def errorMessage(self):
        print("Incorrect value!")
    def tryAgainMessage(self):
        print("Try again!")
    def notAvailableMemoryMessage(self):
        print("Error, not enough available memory to create this process")
    def processCreatedMessage(self):
        print("")

    #CHOICES
    def showMemoriesChosen(self):
        print("Displaying memories")
    def insertProcessChosen(self):
        print("Create a process")
    def listProcessChosen(self):
        print("Dysplaying processes")
    def removeProcessChosen(self):
        print("Remove a process")


    #BASIC MESSAGES
    def programStartMessage(self):
        print("Inicializando o \"Elefante\"")
    def programFinishMessage(self):
        print("O programa será fechado!")

    #I/O MESSAGES
    def createProcessMessage(self):
        print("Insert the process name:", end="")
        processName = str(input())
        print("Insert the process size:", end="")
        try:
            processSize = int(input())
        except ValueError:
            print("Irregular value")
            return

        #Returns a dict
        processInfo = {
            'name': processName,
            'size': processSize,
        }

        return processInfo

    def removeProcessMessage(self):
        print("Insert the process ID:", end="")
        try:
            processID = int(input())
        except ValueError:
            print("Irregular value")
            return

        return processID


    def insertMemValueMessage(self):
        print("Insira o tamanho da memória em KB. Insira 0 para finalizar:", end=" ")
        mem_Size = int(input())
        return mem_Size
    def clickToContinueMessage(self):
        print("Click to continue")
        none = input()

    #SECCESS MESSAGES
    def successfullyCreatedMemoryMessage(self):
        print("Memórias criadas com sucesso!")

    #DISPLAY INFORMATION MESSAGES


    #MENU
    def menuMessage(self):
        print("")
        print(" MENU")
        print(" 1 - Mostrar Memórias")
        print(" 2 - Criar Processo")
        print(" 3 - Remover Processo")
        print(" 4 - Mostrar processos")
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
            elif choice == 4:
                return 4
            elif choice == 0:
                return 0
            else:
                return -1

        except:
            print("Valor irregular")
            return -1
