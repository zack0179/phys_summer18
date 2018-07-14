# -*- coding: utf-8 -*-
import autopep8


def style_fixer(in_fname, out_fname=None, in_place=False):
    if in_place:
        out_fname = in_fname
    if out_fname is None:
        raise ValueError("out_fname must be set if in_place not True.")

    out = autopep8.fix_file(input_fname)

    out = autopep8.fix_code(out,
                            options={"select": ["E2"]})

    with open(out_fname, "w") as f:
        f.write(out)


if __name__ == "__main__":
    input_fname = r"/home/zack0179/Documents/GIT/fitpack/fitlab/maxlike.py"
    output_fname = r"/home/zack0179/Documents/GIT/fitpack/outputboi.py"

    style_fixer(input_fname, output_fname, in_place=False)
