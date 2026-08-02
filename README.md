# 🎓 SnapClass - AI powered Attendance System

An intelligent attendance management system that automates attendance using **Face Recognition**, **Voice Verification**, and **QR Code-based Subject Enrollment**.

The platform enables teachers to create subjects, manage attendance records, and securely verify student presence through AI-powered authentication methods.

---

# 🚀 Features

## 👨‍🏫 Teacher Features

- Teacher Registration & Login
- Create and Manage Subjects
- Generate Unique Subject Codes
- QR Code-Based Subject Sharing
- View Attendance Records
- Attendance Analytics Dashboard
- Face Recognition Attendance
- Voice-Based Attendance Verification

## 👨‍🎓 Student Features

- Student Registration & Login
- Join Subjects Using Subject Codes
- QR Code Subject Enrollment
- Face Enrollment
- Voice Enrollment
- View Enrolled Subjects
- Mark Attendance Securely

---

# 🧠 AI Components

## Face Recognition

The system verifies student identity through facial recognition before marking attendance.

### Workflow

1. Student enrolls face image.
2. Face embeddings are generated and stored.
3. Live image is captured.
4. Similarity matching is performed.
5. Attendance is marked upon successful verification.

---

## Voice Recognition

Voice authentication provides an additional verification layer.

### Workflow

1. Student records voice sample.
2. Voice features are stored.
3. Live voice is captured during attendance.
4. Voice similarity is checked.
5. Attendance is recorded after successful validation.

---

# 📱 QR Code-Based Subject Enrollment

Teachers can instantly share classroom access using QR codes.

### Process

1. Teacher creates a subject.
2. System generates a unique join URL.
3. QR code is generated automatically.
4. Students scan the QR code.
5. Subject is added to the student dashboard.

---

# 🏗️ System Architecture

```text
Teacher
   │
   ▼
Streamlit Frontend
   │
   ▼
Attendance Pipelines
(Face + Voice)
   │
   ▼
Supabase Backend
   │
   ├── Teachers
   ├── Students
   ├── Subjects
   ├── Enrollments
   ├── Attendance Logs
   └── Face/Voice Data
```

---

# 🛠️ Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## Database

- Supabase (PostgreSQL)

## AI / ML Libraries

- OpenCV
- NumPy
- Pandas
- Face Recognition
- Speech Processing Libraries

## Utilities

- Segno (QR Code Generation)
- Python Dotenv

---

# 📂 Project Structure

```text
AI_Attendance/
│
├── src/
│
├── components/
│   ├── dialog_create_subject.py
│   ├── dialog_share_subject.py
│   ├── dialog_voice_attendance.py
│   ├── dialog_attendance_results.py
│   └── ...
│
├── database/
│   ├── db.py
│   ├── config.py
│   └── ...
│
├── pipelines/
│   ├── face_pipeline.py
│   ├── voice_pipeline.py
│   └── ...
│
├── screens/
│   ├── teacher_screen.py
│   ├── student_screen.py
│   └── ...
│
├── ui/
│   └── base_layout.py
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Krishna-Yadav500/SnapClass---AI-powered-attendance-system.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_KEY"
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

Application runs at:

```text
http://localhost:8501
```

---

# 🗄️ Database Schema

### teachers

Stores teacher information.

### students

Stores student information.

### subjects

Stores subject details.

### enrollments

Maps students to subjects.

### attendance_logs

Stores attendance records.

---

# 📊 Attendance Workflow

## Teacher Flow

```text
Login
   ↓
Create Subject
   ↓
Share QR Code
   ↓
Take Attendance
   ↓
View Reports
```

## Student Flow

```text
Login
   ↓
Join Subject
   ↓
Enroll Face
   ↓
Enroll Voice
   ↓
Mark Attendance
```

---

# 🌐 Deployment

## Streamlit Community Cloud

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Configure secrets
4. Deploy application

---

# 🔮 Future Enhancements

- Attendance Export (CSV/PDF)
- Multi-Face Classroom Detection
- Real-Time Attendance Monitoring
- Admin Dashboard
- Attendance Notifications
- Mobile Application
- AI-Based Attendance Analytics

---

# 📸 Screenshots

Add screenshots of:
- Home Page
 <img width="720" height="368" alt="snap-landing" src="https://github.com/user-attachments/assets/23c60ef1-e8bc-4b31-9538-15f8f07da069" />

- Teacher Dashboard
 <img width="720" height="461" alt="snap-teacher-flow-2-dashboard" src="https://github.com/user-attachments/assets/cf910560-98c0-404a-99ee-828941df1bac" />

- Student Dashboard
 <img width="720" height="505" alt="snap-student-flow-1-login" src="https://github.com/user-attachments/assets/5695100f-3ac0-4a93-accd-622d2a136931" />

- QR Code Sharing
 <img width="720" height="511" alt="snap-teacher-flow-4-share-qr-or-link" src="https://github.com/user-attachments/assets/515aa109-dda9-4b82-b783-ea98b3d9bdae" />
 
- Face Recognition Attendance
 <img width="720" height="480" alt="snap-teacher-flow-5 2-photo-attendance" src="https://github.com/user-attachments/assets/89e7cd30-6e30-4898-b880-7621053c1eb4" />

- Voice Recognition Attendance
 <img width="1081" height="702" alt="snap-teacher-flow-5 1-voice-attendance" src="https://github.com/user-attachments/assets/74d3f6ed-cbe4-4165-958d-f08c5c7ae706" />

- Attendance Records Page
 <img width="720" height="477" alt="snap-teacher-flow-5-see-stored-records" src="https://github.com/user-attachments/assets/a31139d6-839e-4b45-bb89-37ee351d2af2" />


---

# 👨‍💻 Author

**Krishna Yadav**

- B.Tech Computer Science Engineering
- AI & Machine Learning Enthusiast
- Data Science Aspirant

### Connect With Me

- GitHub: https://github.com/Krishna-Yadav500
- LinkedIn: www.linkedin.com/in/krishna-yadav-63a0a5331

---

# 📄 License

This project is intended for educational, research, and portfolio purposes.

If you use this project, please provide appropriate attribution.
