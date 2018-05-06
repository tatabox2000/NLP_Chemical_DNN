#! env python
# -*- coding: utf-8 -*-
import numpy as np
import os
import sys
import tensorflow as tf
import pylab as plt

# NLP.tensorflow_test
# Date: 2018/01/22
# Filename: tensorflow_test 

__author__ = 'tatab'
__date__ = "2018/01/22"

class tensorflow_test(object):
    def __init__(self):
        self.__ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.__EXE_PATH = sys.executable
        self.__ENV_PATH = os.path.dirname(self.__EXE_PATH)
        self.__LOG = os.path.join(self.__ENV_PATH, 'log')
        return

    def main(self):
        os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
        x = np.arange(1,10,1)
        y = 5*x +2

        dim = 4
        x = tf.placeholder(tf.float32, [None, dim + 1])
        w = tf.Variable(tf.zeros([dim + 1, 1]))
        y = tf.matmul(x, w)
        t = tf.placeholder(tf.float32, [None, 1])
        loss = tf.reduce_sum(tf.square(y - t))
        train_step = tf.train.AdamOptimizer().minimize(loss)

        sess = tf.Session()
        sess.run(tf.global_variables_initializer())




        #plt.plot(x,y)
        #plt.show()

if __name__ == '__main__':
    tensorflow_test= tensorflow_test()
    tensorflow_test.main()