# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 18:33:00 2018

@author: Tiffany
"""
from __future__ import print_function
import os

os.chdir("C:\\Users\\Aardvark\\Documents\\Py\\phys_summer")
path = "C:\\Users\\Aardvark\\Documents\\GIT\\fitpack"

fitpack_track = {}
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".py"):
            parent_file = os.path.join(root, file)
            target_dependence = []
            for line in open(parent_file):
                if "from" in line.split():
                    marks = line.split()[1]
                    if "," in marks:
                        for x in marks.split(","):
                            target_dependence.append(x)
                    else:
                        target_dependence.append(marks)
                elif "import" in line.split() and "from" not in line.split():
                    marks = line.split()[1]
                    if "," in marks:
                        for x in marks.split(","):
                            target_dependence.append(x)
                    else:
                        target_dependence.append(marks)
            fitpack_track[parent_file] = target_dependence
