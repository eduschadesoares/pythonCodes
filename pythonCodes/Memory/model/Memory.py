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
        for i in range(self.memory_Size):
            if self.memory_Data[i] is not 0:
                self.memory_Available -= 1


    def firstFit(self, pid):
        print(pid)


