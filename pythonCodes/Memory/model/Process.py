#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Process class here

class Process:
    process_List = []
    process_Num = len(process_List)
    process_PID = 1

    def __init__(self, process_Name, process_Size):
        self.process_Name = process_Name
        self.process_Size = process_Size
        self.process_PID = Process.process_PID
        Process.process_PID += 1
        Process.process_Num += 1
        self.__class__.process_List.append(self)


    def __str__(self):
        return "Processo \"%s\" - PID %s - Tamanho %s" % (self.process_Name, self.process_PID, self.process_Size)

