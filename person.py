import cv2
from alerts import alert

timestamp = ""

def humanSearch(**k):
    log = False
    if(len(k) > 0):
        if(k[0] == True):
            log = True
        else:
            log = False

    # Load pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Define color and font for display
    text_color = (255, 255, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Keep track of whether a face has been detected
    face_detected = False

    #last seen human
    timestamp = ""

    while True:
        # Read frame from webcam
        ret, frame = cap.read()

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw squares around the detected faces and display "Human Detected" once
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Human Detected", (x, y-10), font, 0.5, text_color, 2, cv2.LINE_AA)
            timestamp = alert.TIMESTAMP()
            # if not face_detected:
            #     face_detected = True
        print("Last seen person | " + timestamp)
        # Display frame in window
        cv2.imshow('frame', frame)

        # Check for exit key (press 'q' to exit)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

humanSearch()