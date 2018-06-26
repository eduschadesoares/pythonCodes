#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Terminal interface here

class View():

    #ALERT MESSAGES
    def incorrectValueMessage(self):
        print("║")
        print("╠┅▶  Incorrect value")

    def invalidValueMessage(self):
        print("║")
        print("╠┅▶  Invalid value")

    def tryAgainMessage(self):
        print("║")
        print("╠┅▶  Try again!")

    # SUCCESS MESSAGES
    def processSuccessfullyRemoved(self, processPid):
        print("║")
        print("╠┅▶ ✓ Process %s was successfully removed" %(processPid))

    def successfullyCreatedMemoryMessage(self):
        print("║")
        print("╠┅▶ ✓ Memories was successfully created!")

    def successfullyCreatedProcessMessage(self, processName, processPid):
        print("║")
        print("╠┅▶ ✓ Process: \"%s\" - PID: %s was successfully created!" % (processName, processPid))

    # FAIL MESSAGES
    def cancelRemove(self):
        print("║")
        print("╠┅▶ ❎ Remotion is canceled")

    def failedToCreateMemoryMessage(self):
        print("║")
        print("╠┅▶ ❎ Memories couldn't be created!")

    def noProcessesCreated(self):
        print("║")
        print("╠┅▶ ❎ There is no process")

    def notAvailableMemoryMessage(self, memoryName):
        print("╠┅▶ ❎ %12s - Error, not enough available memory to create this process" %(memoryName))

    def processDoesntExist(self, processPID):
        print("║")
        print("╠┅▶ ❎ Process %s doesn't exist" %(processPID))

    def processNotCreatedMessage(self):
        print("║")
        print("╠┅▶ ❎ Process could not be created, no memory available for this size")

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

        print("╠┅▶ ✓ %12s - created in the %s%s position" % (fit, position, suffix))

    def showProcesses(self, process, memories, validate):
        if validate:
            print("║ ╰──◌ PID %s" % process.process_PID)
            print("║    ┝──◐ Name")
            print("║    │  ╰──● %s" % process.process_Name)
            print("║    ┝──◐ Size ")
            print("║    │  ╰──● %s KB" % process.process_Size)
            print("║    ╰──◐ Memory ")
            j = 0
            for key, value in memories.items():
                if j is not len(memories) - 1:
                    print("║       ┝──◑ %s" % key)
                    print("║       │  ╰─● Position: %s" % value)
                else:
                    print("║       ╰──◑ %s" % key)
                    print("║          ╰─● Position: %s" % value)
                j += 1

        else:
            print("║ ┝──◌ PID %s" % process.process_PID)
            print("║ │  ┝──◐ Name")
            print("║ │  │  ╰──● %s" % process.process_Name)
            print("║ │  ┝──◐ Size ")
            print("║ │  │  ╰──● %s KB" % process.process_Size)
            print("║ │  ╰──◐ Memory ")
            j = 0
            for key, value in memories.items():
                if j is not len(memories) - 1:
                    print("║ │     ┝──◑ %s" % key)
                    print("║ │     │  ╰─● Position: %s" % value)
                else:
                    print("║ │     ╰──◑ %s" % value)
                    print("║ │        ╰─● Position: %s" % value)
                j += 1

            print("║ │")


    def showProcessesLessInformation(self, process, validate):
        if validate:
            print("║ ╰──◌ PID: %s - \"%s\"" % (process.process_PID, process.process_Name))
        else:
            print("║ ┝──◌ PID: %s - \"%s\"" %(process.process_PID, process.process_Name))

    #CHOICES
    def insertProcessChosen(self):
        print("║")
        print("╠┅▶ ⌛ Create a process")

    def listProcessChosen(self):
        print("║")
        print("╠┅▶ ⌛ Dysplaying processes")

    def removeProcessChosen(self):
        print("║")
        print("╠┅▶ ⌛ Remove a process")

    def showMemoriesChosen(self):
        print("║")
        print("╠┅▶ ⌛ Displaying memories")

    #BASIC MESSAGES
    def listProcessInformationHeader(self):
        print("║")
        print("╠═╤═┅▶ Process list")
        print("║ │")

    def listProcessLessInformationHeader(self):
        print("║")
        print("╠═╤═┅▶ Process list")
        print("║ │")

    def programFinishMessage(self):
        print("║")
        print("╚┅▶ The program will exit! ㋡")

    def programStartMessage(self):
        print("╔══════════════════════════════════════╗")
        print("║  Initializing the Elefante® program  ║")
        print("╠══════════════════════════════════════╝")
        print("║")

    def showMemoryInformation(self, memory):
        print("║")
        print("╠┅▶  %s" % memory)

    #FORMATED MESSAGES
    def showFormattedMemoryCloseArray(self):
        print("]", end="" "\n\n")

    def showFormattedMemoryOpenArray(self):
        print("[ ", end="")

    def showFormattedMemoryStep(self, step):
        print(step, end=" ")

    #I/O MESSAGES
    def clickToContinueMessage(self):
        print("║")
        print("╠┅▶ ⌨  Press enter to continue", end=" ")
        none = input()

    def confirmRemoveProcess(self, processName, processId):
        yes = ['y', 'yes', 'Yes', 'YEs', 'YES', 'yEs', 'yES', 'yeS']
        no = ['n', 'no', 'No', 'NO']
        print("║")
        print("╠┅▶  Do you really want to remove the process \"%s\" - PID %s?" % (processName, processId))
        print("╠┅▶ ⌨  Type Y/Yes or N/No: ", end="")
        try:
            answer = str(input())
            if answer in yes:
                return True
            if answer in no:
                return False
            else:
                print("║")
                print('╠┅▶ ❎ Invalid answer')
                return False
        except ValueError:
            print("║")
            print('╠┅▶ ❎ Irregular value')
            return False


    def createProcessMessage(self):
        print("║")
        print("╠┅▶ ⌨  Insert the process name:", end="")
        processName = str(input())
        print("╠┅▶ ⌨  Insert the process size:", end="")
        try:
            processSize = int(input())
            if processSize < 1:
                print("║")
                print("╠┅▶ ❎ Invalid value")
                return
        except ValueError:
            print("║")
            print("╠┅▶ ❎ Irregular value")
            return

        #Returns a dict
        processInfo = {
            'name': processName,
            'size': processSize,
        }

        print("║")
        return processInfo

    def insertMemSizeMessage(self):
        print("╠┅▶ ⌨  Insert the memory size (KB). Insert 0 to exit:", end=" ")
        try:
            mem_Size = int(input())
        except ValueError:
            print("╠┅▶ ❎ Irregular value")
            return
        return mem_Size

    def removeProcessMessage(self):
        print("║")
        print("╠┅▶ ⌨  Insert the process ID to remove:", end="")
        try:
            processID = int(input())
            if processID < 1:
                print("╠┅▶ ❎ Invalid value")
                return
        except ValueError:
            print("╠┅▶ ❎ Irregular value")
            return
        return processID

    #MENU
    def menuMessage(self):
        print("║")
        print("║   ╔════════════════════╗")
        print("║   ║        MENU        ║")
        print("║   ╠═══╤════════════════╣")
        print("║   ║ 1 │ Show memories  ║")
        print("║   ╠━━━┿━━━━━━━━━━━━━━━━╣")
        print("║   ║ 2 │ Create process ║")
        print("║   ╠━━━┿━━━━━━━━━━━━━━━━╣")
        print("╠═══╣ 3 │ Remove process ║")
        print("║   ╠━━━┿━━━━━━━━━━━━━━━━╣")
        print("║   ║ 4 │ Show process   ║")
        print("║   ╠━━━┿━━━━━━━━━━━━━━━━╣")
        print("║   ║ 0 │ Exit           ║")
        print("║   ╚═══╧════════════════╝")
        print("║")
        print("╠┅▶ ⌨  Insert an option:", end="")
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
