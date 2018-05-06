import cv2
import pylab as plt
import numpy as np
from matplotlib.font_manager import FontProperties

def dif_pic():
    im = cv2.imread("C:\\Users\\tatab\\OneDrive\\NLP\\pic1.jpg")
    im_Lab = cv2.cvtColor(im, cv2.COLOR_BGR2Lab)
    im_L =  im_Lab[:,:,0]
    im_L = cv2.GaussianBlur(im_L, ksize=(5, 5), sigmaX=1.3)
    mask = im_L< 30
    im_Lab[mask]=(0,0,0)
    im =  im_Lab[:,:,1]
    lookUpTable = np.zeros((256, 1), dtype='uint8')
    for i in range(256):
        if i<40:
            lookUpTable[i][0] = 0
        else:
            lookUpTable[i][0] =  np.exp(i/50+2.3)
    im = cv2.LUT(im, lookUpTable)
    cv2.imwrite('U.jpg',im)
    plt.imshow(im,cmap='gray', interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()
def calc_log():
    x =np.arange(-4,3,0.1)
    y = 127/(np.log(127)+x)
    plt.plot(x,y)
    print(np.exp(127/40+1.69))
    plt.show()


def pic_curve():
    x = np.arange(0,255,1)
    y = np.exp(x/30)
    y2 = x
    plt.plot(x,y)
    plt.plot(x,y2)
    plt.ylim(0,255)
    plt.xlim(0,255)
    fp = FontProperties(fname='C:\\WINDOWS\\Fonts\\msgothic.ttc', size=22)
    plt.legend(['補正関数','元の分布'],prop=fp)

    plt.show()

def pic_hist(im):
    im_Lab = cv2.cvtColor(im, cv2.COLOR_BGR2Lab)
    im_L =  im_Lab[:,:,0]
    im_L = cv2.GaussianBlur(im_L, ksize=(5, 5), sigmaX=1.3)
    # plt.hist(im_L.flatten(),bins=51)
    # plt.show()
    mask = im_L< 30
    im_Lab[mask]=(0,0,0)
    im =  im_Lab[:,:,1]
    #im = cv2.equalizeHist(im)
    # im = np.hstack((im, equ))

    lookUpTable = np.zeros((256, 1), dtype='uint8')
    for i in range(256):
        if i<50:
            lookUpTable[i][0] = 0
        else:
            #j = i - i % 2
            j=i
            #lookUpTable[i][0] = 600 * pow(float(j) / 255, 2.9)
            lookUpTable[i][0] =  np.exp(i/30)

    im = cv2.LUT(im, lookUpTable)
    return im

if __name__ == '__main__':
    #dif_pic()
    #calc_log()
    # im = cv2.imread("C:\\Users\\tatab\\OneDrive\\NLP\\pic1.jpg")
    # im = pic_hist(im)
    #
    # im2 = cv2.imread("C:\\Users\\tatab\\OneDrive\\NLP\\pic2.jpg")
    # im2 = pic_hist(im2)
    # fp = FontProperties(fname='C:\\WINDOWS\\Fonts\\msgothic.ttc', size=25)
    #
    # plt.hist(im.flatten(),  bins=50,alpha=0.3,normed=True,color='r')
    # plt.hist(im2.flatten(),bins=50, alpha=0.3,normed=True,color='b')
    # plt.ylim(0,0.025)
    # plt.xlim(5,255)
    # plt.legend(['処理前','処理後'],prop=fp)
    # plt.show()
    pic_curve()