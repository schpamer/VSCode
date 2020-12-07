import cv2


# Call Back functiom rectangle
def draw_circle(event,x,y,flags,param):
    
    global center,clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        #r eset
        if clicked == True:
            center = (0,0)
            clicked = False
            
        if clicked == False:
            center = (x,y)
            clicked = True

       
# Global varibles
center = (0,0)
clicked = False

#connect callback
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_circle)


while True:

    ret, frame = cap.read()

    # draw on the frame based off cursor click
    if clicked:
        cv2.circle(frame,center=center,radius=50,color=(255,0,),thickness=1)
        cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
    #if cv2.waitKey(1) & 0xFF == 8:
        break

# Shut it down cleam
cap.release()
cv2.destroyAllWindows()