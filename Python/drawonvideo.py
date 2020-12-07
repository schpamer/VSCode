import cv2


# Call Back functiom rectangle
def draw_rectangle(event,x,y,flags,param):
    
    global pt1,pt2,topLeft_clicked,botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        #r eset
        if topLeft_clicked == True and botRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            botRight_clicked = False

        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True

        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True
# Global varibles
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False

#connect callback


cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)
cap = cv2.VideoCapture(0)


while True:

    ret, frame = cap.read()

    # draw on the frame based off cursor click
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

