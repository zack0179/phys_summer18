# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import re


def get_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".py"):
                yield os.path.join(root, file)


def lines_in_file(file_path):
    with open(file_path) as file:
        return file.readlines()


def words_in_line(line):
    return re.findall(r"[\w.]+|#", line)  # |;


def contains_import(words):
    return ("import" in words)


def cut_comment(words):
    return words[:(None if "#" not in words else words.index("#"))]


def cut_as(words):
    return words[:(None if "as" not in words else words.index("as"))]


def gen_import(words):
    if "import" in words:
        for i in words[words.index("import") + 1:]:
            yield i


def parser(words):
    if "from" in words:
        return [words[1], words[3:]]
    else:
        return [[i, []] for i in gen_import(words)]


def find_dependencies(dir_path):
    return {f: map(parser, (filter(
                            contains_import, (cut_as(
                                              cut_comment(words_in_line(line)))
                                              for line in lines_in_file(f)))))
            for f in get_files(dir_path)}





if __name__ == "__main__":
    # dir_path = "/home/zes5027/GIT/fitpack"
    # dir_path = r"C:\Users\Aardvark\Documents\GIT\fitpack"
    dir_path = r"/home/zack0179/Documents/GIT/fitpack"

    ploiu = find_dependencies(dir_path)

   ploiu['/home/zack0179/Documents/GIT/fitpack/fitlab/parman.py'][1]

#  sum(any(";" in x for x in y) and not (print(k)) for k, y in ploiu.items())