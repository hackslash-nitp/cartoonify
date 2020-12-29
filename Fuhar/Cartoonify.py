# Import libraries 
import cv2 
import numpy as np 

# Read image from webcam
cam = cv2.VideoCapture(0)  
while True:
    ret, frame = cam.read()
    if not ret:
        break
    cv2.imshow("Input", frame)
    k = cv2.waitKey(1)
    if k%256==32:              # Press space to capture image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # Grayscaling
        smooth = cv2.medianBlur(gray, 5)        # Smoothening
        edges = cv2.adaptiveThreshold(smooth, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)     # Obtaining edges

        # Cartoonization 
        color = cv2.bilateralFilter(frame, 9, 250, 250) #Smoothening
        cartoon = cv2.bitwise_and(color, color, mask=edges) #Cartoonifying

        # Displaying processed images
        cv2.imshow("Edges", edges) 
        cv2.imshow("Cartoon", cartoon) 
        k = cv2.waitKey(0)
        break

# Termination  
cam.release()
cv2.destroyAllWindows() 
