import cv2
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

#Variables
drawing = False
ix = -1
iy = -1

#Function
def draw_rectangle(event,x,y,flags,params):

    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix, iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,255,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(255,255,0),-1)

#Show the image

#black
#img = np.ones((512,512,3))

img = cv2.imread('sammy.jpg')

cv2.namedWindow(winname = "my_drawing")
cv2.setMouseCallback("my_drawing",draw_rectangle)

while True:

    cv2.imshow("my_drawing", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

#full = cv2.imread('sammy.jpg')
#full = cv2.cvtColor(full,cv2.COLOR_BGR2RGB)

#plt.imshow(full) #need this to 'load' the image
#plt.show()       #need this to display the image
#print(full.shape)