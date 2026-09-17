# 🎤 BRANKS3 – Karaoke Reels

### 🎵 Sing • Record • Listen • Download

**BRANKS3 Karaoke Reels** is a web-based **karaoke and sing-along platform** built with **Django**.

The application allows users to browse shared songs, listen to the original song, record their own voice while the song plays, and access their saved recordings.

Administrators can upload songs, accompaniment tracks, lyrics images, manage songs, and control which songs are publicly shared.

---

## 🚀 Project Overview

Traditional karaoke applications can require complicated software or separate audio/video tools.

**BRANKS3 Karaoke Reels** provides a simple web-based workflow:

```text
Admin Uploads Song
        ↓
Original Song + Accompaniment + Lyrics
        ↓
Song Published / Shared
        ↓
User Opens Song
        ↓
Play Song
        ↓
Record User Voice
        ↓
Recording Uploaded
        ↓
Play Recording
        ↓
Download Recording
```

The project is designed to provide a simple and accessible **online singing and karaoke experience**.

---

## ✨ Features

### 🎵 Karaoke Features

* 🎤 Online karaoke experience
* 🎵 Original song playback
* 🎶 Accompaniment/music playback
* 🎙️ Voice recording
* ⏹️ Start and stop recording
* ▶️ Play saved recordings
* ⬇️ Download recordings
* 🖼️ Lyrics image support
* 🎬 Reel-style song interface

### 👤 User Features

* 🔐 User login
* 🚪 Logout
* 👤 User dashboard
* 🎵 Browse shared songs
* 🎤 Record singing
* ▶️ Play recordings
* ⬇️ Download recordings

### 👨‍💻 Admin Features

* 🔐 Admin authentication
* 🎵 Upload songs
* 🎶 Upload accompaniment tracks
* 🖼️ Upload lyrics images
* 📂 Manage songs
* 🌐 Share/unshare songs
* 🗑️ Delete songs
* 👥 Manage admin/user roles

### 🌐 Website Features

* 📱 Responsive web interface
* 🎨 Custom karaoke UI
* 📜 Privacy Policy page
* 📞 Contact page
* ℹ️ About page
* ❓ FAQ page
* 📋 Terms page
* 🤖 robots.txt
* 🗺️ sitemap.xml
* 📢 ads.txt support

---

# 🧠 How It Works

## 1️⃣ Admin Uploads a Song

An administrator can upload:

```text
Song Name
     +
Original Audio
     +
Accompaniment Audio
     +
Lyrics Image
```

The song information is stored in the Django database.

The application uses a `Song` model containing the song name, original file, accompaniment file, lyrics image, uploader, creation date, and sharing status.

---

## 2️⃣ Song Sharing

Administrators can control whether a song is available publicly.

```text
Song
 │
 ├── Shared
 │      ↓
 │   Users can access
 │
 └── Not Shared
        ↓
     Restricted
```

Shared songs are displayed to users through the public/user interfaces.

---

## 3️⃣ User Opens a Song

A user can open an available song and access the karaoke player.

The application supports song URLs using a song ID and slug, for example:

```text
/song-id/song-name/
```

The application also maintains older karaoke URL formats for compatibility.

---

## 4️⃣ Play the Song

The karaoke interface provides playback controls.

```text
▶️ Play
🎙️ Record
⏹️ Stop
```

The original audio and accompaniment audio are loaded into the browser for playback.

---

## 5️⃣ Record Your Voice

When the user presses **Record**, the browser requests microphone permission.

The application uses the browser's:

```text
MediaDevices API
        ↓
Microphone Stream
        ↓
MediaRecorder
        ↓
WebM Recording
```

The recorded audio is collected as chunks and converted into a WebM audio file.

---

## 6️⃣ Upload the Recording

After recording stops, the WebM file is uploaded to the Django server.

The backend stores the recording inside:

```text
media/
└── recordings/
```

A `Recording` database record is also created and connected to the corresponding song and user.

---

## 7️⃣ Play the Recording

After successful upload, the application provides a playback interface.

Users can:

```text
▶️ Play Recording
⏹️ Stop / Cancel
```

The saved recording is loaded from the generated media URL.

---

## 8️⃣ Download the Recording

The application provides a download option so users can save their recorded karaoke audio locally.

```text
🎤 User Recording
        ↓
   WebM File
        ↓
      Download
```

---

# 🏗️ Application Architecture

```text
                    BRANKS3
                       │
          ┌────────────┴────────────┐
          │                         │
       Frontend                  Backend
          │                         │
     HTML / CSS / JS             Django
          │                         │
          │                ┌────────┴────────┐
          │                │                 │
       Browser          Views             Models
          │                │                 │
          │                │              SQLite /
          │                │              PostgreSQL
          │                │
          │             Media Files
          │                │
          └───────────────┴───────────────
```

---

# 🛠️ Technologies Used

## Backend

* 🐍 Python
* Django
* Gunicorn

## Frontend

* HTML5
* CSS3
* JavaScript

## Audio

* 🎵 Browser Audio API
* 🎙️ MediaRecorder API
* 🎚️ WebM audio recording
* FFmpeg / ffmpeg-python
* Pydub

## Database

* SQLite for local development
* PostgreSQL support through `psycopg2-binary`
* `dj-database-url`

## Static Files

* WhiteNoise

## Image Processing

* Pillow

---

# 📦 Python Dependencies

The project currently includes the following main dependencies:

```text
Django
gunicorn
psycopg2-binary
Pillow
whitenoise
dj-database-url
pydub
ffmpeg-python
```

These dependencies are listed in `requirements.txt`.

---

# 📁 Project Structure

```text
branks3/
│
├── karaoke_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── recorder/
│   ├── migrations/
│   ├── templates/
│   │   └── recorder/
│   │       ├── home_public.html
│   │       ├── login.html
│   │       ├── admin_dashboard.html
│   │       ├── user_dashboard.html
│   │       ├── karaoke_player.html
│   │       ├── songs.html
│   │       ├── about.html
│   │       ├── contact.html
│   │       ├── faq.html
│   │       ├── privacy_policy.html
│   │       └── terms.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── media/
│   ├── songs/
│   ├── recordings/
│   ├── lyrics_images/
│   └── logo/
│
├── static/
│   └── ...
│
├── manage.py
├── requirements.txt
├── runtime.txt
├── Dockerfile
├── Procfile
├── staticfiles_build.sh
├── .gitignore
└── README.md
```

The repository currently contains the main Django project, `recorder` application, media/static directories, deployment files, and dependency configuration.

---

# 🗃️ Database Models

The application currently uses three main models.

## 👤 UserProfile

Stores additional information about Django users.

```text
UserProfile
│
├── user
└── role
     ├── admin
     └── user
```

---

## 🎵 Song

Stores karaoke song information.

```text
Song
│
├── name
├── original_file
├── accompaniment_file
├── lyrics_image
├── uploaded_by
├── created_at
└── is_shared
```

---

## 🎙️ Recording

Stores user karaoke recordings.

```text
Recording
│
├── song
├── user
├── file
└── created_at
```

The current Django models define these relationships directly.

---

# 🔗 Main Application URLs

The application includes routes for:

```text
/
├── Login
├── Logout
├── Admin Dashboard
├── User Dashboard
├── Songs
├── Karaoke Player
├── Upload Song
├── Upload Recording
├── Delete Song
├── Toggle Song Sharing
├── About
├── Contact
├── FAQ
├── Privacy Policy
└── Terms
```

These routes are defined in the `recorder` application's URL configuration.

---

# 💻 Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/branks3-sing/branks3.git
```

---

## 2️⃣ Open the Project Folder

```bash
cd branks3
```

---

## 3️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run Django Migrations

```bash
python manage.py migrate
```

---

## 6️⃣ Create an Admin User

```bash
python manage.py createsuperuser
```

Follow the terminal instructions.

---

## 7️⃣ Start the Development Server

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

Open the address in your browser.

---

# 🎤 How to Use

## 👨‍💻 Admin Workflow

```text
Login
  ↓
Admin Dashboard
  ↓
Upload Song
  ↓
Upload Original Audio
  ↓
Upload Accompaniment
  ↓
Upload Lyrics Image
  ↓
Share Song
```

---

## 🎙️ User Workflow

```text
Open Website
     ↓
Select Song
     ↓
Play Song
     ↓
Allow Microphone
     ↓
Start Recording
     ↓
Sing Along
     ↓
Stop Recording
     ↓
Recording Uploaded
     ↓
Play Recording
     ↓
Download
```

---

# 🎧 Recording Workflow

The browser records microphone input using the MediaRecorder API.

```text
Microphone
    ↓
getUserMedia()
    ↓
MediaRecorder
    ↓
Audio Chunks
    ↓
WebM Blob
    ↓
Django Upload
    ↓
media/recordings/
```

The backend then creates a database record for the uploaded recording.

---

# 🔐 Authentication & Roles

The application supports two primary roles:

```text
Admin
  │
  ├── Upload songs
  ├── Delete songs
  ├── Share/unshare songs
  └── Manage karaoke content

User
  │
  ├── Browse shared songs
  ├── Play songs
  ├── Record voice
  └── Access recordings
```

The backend checks the user's `UserProfile.role` before allowing administrator operations.

---

# 🌐 Deployment

The repository includes deployment-related configuration such as:

```text
Dockerfile
Procfile
runtime.txt
staticfiles_build.sh
```

The project also includes:

```text
gunicorn
whitenoise
dj-database-url
psycopg2-binary
```

which can be used as part of a production deployment setup.

---

# ⚙️ FFmpeg

The project includes Python packages for audio/video processing:

```text
pydub
ffmpeg-python
```

For workflows that require the FFmpeg executable itself, install FFmpeg separately and make sure it is available in the system PATH.

Verify the installation:

```bash
ffmpeg -version
```

---

# 🧪 Development Commands

### Check Django Configuration

```bash
python manage.py check
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Migrations

```bash
python manage.py makemigrations
```

### Run Development Server

```bash
python manage.py runserver
```

### Create Superuser

```bash
python manage.py createsuperuser
```

---

# 🔒 Security

For local development, avoid committing sensitive files such as:

```text
.env
db.sqlite3
venv/
__pycache__/
*.pyc
```

Also avoid uploading private credentials, API keys, database passwords, or deployment secrets to GitHub.

---

# 🚧 Project Status

### 🟢 Active Development

Current project workflow:

```text
🎵 Song Management
       ↓
🎤 Karaoke Player
       ↓
🎙️ Voice Recording
       ↓
💾 Recording Storage
       ↓
▶️ Playback
       ↓
⬇️ Download
```

The project can be extended with additional audio, video, social, and AI-powered features.

---

# 🔮 Future Enhancements

Possible future improvements include:

* 🎧 Advanced audio mixing
* 🎚️ Voice and music volume controls
* 🎤 Real-time microphone visualization
* 🎵 Audio synchronization
* 📝 Live lyrics highlighting
* 🎬 Video karaoke recording
* 📹 Camera recording
* 🎞️ Audio + video export
* 🎨 More reel templates
* 📱 Improved mobile UI
* 👥 User profiles
* ❤️ Like/favorite songs
* 🔎 Song search
* 🏷️ Song categories
* 📊 User recording history
* 🌐 Social sharing
* 🤖 AI voice processing
* 🎙️ Voice enhancement
* 🔊 Noise reduction
* 🎼 Pitch detection
* 📈 Singing performance analysis
* ☁️ Cloud media storage

---

# 🎯 Project Goals

The main goals of BRANKS3 Karaoke Reels are:

```text
Make Singing Easier
        ↓
Make Karaoke Accessible
        ↓
Provide Simple Recording
        ↓
Allow Easy Playback
        ↓
Enable Download & Sharing
```

---

# 🌟 Key Benefits

* 🎤 Simple karaoke workflow
* 🎵 Browser-based audio playback
* 🎙️ Built-in voice recording
* 💾 Automatic recording storage
* 👤 User authentication
* 👨‍💻 Admin content management
* 🖼️ Lyrics image support
* 📱 Web-based interface
* 🔧 Django-based backend
* 🚀 Deployment-ready project structure

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

* Python
* Django
* HTML
* CSS
* JavaScript
* Django Models
* Django Views
* URL Routing
* Authentication
* File Uploads
* Media File Handling
* Browser Audio APIs
* MediaRecorder API
* Database Relationships
* Static File Management
* Audio Processing
* Web Application Deployment

---

# 👩‍💻 Developer

## Shekina Pilla

**B.Tech – Computer Science & Engineering (Data Science)**

### Interests

* 🤖 Artificial Intelligence
* 🎨 3D Animation
* 🎥 Motion Capture
* 💻 Software Development
* 📊 Data Science
* 🎵 Creative Technology
* 🌐 Web Development

---

# 🙏 Acknowledgements

This project uses open-source technologies including:

* Django
* Python
* JavaScript
* HTML5
* CSS3
* Pillow
* Pydub
* FFmpeg
* PostgreSQL
* Gunicorn
* WhiteNoise

---

# 📜 License

This project is developed for **educational, personal, research, and development purposes**.

Please ensure that any songs, music, lyrics, images, or other media uploaded to the application are used with the appropriate rights or permissions.

---

# ⭐ Support

If you find **BRANKS3 Karaoke Reels** useful or interesting, consider giving the repository a ⭐ **Star**.

You can also explore the project, report issues, and suggest improvements.

---

## 🎤 BRANKS3

### **Sing Your Song. Record Your Voice. Create Your Reel.** 🎵🎙️🎬

**Thank you for checking out BRANKS3! ❤️**
