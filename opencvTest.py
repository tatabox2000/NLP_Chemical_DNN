#! env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image
import os
import sys
# NLP.opencvTest
# Date: 2018/05/06
# Filename: opencvTest

__author__ = 'tatab'
__date__ = "2018/05/06"


class opencvTest(object):
    def __init__(self):
        self.__ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.__EXE_PATH = sys.executable
        self.__ENV_PATH = os.path.dirname(self.__EXE_PATH)
        self.__LOG = os.path.join(self.__ENV_PATH, 'log')

    def main(self,DIR):
        os.chdir(DIR)
        CV_im = cv2.imread("lena.jpg")
        PIL_im = np.array(Image.open("lena.jpg"))
        # BGRからRGBへ変換
        CV_im_RGB = CV_im[:, :, ::-1].copy()

        # 変換
        PIL2CV = np.asarray(PIL_im)
        CV2PIL = Image.fromarray(CV_im)
        CV2PIL_normalize = Image.fromarray(CV_im_RGB)

        # 描画
        plt.subplot(1, 3, 1), plt.imshow(PIL2CV)
        plt.title(u"PIL⇒CV")
        plt.subplot(1, 3, 2), plt.imshow(CV2PIL)
        plt.title(u"CV(BGR)⇒PIL")
        plt.subplot(1, 3, 3), plt.imshow(CV2PIL_normalize)
        plt.title(u"CV(RGB⇒PIL")
        plt.show()

if __name__ == '__main__':
    DIR = "C:\\googledrive\\Data\\ComputerVision"
    test = opencvTest()
    test.main(DIR)