import os
from datetime import datetime

class AttendanceManager:
    def __init__(self, file_name="attendance.csv"):
        self.file_name = file_name

    def mark_attendance(self, name):
        # Create file if not exists
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as f:
                f.write("Name,Time\n")

        with open(self.file_name, 'r+') as f:
            data = f.readlines()
            names = [line.split(',')[0] for line in data]

            if name not in names:
                now = datetime.now()
                time_string = now.strftime('%H:%M:%S')
                f.write(f"{name},{time_string}\n")