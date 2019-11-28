import cv2
from mtcv import histEqualize
from skimage import data
import matplotlib.pyplot as plt

plt.figure("hist")
img_path="E:/project/0000316.jpg"
img=cv2.imread(img_path)
arr=img.flatten()
n, bins, patches = plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='red')
plt.show()

hist=histEqualize(img,space='rgb',clipLimit=2)
arr2=hist.flatten()
n2, bins2, patches2 = plt.hist(arr2, bins=256, normed=1,edgecolor='None',facecolor='red')
plt.show()
cv2.imshow('src',img)
cv2.imshow("hah",hist)
cv2.imwrite("361.jpg",hist)
cv2.waitKey()