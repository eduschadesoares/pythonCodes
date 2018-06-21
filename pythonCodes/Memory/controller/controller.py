#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Controller stuff here

import sys
sys.path.append('..')

from model.process import Process
from model.memory import Memory
from view.view import View


def addProc():
    pass
#Chama classe view
#     View()

"""
    #Cria os processos
    p1 = Process('Spotify', 1024)
    p2 = Process('Chrome', 4098)
    p3 = Process('Minecraft', 52)
    p4 = Process('Mozilla', 234)
    p5 = Process('Windows', 561)
    p6 = Process('Linux', 4241)
    p7 = Process('Eae', 8064)
    p8 = Process('asfasfas', 1022)

    #Salva os processos (conferir se tem espaço na memória)
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
    """

    #Printa Quantidade de processos criados
    #print("Quantidade de processos: ", Process.process_Num)

def addMem():

#Cria as memórias do tamanho passado pelo usuário
    for i in range(4):
        mem = Memory(i, 80)
        print(mem)


#  print(Memory.memory_List)
"""
    Printa o vetor de memória
    list = mem.memory_Data
    for each in list:
        print(each, end=" ")
    print(" ")
"""

#Main function
if __name__ == '__main__':
    addProc()
    addMem()
else:
    print("Execute o arquivo controller.py")
