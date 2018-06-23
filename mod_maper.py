# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:06:22 2018

@author: Aardvark
"""
from __future__ import print_function
import os

# path = r"C:\Users\Aardvark\Documents\GIT\fitpack"


def get_file_tree(path):
    '''takes path retrns {file_path: {}}'''
    file_tree = {}
    for root, dirs, files in os.walk(path):
        keys = [os.path.join(root, file)
                for file in files
                if file.endswith(".py")]
        for key in keys:
            file_tree[key] = {}
    return file_tree

# file_tree = get_file_tree(path)


def get_line_tree(file_tree):
    '''takes dict | keys as file paths,
       returns dict| values = [{first: [second, rest]}, ...
                                for n inports in file] '''
    line_tree = {}
    for key in file_tree.keys():
        with open(key) as file:
            file_lines = file.readlines()
        extras = []
        line_list = []
        while file_lines:
            for line in file_lines:
                items = line.strip().split()
                if len(items) < 2:
                    continue
                if items[0] in ["import", "from"]:
                    if len(items) == 2:
                        first, second = items[0], items[1]
                        rest = []
                    else:
                        first, second, rest = items[0], items[1], items[2:]
                    if "as" in rest:
                        rest = rest[:rest.index("as")]
                    elif "#" in rest:
                        rest = rest[:rest.index("#")]
                    if ";" in rest:
                        extras += rest.split(";")[1:]
                        rest = rest[:rest.index(";")]
                    line_list.append({first: [second, rest]})
            file_lines = extras
            extras = []
        line_tree[key] = line_list
    return line_tree


def get_import_tree(line_tree):
    '''post processing of line_tree'''
    import_tree = {}
    for line_key in line_tree.keys():
        if not line_tree[line_key]:
            import_tree[line_key] = []
            continue
        value = {}
        for dic in line_tree[line_key]:
            for imp_key in dic.keys():
                if imp_key == "import":
                    second, rest = dic[imp_key]
                    if not rest:  # if rest is empty
                        for i in second.split(","):  # "import os,sys"
                            value[i] = []
                    else:  # if rest is not empty
                        value[second.replace(",", "")] = []  # "import os, sys"
                        for i in rest.replace(",", ""):
                            value[i] = []
                elif imp_key == "from":
                    second, rest = dic[imp_key]
                    if len(rest) == 2:
                        imp = []  # initalise for all imports
                        for i in rest[1].split(","):
                            imp.append(i)
                        if second in value.keys():
                            value[second].extend(imp)
                        else:
                            value[second] = imp
                    else:
                        imp = []  # initalise for all
                        for i in rest[1:]:
                            imp.append(i.replace(",", ""))
                        if second in value.keys():
                            value[second].extend(imp)
                        else:
                            value[second] = imp
                import_tree[line_key] = value
    return import_tree


def import_tracker(path):
    file_tree = get_file_tree(path)
    line_tree = get_line_tree(file_tree)
    import_tree = get_import_tree(line_tree)

    #  represent you work
    keys = [key for key in import_tree.keys()]
    keys.sort()
    for k in keys:
        print(k)
        if not import_tree[k]:
            continue
        else:
            for d in import_tree[k].keys():
                if import_tree[k][d] == []:
                    print("    " + d)
                else:
                    print("    " + d + ": " + ",  ".join(import_tree[k][d]))
    return import_tree


if __name__ == "__main__":

    #  path = "/home/zes5027/GIT/fitpack"
    path = r"C:\Users\Aardvark\Documents\GIT\fitpack"
    file_tree = get_file_tree(path)
    line_tree = get_line_tree(file_tree)
    import_tree = get_import_tree(line_tree)






