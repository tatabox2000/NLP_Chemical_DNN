#! env python
# -*- coding: utf-8 -*-

import os
import sys

# NLP.spark_test
# Date: 2018/02/16
# Filename: spark_test 

__author__ = 'tatab'
__date__ = "2018/02/16"

class spark_test(object):
    def __init__(self):
        self.__ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.__EXE_PATH = sys.executable
        self.__ENV_PATH = os.path.dirname(self.__EXE_PATH)
        self.__LOG = os.path.join(self.__ENV_PATH, 'log')

    def main():
        os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
        return


if __name__ == '__main__':
    main()
