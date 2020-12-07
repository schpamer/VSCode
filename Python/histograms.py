import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('f16.jpg',0)
#plt.hist(img.ravel(),256,[0,256]); plt.show()

#img = cv2.imread('f16.jpg')
#color = ('b','g','r')
#for i,col in enumerate(color):
#    histr = cv2.calcHist([img],[i],None,[256],[0,256])
#    plt.plot(histr,color = col)
#    plt.xlim([0,256])
#plt.show()

#img = cv2.imread('f16.jpg')
#hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )

#plt.imshow(hist,interpolation = 'nearest')
#plt.show()

img = cv2.imread('f16.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

#plt.subplot(121),plt.imshow(img, cmap = 'gray')
#plt.title('Input Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
#plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
#plt.show()

#rows, cols = img.shape
#crow,ccol = rows//2 , cols//2
#fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
#f_ishift = np.fft.ifftshift(fshift)
#img_back = np.fft.ifft2(f_ishift)
#img_back = np.abs(img_back)

#plt.subplot(131),plt.imshow(img, cmap = 'gray')
#plt.title('Input Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
#plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
#plt.subplot(133),plt.imshow(img_back)
#plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

#plt.show()

img = cv2.imread('f16.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,35,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),5,255,-1)

plt.imshow(img),plt.show()