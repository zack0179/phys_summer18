from __future__ import print_function
import os


def yada(path):
    imports = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith(".py"):
                continue
            parent_file = os.path.join(root, file)
            imports[parent_file] = []
            with open(parent_file) as file:
                file_lines = file.readlines()
            extras = []
            while file_lines:
                for line in file_lines:
                    words = line.strip().split()
                    if len(words) < 2:
                        continue
                    if len(words) == 2:
                        first, second = words
                        rest = []
                    else:
                        first, second, rest = words[0], words[1], words[2:]
                    if first == "from":
                        if "as" in rest:
                            edge = " ".join(rest[1:rest.index("as")])
                        elif "#" in rest:
                            edge = " ".join(rest[1:rest.index("#")])
                        else:
                            edge = "".join(rest[1:]).replace(",", ", ")
                        imports[parent_file].append([second, edge])
                    elif first == "import":
                        for module in second.split(","):
                            imports[parent_file].append(module
                                                        .replace(";", "")
                                                        .replace("#", ""))
                    rest = " ".join(rest)
                    if ";" in rest:
                        extras += rest.split(";")[1:]
                file_lines = extras
                extras = []

    # Show your work
#    for key in imports.keys():
#        print(key)
#        for val in imports[key]:
#            if type(val) is list:
#                print("    " + val[0] + ": " + val[1])
#            else:
#                print("    " + val)

    # Consolidate your work
    for key in imports.keys():
        val = [val for val in imports[key]
               if (type(val) is list)]
        trash = []
        for v in val:
            if imports[key].index(v) + 1 < len(imports[key]):
                if imports[key][imports[key].index(v) + 1][0] == v[0]:
                    i = imports[key].index(v) + 1
                    imports[key][i - 1] = [v[0],
                                           v[1] + ", " +
                                           imports[key]
                                           [i][1]]
                    trash.append(i)
        n = 0
        for i in trash:
            del imports[key][i - n]
            n += 1

    # Show your work
    for key in imports.keys():
        print(key)
        for val in imports[key]:
            if type(val) is list:
                print("    " + val[0] + ": " + val[1])
            else:
                print("    " + val)

    return imports


if __name__ == "__main__":
#    path = "/home/zes5027/GIT/fitpack"
    path = r"C:\Users\Aardvark\Documents\GIT\fitpack"
    imports = yada(path)
