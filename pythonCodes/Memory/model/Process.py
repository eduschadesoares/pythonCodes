#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Process class here

class Process:
    process_List = []
    process_Num = 0
    process_PID = 1

    def __init__(self, process_Name, process_Size):
        self.process_Name = process_Name
        self.process_Size = process_Size
        self.process_PID = Process.process_PID
        self.process_Memories = {
            'First Fit'   : False,
            'Best Fit'    : False,
            'Worst Fit'   : False,
            'Circular Fit': False,
        }
        Process.process_PID += 1
        Process.process_Num += 1
        self.__class__.process_List.append(self)

    def memoryAssociated(self):
        inMemory = []
        for key, value in self.process_Memories.items():
            if value:
                inMemory.append(key)
        return inMemory

    def __str__(self):
        return "Process \"%s\" - PID %s - Size %s" % (self.process_Name,
                                                      self.process_PID,
                                                      self.process_Size,
                                                      )
