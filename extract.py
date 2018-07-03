# -*- coding: utf-8 -*-

words = [['from', 'mpmath', 'import', 'fp', 'mp'],
         ['import', 'sys', 'os']]


def gen_import(words):
    if "import" in words:
        for i in words[words.index("import") + 1:]:
            yield i


def parser(words):
    if "from" in words:
        return [words[1], words[3:]]
    else:
        return [i for i in gen_import(words)]

parser(words[1])