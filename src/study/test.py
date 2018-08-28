# -*- coding: utf-8 -*-
# ----------------------------------------------
# Test
# ----------------------------------------------

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import functions

def main():
    functions.touch("test.txt")
    print("test")


main()
