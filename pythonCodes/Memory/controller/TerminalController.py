#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Controller stuff here

import sys
sys.path.append('..')

from model.Process import Process
from model.Memory import Memory
from view.TerminalView import View



class CtrlMemory():

    def startMemory(self):

        def createMemory():
            resultValue = self.view.insertMemValueMessage()

            if resultValue is 0:
               self.view.programFinishMessage()
               exit()

            elif resultValue < 0:
                self.view.errorMessage()
                self.view.tryAgainMessage()
                createMemory()
            else:
                try:
                    Memory.createMemories(self, resultValue)
                    return True
                except Exception as error:
                    print("Memories couldn't be created!")
                    print(error)
                    print("The program will be finished.")
                    exit()

        self.view.programStartMessage()

        if createMemory():
            self.view.successfullyCreatedMemoryMessage()

    def insertPrograms(self):

        def showMemories():
            self.view.showMemoriesChosen()
            allMemoriesList = Memory.memory_List

            for each in allMemoriesList:
                print(each)
                data = each.memory_Data
                print("[ ", end="")
                for step in data:
                    print(step, end=" ")

                print("]", end="")
                print("\n")

            self.view.clickToContinueMessage()

        def createProcess():
            self.view.insertProcessChosen()

            #Returning 'name' and 'size'
            processInfo = self.view.createProcessMessage()

            #Check if dict is not null
            if processInfo != None:
                processName = processInfo['name']
                processSize = processInfo['size']

                allMemoriesList = Memory.memory_List

                newProcess = Process(processName, processSize)

                for each in allMemoriesList:
                    if processSize > each.memory_MaxForProcess:
                        print(each)
                        self.view.notAvailableMemoryMessage()
                        newProcess.deleteProcess()
                        print(newProcess)
                    else:
                        if each.memory_Id == 0:
                            #FirstFit
                            Memory.firstFit(each, newProcess.process_Size, newProcess.process_PID)
                            print("num proc", Process.process_List)
                        elif each.memory_Id == 1:
                            #BestFit
                            Memory.bestFit(each, newProcess.process_Size, newProcess.process_PID)
                        elif each.memory_Id == 2:
                            #WorstFit
                            Memory.worstFit(each, newProcess.process_Size, newProcess.process_PID)
                        else:
                            #CircularFit
                            Memory.circularFit(each, newProcess.process_Size, newProcess.process_PID)


                        #allProcessList = Process.process_List















            self.view.clickToContinueMessage()


        def removeProcess():
            self.view.removeProcessChosen()

            processInfo = self.view.removeProcessMessage()

            #Checks if return is a valid value
            if processInfo != None:
                print(processInfo)







            self.view.clickToContinueMessage()

        def programMenu():
            menuResultOption = self.view.menuMessage()

            if menuResultOption == 0:
                self.view.programFinishMessage()
                exit()
            elif menuResultOption < 0:
                self.view.errorMessage()
                self.view.tryAgainMessage()
                programMenu()
            elif menuResultOption == 1:
                #MOSTRA MEMORIA STUFF
                showMemories()
            elif menuResultOption == 2:
                #INSERE PROCESSO STUFF
                createProcess()
            else:
                #REMOVE PROCESSO STUFF
                removeProcess()
            programMenu()

        programMenu()




    def __init__(self):
        self.view = View()















#def addProc():
#    pass
#Chama classe view
#     View()

"""
    #Cria os processos
    p1 = Process('Spotify', 1024)
    p2 = Process('Chrome', 4098)
    p3 = Process('Minecraft', 52)
    p4 = Process('Mozilla', 234)
    p5 = Process('Windows', 561)
    p6 = Process('Linux', 4241)
    p7 = Process('Eae', 8064)
    p8 = Process('asfasfas', 1022)

    #Salva os processos (conferir se tem espaço na memória)
    #print(p1)
    p1.save()
    #print(p2)
    p2.save()
    #print(p3)
    p3.save()
    #print(p4)
    p4.save()
    #print(p5)
    p5.save()
    #print(p6)
    p6.save()
    #print(p7)
    p7.save()
    #print(p8)
    p8.save()
    """

    #Printa Quantidade de processos criados
    #print("Quantidade de processos: ", Process.process_Num)

#def addMem():

#Cria as memórias do tamanho passado pelo usuário
 #   for i in range(4):
 #       mem = Memory(i, 80)
 #       print(mem)


#  print(Memory.memory_List)
"""
    Printa o vetor de memória
    list = mem.memory_Data
    for each in list:
        print(each, end=" ")
    print(" ")
"""

