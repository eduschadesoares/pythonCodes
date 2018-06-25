#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Terminal interface here

class View():

    #ALERT MESSAGES
    def incorrectValueMessage(self):
        print("Incorrect value")

    def invalidValueMessage(self):
        print("Invalid value")

    def processCreatedMessage(self):
        print("")

    def tryAgainMessage(self):
        print("Try again!")

    # SUCCESS MESSAGES
    def processSuccessfullyRemoved(self, processPid):
        print("Process %s was successfully removed" %(processPid))

    def successfullyCreatedMemoryMessage(self):
        print("Memories was successfully created!")

    # FAIL MESSAGES
    def failedToCreateMemoryMessage(self):
        print("Memories couldn't be created!")

    def noProcessesCreated(self):
        print("There is no process")

    def notAvailableMemoryMessage(self, memoryName):
        print(" %12s - Error, not enough available memory to create this process" %(memoryName))

    def processDoesntExist(self, processPID):
        print("Process %s doesn't exist" %(processPID))

    def processNotCreatedMessage(self):
        print("Process could not be created, no memory available for this size")

    # DISPLAY INFORMATION MESSAGES
    def showFitPosition(self, fit, position):
        if position is 1 or (position % 10) is 1:
            suffix = 'st'
        elif position is 2 or (position % 10) is 2:
            suffix = 'nd'
        elif position is 3 or (position % 10) is 3:
            suffix = 'rd'
        else:
            suffix = 'th'

        print(" %12s - created in the %s%s position" % (fit, position, suffix))

    def showProcesses(self, process, memories):
        inMemory = []
        for key, value in memories.items():
            if value:
                inMemory.append(key)

        print(process, " is in ", end="")
        for i in inMemory:
            print("%s - " %i, end="")
        print("")

    #CHOICES
    def insertProcessChosen(self):
        print("Create a process")

    def listProcessChosen(self):
        print("Dysplaying processes")

    def removeProcessChosen(self):
        print("Remove a process")

    def showMemoriesChosen(self):
        print("Displaying memories")

    #BASIC MESSAGES
    def programFinishMessage(self):
        print("The program will exit!")

    def programStartMessage(self):
        print("Initializing the \"Elefante\" program")

    def showMemoryInformation(self, memory):
        print(memory)

    #FORMATED MESSAGES
    def showFormattedMemoryCloseArray(self):
        print("]", end="" "\n")

    def showFormattedMemoryOpenArray(self):
        print("[ ", end="")

    def showFormattedMemoryStep(self, step):
        print(step, end=" ")

    #I/O MESSAGES
    def clickToContinueMessage(self):
        print("Press enter to continue")
        none = input()

    def createProcessMessage(self):
        print("Insert the process name:", end="")
        processName = str(input())
        print("Insert the process size:", end="")
        try:
            processSize = int(input())
            if processSize < 1:
                print("Invalid value")
                return
        except ValueError:
            print("Irregular value")
            return

        #Returns a dict
        processInfo = {
            'name': processName,
            'size': processSize,
        }

        return processInfo

    def insertMemSizeMessage(self):
        print("Insert the memory size (KB). Insert 0 to exit:", end=" ")
        try:
            mem_Size = int(input())
        except ValueError:
            print("Irregular value")
            return
        return mem_Size

    def removeProcessMessage(self):
        print("Insert the process ID:", end="")
        try:
            processID = int(input())
            if processID < 1:
                print("Invalid value")
                return
        except ValueError:
            print("Irregular value")
            return
        return processID

    #MENU
    def menuMessage(self):
        print("")
        print(" MENU")
        print(" 1 - Show Memories")
        print(" 2 - Create Process")
        print(" 3 - Remove Process")
        print(" 4 - Show Process")
        print(" 0 - Exit")
        print("Insert an option:", end="")
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
        except ValueError:
            return -1
