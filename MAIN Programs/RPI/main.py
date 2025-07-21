import requests
import time
import config
from datetime import datetime
from camera import capture_image
from face_recognition import recognize_face
from oled_display import display_message, display_idle, display_success, display_no_control
from ir_sensor import is_triggered
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

cred = credentials.Certificate("E:\\IOT\\iot-smart-attendance-cfd49-firebase-adminsdk-fbsvc-63f16e561b.json")  # <-- use your file name here
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-smart-attendance-cfd49-default-rtdb.firebaseio.com'  # <-- replace with your actual Firebase DB URL
})
def get_system_status():
    """Check if the system should be active based on PC control."""
    try:
        resp = requests.get(config.SERVER_CONTROL_URL, timeout=5)
        return resp.text.strip().lower() == "on"
    except:
        return False

def send_attendance(name):
    """Send attendance data to Flask app on PC."""
    # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # try:
    #     response = requests.post("http://192.168.66.182:5000/submit_attendance", json={
    #         "name": name,
    #         "timestamp": timestamp
    #     }, timeout=5)
    #     if response.ok:
    #         print(f"Attendance sent: {name}, {timestamp}")
    #     else:
    #         print(f"Failed to send attendance: {response.status_code}")
    # except Exception as e:
    #     print(f"Error sending attendance: {e}")
    timestamp = datetime.now()
    date_str = timestamp.strftime("%Y-%m-%d")
    time_str = timestamp.strftime("%H:%M:%S")

    if name.strip().lower() == "unknown":
        return

    ref = db.reference(f'attendance/{date_str}/{name}')
    ref.set({
        'status': 'P',
        'time': time_str
    })

    print(f"Firebase updated for {name} at {time_str}")

if __name__ == "__main__":
    print("Smart Attendance System Started")
    display_message("Smart Attendance", "Starting...")

    while True:
        system_on = get_system_status()

        if not system_on:
            display_no_control()
            time.sleep(2)
            continue

        display_idle()
        if is_triggered():
            path = capture_image()
            name = recognize_face(path)
            send_attendance(name)
            display_success(name)
            time.sleep(3)  # Debounce delay
