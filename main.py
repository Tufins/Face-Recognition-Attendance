import cv2
from face_recognition_module import FaceRecognizer
from attendance_manager import AttendanceManager

# Initialize objects
face_recognizer = FaceRecognizer('images')
attendance = AttendanceManager('attendance.csv')

# Load and encode
face_recognizer.load_images()
face_recognizer.encode_faces()

print("System Ready")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    results = face_recognizer.recognize_faces(frame)

    for name, faceLoc in results:
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.putText(frame,name,(x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.75,(255,255,255),2)

        attendance.mark_attendance(name)

    cv2.imshow('Attendance System', frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()