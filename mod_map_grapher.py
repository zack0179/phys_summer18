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

dir_path = r"/home/mda5232/git/fitpack"

exclude = {"examples"}
ignore = {"argparse", "collections", "cPickle", "fnmatch", "numba", "numpy",
          "os", "pandas", "pickle", "psutil", "pylab", "re", "scipy", "sys",
          "timeit", "warnings", "zlib", "zmq"}

deps = find_dependencies(dir_path, {"jam3d", "mcproc", "run_notebook"})

mods = [k.split("/")[-1].split(".")[0] for k in deps.keys()]

ambigs = {k: v for k, v in Counter(mods).items() if v > 1}

G = nx.DiGraph()

for f, imports in deps.items():
    parts = f.split("/")[1:]
    parts[-1] = parts[-1].split(".")[0]
    f = ".".join(parts)
    for big, smalls in imports:
        if not (ignore & set(big.split("."))):
            G.add_edge(f, big, info=smalls)


def plot(node_color=DEFAULT_NODE_COLOR,
         edge_color=DEFAULT_EDGE_COLOR,
         font_color=DEFAULT_FONT_COLOR):
    fig, ax = plt.subplots(figsize=(8, 6))

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
    print(sorted(G.nodes))

    # fig, ax = plot()
