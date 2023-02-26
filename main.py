import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize background subtraction model
fgbg = cv2.createBackgroundSubtractorMOG2()

# Define color for highlighting moving object
highlight_color = (255, 255, 255) # white

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Apply background subtraction to detect moving objects
    fgmask = fgbg.apply(frame)

    # Apply noise reduction and smoothing
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    fgmask = cv2.GaussianBlur(fgmask, (7, 7), 0)

    # Find contours of moving objects
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding box around moving object and display "Object Detected"
    for contour in contours:
        if cv2.contourArea(contour) > 2000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), highlight_color, 2)
            print("Object Detected")

    # Display frame in window
    cv2.imshow('frame', frame)

    # Check for exit key (press 'q' to exit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
