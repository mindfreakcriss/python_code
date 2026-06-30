# -*- coding: utf-8 -*-

from language.python import python
from windows import Windows
from datetime import date
from log import Log
from file import File
from list import List
import json

if __name__ == "__main__":
    dir = List(".")
    files = dir.listdir()
    print(files)
    dump = json.dumps(files)