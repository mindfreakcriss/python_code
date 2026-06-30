# -*- utf-8 -*-

class File:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as file:
            return file.read()

    def write(self, content):
        with open(self.path, 'w') as file:
            file.write(content)
    
    def read_lines(self):
        with open(self.path, 'r') as file:
            return file.readlines()