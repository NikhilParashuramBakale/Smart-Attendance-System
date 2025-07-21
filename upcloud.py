import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

# Initialize Firebase only once
cred = credentials.Certificate("E:\\Smart-Attendence-System\\iot-smart-attendance-cfd49-firebase-adminsdk-fbsvc-63f16e561b.json")  # <-- use your file name here
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-smart-attendance-cfd49-default-rtdb.firebaseio.com'  # <-- replace with your actual Firebase DB URL
})

def send_attendance_to_firebase(name):
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

# Test the function
if __name__ == "__main__":
    send_attendance_to_firebase("Nihal")
