#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from connection import Connection

class Data:
    def __init__(self):
        self.connection = Connection()
