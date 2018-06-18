# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 18:33:00 2018

@author: Tiffany
"""
from __future__ import print_function
import os
import numpy as np


if __name__ == "__main__":
    os.chdir("/home/zes5027/GIT/phys_summer18")
    path = "/home/zes5027/GIT/fitpack"
    
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
    
    # Save
    np.save('fitpack_track.npy', fitpack_track) 
    
