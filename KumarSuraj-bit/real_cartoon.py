import cv2 as cv

cam=cv.VideoCapture(0)

while True:
     ret,img=cam.read()

     cv.imshow('real ',img)

     gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

     gray=cv.medianBlur(gray,3)

     edge=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,5)

     new_img=cv.bilateralFilter(img,3,255,255)

     cartoon=cv.bitwise_and(new_img,new_img,mask=edge)

     cv.imshow('cartoon imaged',cartoon)

     if not ret:
        break
     k=cv.waitKey(1)

     if k%256==32:
        break

cam.release()
cv.destroyAllWindows()


              