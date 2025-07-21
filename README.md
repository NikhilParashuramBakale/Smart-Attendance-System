# Smart-Attendence-System
# 🎓 Smart Attendance System

A comprehensive IoT-based attendance tracking system using Raspberry Pi, Firebase, and Flask web application with facial recognition capabilities.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)

## 🌟 Overview

The Smart Attendance System is an automated solution that combines facial recognition, IR sensors, and cloud connectivity to track student attendance in real-time. The system features a Raspberry Pi-based detection unit and a comprehensive web dashboard for monitoring and management.

### Key Components:
- **Raspberry Pi Unit**: Handles face detection, recognition, and sensor input
- **Web Dashboard**: Flask-based admin panel for monitoring and reports
- **Firebase Integration**: Real-time cloud database for attendance data
- **Analytics Dashboard**: Visual charts and comprehensive reporting

## ✨ Features

### Hardware Features
- 🔍 **Facial Recognition**: Automated student identification using dlib
- 📷 **USB Camera Integration**: Real-time image capture
- 🚥 **IR Sensor Trigger**: Motion detection for attendance activation
- 📺 **OLED Display**: Real-time status and feedback display
- ☁️ **Cloud Connectivity**: Firebase real-time database integration

### Web Dashboard Features
- 🎛️ **Master Control Panel**: Remote system on/off control
- 👥 **Student Management**: Individual student profiles and statistics
- 📊 **Analytics Dashboard**: Multiple chart types and visualizations
- 📈 **Comprehensive Reports**: Monthly, daily, and individual student reports
- 📑 **PDF Export**: Generate downloadable attendance reports
- 🔐 **Secure Authentication**: Admin login system

### Analytics & Reporting
- 📊 **Attendance Trends**: Line charts showing attendance patterns
- 📈 **Daily Counts**: Bar charts of daily student attendance
- 🏆 **Student Comparison**: Top and bottom performers analysis
- 📅 **Weekday Analysis**: Attendance patterns by day of week

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Raspberry Pi  │    │    Firebase     │    │   PC/Web App    │
│                 │    │   Database      │    │                 │
│ • Face Recognition◄─────► Real-time DB ◄─────► Flask Dashboard │
│ • Camera Module │    │                 │    │ • Analytics     │
│ • IR Sensor     │    │ • Attendance    │    │ • Reports       │
│ • OLED Display  │    │ • Status        │    │ • PDF Export    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Hardware Requirements

### Raspberry Pi Setup
- Raspberry Pi 4 (recommended) or Pi 3B+
- MicroSD card (32GB recommended)
- USB Camera or Raspberry Pi Camera Module
- 0.96" OLED Display (SSD1306, I2C)
- IR Proximity Sensor
- Jumper wires and breadboard
- Power supply (5V 3A)

### Circuit Connections
- **OLED Display**: Connect to I2C (SDA/SCL pins)
- **IR Sensor**: Connect to GPIO pin 17
- **USB Camera**: Connect to USB port

## 💻 Software Requirements

### Raspberry Pi
- Raspberry Pi OS (Bullseye or later)
- Python 3.8+
- Required Python packages (see [`MAIN Programs/RPI/requirements.txt`](MAIN%20Programs/RPI/requirements.txt))

### PC/Server
- Python 3.8+
- Flask and dependencies
- Firebase Admin SDK
- PDF generation libraries

## 🚀 Installation & Setup

### 1. Raspberry Pi Setup

#### System Dependencies
```bash
sudo apt update
sudo apt install -y python3-dev python3-pip libfreetype6-dev libjpeg-dev \
    build-essential libopenjp2-7 libtiff5 libatlas-base-dev i2c-tools \
    python3-pil cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev \
    libboost-python-dev
```

#### Enable I2C
```bash
sudo raspi-config
# Navigate to Interface Options → I2C → Enable
sudo reboot
```

#### Python Environment
```bash
python3 -m venv ~/attendance_env --system-site-packages
source ~/attendance_env/bin/activate
pip install -r "MAIN Programs/RPI/requirements.txt"
```

#### Download Face Recognition Models
```bash
# Download the required dlib models (see MAIN Programs/RPI/readme.md for links)
wget https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2
wget https://github.com/davisking/dlib-models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2
bunzip2 *.bz2
```

### 2. PC/Server Setup

#### Install Dependencies
```bash
cd "MAIN Programs/PC"
pip install -r requirements.txt
```

#### Firebase Configuration
1. Download your Firebase service account key
2. Place it in the project root
3. Update the path in [`upcloud.py`](upcloud.py) and [`app.py`](MAIN%20Programs/PC/app.py)

### 3. Configuration

#### Update Configuration Files
- **Raspberry Pi**: Edit [`MAIN Programs/RPI/config.py`](MAIN%20Programs/RPI/config.py)
  ```python
  SERVER_CONTROL_URL = "http://YOUR_PC_IP:5000/status"
  IR_GPIO_PIN = 17
  CAMERA_RESOLUTION = (640, 480)
  ```

- **PC Application**: Update Firebase credentials in [`MAIN Programs/PC/app.py`](MAIN%20Programs/PC/app.py)

### 4. Add Known Faces
Place student photos in [`MAIN Programs/RPI/known_faces/`](MAIN%20Programs/RPI/known_faces/) directory. Filename should be the student's name (e.g., `john_doe.jpg`).

## 🎯 Usage

### Starting the System

#### 1. Start the PC/Web Application
```bash
cd "MAIN Programs/PC"
python app.py
```
Access the web dashboard at `http://localhost:5000`

#### 2. Start the Raspberry Pi Unit
```bash
cd "MAIN Programs/RPI"
source ~/attendance_env/bin/activate
python main.py
```

### Web Dashboard Usage

1. **Login**: Use credentials (admin/1234)
2. **Control System**: Turn attendance tracking on/off
3. **Monitor Students**: View individual attendance records
4. **Generate Reports**: Create PDF reports for different time periods
5. **View Analytics**: Access various charts and statistics

### Default Credentials
- **Username**: admin
- **Password**: 1234

## 📁 Project Structure

```
Smart-Attendence-System/
├── MAIN Programs/
│   ├── PC/                          # Web application
│   │   ├── app.py                   # Main Flask application
│   │   ├── templates/               # HTML templates
│   │   │   ├── dashboard.html       # Main control panel
│   │   │   ├── analytics.html       # Analytics dashboard
│   │   │   ├── students.html        # Student management
│   │   │   └── ...                  # Other templates
│   │   ├── static/                  # Static files (CSS)
│   │   └── attendance_data/         # Generated reports
│   │
│   └── RPI/                         # Raspberry Pi code
│       ├── main.py                  # Main program
│       ├── face_recognition.py      # Face recognition logic
│       ├── camera.py                # Camera handling
│       ├── ir_sensor.py             # IR sensor interface
│       ├── oled_display.py          # OLED display functions
│       ├── config.py                # Configuration
│       ├── known_faces/             # Student photos
│       └── requirements.txt         # Python dependencies
│
├── Trial_Projects/                  # Development and testing
│   ├── PC_Code/                     # Trial PC code
│   └── Raspberry_PI/                # Trial Pi code
│
├── upcloud.py                       # Firebase utility
├── attendance_data/                 # Data storage
└── README.md                        # This file
```

## 🔌 API Endpoints

### Control Endpoints
- `GET /status` - Get system status
- `GET /toggle/<state>` - Set system on/off

### Data Endpoints
- `GET /api/stats` - Get attendance statistics
- `GET /api/student/<name>` - Get individual student data
- `POST /submit_attendance` - Submit attendance record

### Report Endpoints
- `GET /download_pdf` - Generate full attendance report
- `GET /monthly_report` - Monthly attendance report
- `GET /student_report/<name>` - Individual student report

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔧 Troubleshooting

### Common Issues

#### Raspberry Pi Issues
- **Camera not detected**: Check USB connection and permissions
- **I2C device not found**: Ensure I2C is enabled and OLED is properly connected
- **Face recognition errors**: Verify dlib models are downloaded and in correct location

#### Connectivity Issues
- **Cannot reach server**: Check network connectivity and firewall settings
- **Firebase connection failed**: Verify service account key and database URL

#### Web Dashboard Issues
- **Charts not loading**: Ensure matplotlib backend is set correctly
- **PDF generation fails**: Check file permissions and available disk space

### Debug Mode
Enable debug logging by setting `debug=True` in the Flask app or adding logging statements in the Pi code.

### Testing Components

#### Test Camera
```bash
cd "MAIN Programs/RPI/trial codes"
python take_picture.py
```

#### Test OLED Display
```bash
cd "MAIN Programs/RPI/trial codes"
python oled_trial.py
```

#### Test IR Sensor
```bash
cd "MAIN Programs/RPI/trial codes"
python ir_test.py
```

## 📧 Support

For issues and questions:
1. Check the [troubleshooting section](#troubleshooting)
2. Review the code comments and configuration files
3. Create an issue in the repository

## 📄 License

This project is open source and available under the MIT License.

---

**Note**: This project was developed as an educational IoT system. Ensure proper privacy considerations and permissions before deploying in production environments.
