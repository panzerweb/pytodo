# 📝 PyTodo — Boot Startup To-Do App

**PyTodo** is a simple, terminal-based to-do list application built in **Python**.  
It’s designed to automatically run at system startup, so you can see your tasks every time you open your laptop — helping you stay organized right from boot.

---

## 🚀 Features
- ✅ Add, view, and manage your daily tasks
- 🕒 Runs automatically on system startup (via `.bat` file)
- 🧩 Modular structure (`config`, `models`, `services`, `utils`)
- 💾 Lightweight — no database required
- 💡 Built for quick productivity

---

## 🗂️ Project Structure
```
PYTODO/
├── pytodo/
│ ├── pycache/
│ ├── config/
│ ├── models/
│ ├── services/
│ ├── utils/
│ │ └── init.py
│ ├── main.py
│ ├── menu.py
│ └── tasks.json
├── venv/
├── .gitignore
├── pytodo.bat
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/pytodo.git
cd pytodo
```
---
# Virtual Environment (Recommended)
## Create and activate venv
```python
python -m venv venv
```
## On Windows:
```python
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

# Install Dependencies
```python
pip install -r requirements.txt
```

# Run the script
The `pytodo` directory is considered a module through using `__pycache__` as you can see in the directory, and every other folder that has code has the same `__pycache__` since they were used as a module.

To **run the script**, you activate it using:
```python
python -m pytodo.main
```
or
```python
python pytodo/main
```

---
# Setting up script for Windows Startup boot
## For Windows:

1. Locate the pytodo.bat file in the project root.

2. Press Win + R, type:
```bash
shell:startup
```

- and press **Enter**.

3. Copy pytodo.bat into the opened Startup folder.

4. Now, PyTodo will launch automatically on boot.

---
# Updating Batch File
### Batch file (.bat)
The location will always depend on what drive this repository is in according to your device. Update it to correspond to your preference.
```bash
@echo off
cd /d "drive\path_of_file" # Update location of path
call venv\Scripts\activate
python -m pytodo.main
pause
```

# Requirements:
- Python 3.10+
- Pip (latest)
- Code Editors

# Contributing

> Feel free to fork this repository and improve upon it!
Pull requests are welcome — whether it’s bug fixes, new features, or better documentation.

# Author

**Panzerweb**

Developer-friendly, simple productivity tools.

## Installation (Development Environment):

#### After code changes and verifying its good, do this:
`bash
pyinstaller --onefile pytodo/main.py ^
--hidden-import=speech_recognition ^
--hidden-import=pyaudio
`

**change main.exe in dist/main.exe to pytodo.exe**

#### Open InnoDB Setup

Import the `pytodo_installer.iss` and build



# License

This project is licensed under the MIT License
 — feel free to modify and use it for personal or commercial projects.

