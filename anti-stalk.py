import cv2
import win32api
import win32con
import time
import os

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open the webcam for capturing video
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # If a face is detected, perform an action (in this case, print a message)
    if len(faces) > 1:
        print("Face detected!")
        
        # time.sleep(0.1)  # Wait for 5 seconds
        os.system("rundll32.exe user32.dll,LockWorkStation")


    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Wait for 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
