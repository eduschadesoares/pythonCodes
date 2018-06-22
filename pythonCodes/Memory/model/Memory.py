#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Memory class here

class Memory:
    memory_List = []

    def __init__(self, memory_Id, memory_Size):
        self.memory_Id = memory_Id
        self.memory_Size = memory_Size
        self.memory_Available = memory_Size
        self.memory_Data = []

        for i in range(self.memory_Size):
            self.memory_Data.append(0)

        self.__class__.memory_List.append(self)

    def __str__(self):
        return "Memória %s de tamanho %s KB. Disponível: %s KB" % (self.memory_Id + 1, self.memory_Size, self.memory_Available)

    def createMemories(self, size):
        for i in range(4):
            mem = Memory(i, size)
            #print(mem) REMOVER DPS



#Métodos addMem, remMem