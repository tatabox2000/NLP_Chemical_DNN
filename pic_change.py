import cv2
import pylab as plt
import numpy as np

def dif_pic():
    im = cv2.imread("C:\\Users\\tatab\\OneDrive\\NLP\\pic1.jpg")
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
    x = np.arange(0,255,1)

    y = np.exp(x/30)
    y2 = x
    plt.plot(x,y)
    plt.plot(x,y2)
    plt.ylim(0,255)
    plt.xlim(0,255)
    plt.show()

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
    cv2.imwrite('U.jpg',im)

    #print(np.average(im))
    plt.imshow(im,cmap='gray', interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()

    # im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # laplacian = cv2.Laplacian(im, cv2.CV_64F)
    # sobelx = cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize=5)
    # sobely = cv2.Sobel(im, cv2.CV_64F, 0, 1, ksize=5)
    #
    # plt.subplot(2, 2, 1), plt.imshow(im, cmap='gray')
    # plt.title('Original'), plt.xticks([]), plt.yticks([])
    # plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    # plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    # plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    # plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    # plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    # plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == '__main__':
    dif_pic()