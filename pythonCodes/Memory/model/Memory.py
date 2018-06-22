#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

#Memory class here

class Memory:
    memory_List = []

    def __init__(self, memory_Id, memory_Size):
        self.memory_Id = memory_Id
        self.memory_Size = memory_Size
        self.memory_Available = memory_Size
        self.memory_MaxForProcess = 0
        self.memory_Data = []

        for i in range(self.memory_Size):
            n = randint(0, 1)
            self.memory_Data.append(n)

        self.__class__.memory_List.append(self)

    def __str__(self):
        if self.memory_Id == 0:
            fitType = 'First Fit'
        elif self.memory_Id == 1:
            fitType = 'Best Fit'
        elif self.memory_Id == 2:
            fitType = 'Worst Fit'
        elif self.memory_Id == 3:
            fitType = 'Circular Fit'    

        return "(%s) - Memória %s de tamanho %s KB. Disponível: %s KB" % (fitType, self.memory_Id + 1, self.memory_Size, self.memory_Available)

    def createMemories(self, size):
        for i in range(4):
            mem = Memory(i, size)
            mem.verifyAvailableSpace()
            #print(mem) REMOVER DPS

    #Just some tests here
    def verifyAvailableSpace(self):
        counter, maxSize = 0,0
        for i in range(self.memory_Size):
            if self.memory_Data[i] is not 0:
                self.memory_Available -= 1

        for i in range(self.memory_Size):
            if self.memory_Data[i] is 0:
                counter += 1
                if counter > self.memory_MaxForProcess:
                    self.memory_MaxForProcess = counter
            else:
                counter = 0

    def firstFit(self, size, pid):
        aux, counter, final, initial = 1, 0, 0, 0

        for i in range(self.memory_Size):
            if self.memory_Data[i] is 0:
                if counter is 0:
                    initial = i
                counter += 1
            else:
                initial = 0
                counter = 0
            if counter is size:
                final = i
                print("ini", initial)
                print("fin", final)
                print("First on ", initial + 1)
                break


       # print(pid)
#





    def bestFit(self, size, pid):
        pass

    def worstFit(self, size, pid):
        pass

    def circularFit(self, size, pid):
        pass

