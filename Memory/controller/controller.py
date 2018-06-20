#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from model.model import Process, Memory
#import view


def addProc():
    p1 = Process('Spotify', 1024)
    p2 = Process('Chrome', 4098)
    p3 = Process('Minecraft', 52)
    p4 = Process('Mozilla', 234)
    p5 = Process('Windows', 561)
    p6 = Process('Linux', 4241)
    p7 = Process('Eae', 8064)
    p8 = Process('asfasfas', 1022)

    #print(p1)
    p1.save()
    #print(p2)
    p2.save()
    #print(p3)
    p3.save()
    #print(p4)
    p4.save()
    #print(p5)
    p5.save()
    #print(p6)
    p6.save()
    #print(p7)
    p7.save()
    #print(p8)
    p8.save()

    print("Quantidade de processos: ", Process.process_Qnt)

def addMem():
    for i in range(4):
        mem = Memory(i, 2048)

    for each in Memory.memory_List:
        print(each)


if __name__ == '__main__':
    addProc()
    addMem()

