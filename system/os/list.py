# -*- utf-8 -*-

import os;

class List:
    def __init__(self, items):
        self.items = items

    def listdir(self):
        return os.listdir(self.items)