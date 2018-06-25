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

            #Need to put this output to view
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
            allMemoriesList = Memory.memory_List
            self.view.insertProcessChosen()

            #Returning 'name' and 'size'
            processInfo = self.view.createProcessMessage()

            #Check if dict is not null
            if processInfo != None:
                processName = processInfo['name']
                processSize = processInfo['size']

                counter = 0
                for each in allMemoriesList:
                    if processSize <= each.memory_MaxForProcess:
                        counter += 1

                if counter > 0:
                    newProcess = Process(processName, processSize)

                    for each in allMemoriesList:
                        if processSize > each.memory_MaxForProcess:
                            #print(each) Criar view depois
                            self.view.notAvailableMemoryMessage(each.memoryName())
                        else:
                            if each.memory_Id == 0:
                                #FirstFit
                                content = Memory.firstFit(each, newProcess.process_Size, newProcess.process_PID)
                                newProcess.process_Memories['firstFit'] = True
                                self.view.showFitPosition(content['fit'], content['position'])
                            elif each.memory_Id == 1:
                                #BestFit
                                content = Memory.bestFit(each, newProcess.process_Size, newProcess.process_PID)
                                newProcess.process_Memories['bestFit'] = True
                                self.view.showFitPosition(content['fit'], content['position'])
                            elif each.memory_Id == 2:
                                #WorstFit
                                content = Memory.worstFit(each, newProcess.process_Size, newProcess.process_PID)
                                newProcess.process_Memories['worstFit'] = True
                                self.view.showFitPosition(content['fit'], content['position'])
                            else:
                                #CircularFit
                                content = Memory.circularFit(each, newProcess.process_Size, newProcess.process_PID)
                                newProcess.process_Memories['circularFit'] = True
                                self.view.showFitPosition(content['fit'], content['position'])
                else:
                    self.view.processNotCreatedMessage()

            self.view.clickToContinueMessage()


        def listProcess():
            self.view.listProcessChosen()
            allProcessList = Process.process_List
            for each in allProcessList:
                print(each) #Create view
            self.view.clickToContinueMessage()

        def removeProcess():
            self.view.removeProcessChosen()

            allProcessList = Process.process_List

            if not allProcessList:
                self.view.noProcessesCreated()
                self.view.clickToContinueMessage()
                return

            processId = self.view.removeProcessMessage()

            for each in allProcessList:
                if each.process_PID is processId:
                    try:
                        allMemoriesList = Memory.memory_List

                        for each2 in allMemoriesList:
                            each2.removeProcessFromMemory(processId)

                        allProcessList.remove(each)
                        self.view.processSuccessfullyRemoved(processId)
                        return
                    except Exception as error:
                        print(error)

            self.view.processDoesntExist(processId)
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
            elif menuResultOption == 3:
                #REMOVE PROCESSO STUFF
                removeProcess()
            else:
                listProcess()
            programMenu()

        programMenu()


    #Inicializa objeto view
    def __init__(self):
        self.view = View()
