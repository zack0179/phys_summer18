# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import re


def get_files(dir_path, specifics=None):
    # names in specifics will be included, additionally
    if specifics is None:
        specifics = set()
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".py") or file in specifics:
                yield os.path.join(root, file)


def lines_in_file(file_path):
    with open(file_path) as file:
        return file.readlines()


def words_in_line(line):
    return re.findall(r"[\w.]+|#", line)  # XXX: note that ';' is not treated


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
        return [[words[1], words[3:]]]
    else:
        return [[i, []] for i in gen_import(words)]


def find_dependencies(dir_path, specifics=None):
    return {
        f.replace(dir_path, ""):
            reduce(list.__add__,
                   map(parser,
                       filter(contains_import,
                              (cut_as(cut_comment(words_in_line(line)))
                               for line in lines_in_file(f)))), [])
            for f in get_files(dir_path, specifics)}


if __name__ == "__main__":
    dir_path = r"/home/mda5232/git/fitpack"

    deps = find_dependencies(dir_path, {"jam3d", "mcproc", "run_notebook"})
