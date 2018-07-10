#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Tree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.counter = 1

    def __str__(self):
        return "%s" % self.data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
            else:
                self.counter += 1
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        # print(self.data, self.counter)
        print(self.data)
        if self.right:
            self.right.printTree()



# root = Tree(12)
# root.insert(9)
# root.insert(13)
# root.insert(12)
# root.insert(4)
# root.printTree()