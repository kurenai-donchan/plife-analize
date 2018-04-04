# -*- coding: utf-8 -*-
# ----------------------------------------------
# python 関数郡
# ----------------------------------------------
import os


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)
