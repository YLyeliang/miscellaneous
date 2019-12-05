import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import pywt

path="D:\\zmhj_photo\\detection\\img"

cv2.namedWindow("img")
cv2.namedWindow("xfft")
cv2.namedWindow("yfft")

for file in os.listdir(path):
    file=os.path.join(path,file)
    img =cv2.imread(file)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    wt = pywt.Wavelet()
    fimg = np.fft.fft2(gray)

    # fimg = np.fft.fftshift(fimg)
    xfimg = np.log(np.abs(fimg))
    # xpic = np.uint8(xfimg)
    xpic = xfimg

    yfimg = np.angle(fimg)
    ypic = np.uint8(fimg)

    plt.imshow(xpic)
    plt.show()
    cv2.imshow("img",img)
    cv2.imshow("xfft",xpic)
    cv2.imshow("yfft", ypic)
    cv2.waitKey()

