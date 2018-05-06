#! env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import pylab as plt
import pandas as pd

# test2.py.for_tox_log
# Date: 2018/03/12
# Filename: for_tox_log 

__author__ = 'tatab'
__date__ = "2018/03/12"


class for_tox_log(object):
    def __init__(self):
        self.__ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.__EXE_PATH = sys.executable
        self.__ENV_PATH = os.path.dirname(self.__EXE_PATH)
        self.__LOG = os.path.join(self.__ENV_PATH, 'log')

    def main(self):
        np.random.seed(100)
        # os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
        plt.subplot(2,1,1)
        log_data = np.random.lognormal(3,1,1000)
        plt.hist(log_data,bins=100, normed=True, align='mid')
        plt.subplot(2,1,2)

        norm_log_data = np.log(log_data)
        std = np.std(norm_log_data)
        ave = np.average(norm_log_data)
        print(std,ave)
        plt.hist(norm_log_data,bins=100, normed=True, align='mid')
        plt.axis('tight')
        plt.show()

        df = pd.DataFrame({'log':log_data,'norm':norm_log_data})
        #df.to_csv('norm_log_result.csv')
        n = 10
        a = np.exp(n)
        result = np.log(a)
        print(result)



        return


if __name__ == '__main__':
    for_tox_log= for_tox_log()
    for_tox_log.main()