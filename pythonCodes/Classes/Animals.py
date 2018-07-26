#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __str__(self):
        return "{} {}".format(self.name, self.genre)


a = Animal("rodolfo", "masculino")

print(a)
