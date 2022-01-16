#!/usr/bin/env python

import numpy as np
import argparse
import pymatgen.core as mg

class LennardJones():
    def __init__(self, a: float):
        lattice = mg.Lattice.cubic(a)


if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
