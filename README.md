#  AI Face Recognition Attendance System

An automated attendance solution built with Python that identifies faces in real-time and logs entry times into a CSV database.

###  Key Features
* **Real-time Detection:** Uses a webcam feed to recognize faces instantly.
* **Modern GUI:** Built with Tkinter for a clean, user-friendly dashboard.
* **Smart Logging:** Automatically records name and timestamp in a CSV file.
* **Modular Code:** Separated into Recognition, Manager, and UI modules for easy maintenance.

---

###  Setup & Installation

To get this attendance system running on your local machine, follow these steps:

#### 1. Clone the Repository
```bash
git clone [https://github.com/Tufins/Face-Recognition-Attendance.git](https://github.com/Tufins/Face-Recognition-Attendance.git)
cd Face-Recognition-Attendance
2. Create a Virtual Environment (Recommended)
Bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
3. Install Dependencies
You must have CMake and Visual Studio (C++ Desktop Development) installed on your system to compile the face_recognition library.

Bash
pip install -r requirements.txt
4. Prepare your Database
Place images of people you want to recognize in the images/ folder.

Rename the files to the person's name (e.g., elon_musk.jpg).

Ensure an attendance.csv file exists in the root directory with the header: Name,Time.

           How to Use the UI
Run the application: python attendance_ui.py.

Once the window opens, your webcam will activate.

Position your face in front of the camera.

When a match is found, a green box will appear around your face with your name.

The system will automatically log your name and the current timestamp into attendance.csv.

Click "Exit System" or close the window to stop the camera.

      Tech Stack
Language: Python 3.10+

Computer Vision: OpenCV, face_recognition (dlib)

GUI: Tkinter, Pillow

Data: CSV / NumPy