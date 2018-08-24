# -*- coding: utf-8 -*-
from __future__ import print_function
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx
from mod_mapper import find_dependencies

DEFAULT_NODE_COLOR = "#0e1b3a"
DEFAULT_EDGE_COLOR = "#000102"
DEFAULT_FONT_COLOR = "#b9cdfb"
DEFAULT_FIG_COLOR = "#2e4272"

dir_path = r"/home/mason/dev/fitpack"

ignore = {"argparse", "collections", "cPickle", "fnmatch", "numba", "numpy",
          "os", "pandas", "pickle", "psutil", "pylab", "re", "scipy", "sys",
          "timeit", "warnings", "zlib", "zmq"}

deps = find_dependencies(dir_path, {"jam3d", "mcproc", "run_notebook"})

deps = {f[1:].replace(".py", "").replace("/", "."): imports
        for f, imports in deps.items()}

mods = [k.split(".")[-1] for k in deps.keys()]

ambigs = {k: v for k, v in Counter(mods).items() if v > 1}

mods = set(mods)

G = nx.DiGraph()

dep_ups = {".".join(x.split(".")[:-1]) for x in deps if "." in x}

for f, imports in deps.items():
    for big, smalls in imports:
        if (ignore & set(big.split("."))):
            continue

        f_parts = f.split(".")

        while f_parts:
            if big in deps or big in dep_ups:
                break
            big = f_parts.pop() + big
        else:
            continue

        if smalls and smalls[0] in mods:
            for small in smalls:
                G.add_edge(f, big + "." + small)
        else:
            G.add_edge(f, big)


def plot(node_color=DEFAULT_NODE_COLOR,
         edge_color=DEFAULT_EDGE_COLOR,
         font_color=DEFAULT_FONT_COLOR):
    fig, ax = plt.subplots(figsize=(16, 12))

    nx.draw_kamada_kawai(G,
                         with_labels=True,
                         ax=ax,
                         node_color=node_color,
                         edge_color=edge_color,
                         font_color=font_color
                         )

    fig.set_facecolor(DEFAULT_FIG_COLOR)

    fig.tight_layout()

    return fig, ax


if __name__ == "__main__":
    print("ins")
    print("=======")

    ins = dict(G.in_degree)

    for node in sorted(ins, key=ins.get):
        print(node, ":", ins[node])

    print()
    print("outs")
    print("=======")

    outs = dict(G.out_degree)

    for node in sorted(outs, key=outs.get):
        print(node, ":", outs[node])

    # fig, ax = plot()
