#! env python
# -*- coding: utf-8 -*-
import numpy
import os
import sys
import tensorflow as tf

# NLP.cluster_count
# Date: 2018/01/25
# Filename: cluster_count 

__author__ = 'tatab'
__date__ = "2018/01/25"


class cluster_count(object):
    def __init__(self):
        self.__ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.__EXE_PATH = sys.executable
        self.__ENV_PATH = os.path.dirname(self.__EXE_PATH)
        self.__LOG = os.path.join(self.__ENV_PATH, 'log')
        return
    def main(self,dir):
        dirs = os.listdir(dir)
        values = {}
        for pic_dir in dirs:
            pic_dir2 = os.path.join(dir,pic_dir)
            if os.path.isdir(pic_dir2)==True:
                files = os.listdir(pic_dir2)
                values.update({pic_dir:len(files)})
        for k, v in sorted(values.items(), key=lambda x: x[1], reverse=True):
            print(k,v)
if __name__ == '__main__':
    dir = u"C:\\Users\\tatab\OneDrive\\NLP\\0.75cut Louvan clustering\\pics"
    cluster_count = cluster_count()
    cluster_count.main(dir)