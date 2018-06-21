#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Process:
    process_List = []
    process_Qnt = len(process_List)
    process_PID = 1

    def __init__(self, process_Name, process_Size):
        self.process_Name = process_Name
        self.process_Size = process_Size
        self.process_PID = Process.process_PID
        Process.process_PID += 1
        Process.process_Qnt += 1

    def save(self):
        self.__class__.process_List.append(self)


    def __str__(self):
        return "Processo \"%s\" - PID %s - Tamanho %s" % (self.process_Name, self.process_PID, self.process_Size)


class Memory:
    memory_List = []

    def __init__(self, memory_Id, memory_Size):
        self.memory_Id = memory_Id
        self.memory_Size = memory_Size
        self.memory_Real = []

        for i in range(self.memory_Size):
            self.memory_Real.append(0)

        self.__class__.memory_List.append(self)

   # def save(self):
   #     for i in range(self.memory_Size):
    #        self.memory_Real.append(0)


    def __str__(self):
        return "Memória %s de tamanho %s" % (self.memory_Id, self.memory_Size)



