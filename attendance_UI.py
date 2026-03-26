import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
from face_recognition_module import FaceRecognizer
from attendance_manager import AttendanceManager

class AttendanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("900x700")

        # 1. Initialize YOUR existing logic classes
        self.face_recognizer = FaceRecognizer('images')
        self.attendance = AttendanceManager('attendance.csv')
        self.face_recognizer.load_images()
        self.face_recognizer.encode_faces()

        # 2. Setup the UI Layout
        self.label = tk.Label(root, text="Scan Face for Attendance", font=("Arial", 20))
        self.label.pack(pady=10)

        # Video Frame
        self.video_label = tk.Label(root)
        self.video_label.pack()

        # Status Display
        self.status_var = tk.StringVar(value="System Ready")
        self.status_label = tk.Label(root, textvariable=self.status_var, font=("Arial", 14), fg="blue")
        self.status_label.pack(pady=10)

        # 3. Start Camera
        self.cap = cv2.VideoCapture(0)
        self.update_frame() # Start the loop

    def update_frame(self):
        success, frame = self.cap.read()
        if success:
            # Run YOUR existing recognition logic
            results = self.face_recognizer.recognize_faces(frame)

            for name, faceLoc in results:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4 # Scaling up

                # Draw on the frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

                # Mark Attendance using YOUR manager
                self.attendance.mark_attendance(name)
                self.status_var.set(f"Recognized: {name}")

            # Convert OpenCV frame to Tkinter-compatible image
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img_tk = ImageTk.PhotoImage(image=img)

            # Update the label with the new image
            self.video_label.imgtk = img_tk
            self.video_label.configure(image=img_tk)

        # Re-run this function every 10ms (This replaces 'while True')
        self.root.after(10, self.update_frame)

    def on_close(self):
        self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()