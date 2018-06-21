# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:06:22 2018

@author: Aardvark
"""

from __future__ import print_function
import os


def shell(path):
    mod_map = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith(".py"):
                continue
            mod_map[os.path.join(root, file)] = {}
    return mod_map

def get_lines(file):
    with open(file) as file:
        file_lines = file.readlines()
    while file_lines:
        for line in file_line:
            return [line if "]



if __name__ == "__main__":


#    path = "/home/zes5027/GIT/fitpack"
    path = r"C:\Users\Aardvark\Documents\GIT\fitpack"
    mod_map = shell(path)