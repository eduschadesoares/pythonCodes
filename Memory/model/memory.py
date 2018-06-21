#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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



