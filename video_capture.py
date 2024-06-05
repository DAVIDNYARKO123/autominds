import cv2

# Open a connection to the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # If frame is read correctly ret is True
    if not ret:
        print("Failed to grab frame")
        break
    
    # Display the resulting frame
    cv2.imshow('Video Stream', frame)
    
    # Press 'q' to break the loop and stop the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
