# Server Performance Monitoring Tool

## 📌 Overview

This project is a **Server Performance Monitoring Tool** designed to analyze and display key system performance metrics on a Linux server.

It includes two implementations:

* 🐍 **Python Script**
* 🐚 **Bash Script**

Both scripts provide a quick and efficient way to monitor system health.

---

## 🚀 Installation

Clone the repository using SSH:

```
git clone git@github.com:tsepang-beep/Server-Monitor.git
```

Navigate into the project directory:

```
cd Server-Monitor
```

---

## ⚙️ Features

The scripts monitor:

* CPU Usage
* Memory Usage
* Disk Usage
* Top Processes (CPU & Memory)
* Load Average (1, 5, 15 minutes)
* Failed Login Attempts
* System Uptime
* Operating System Information
* Logged-in Users

---

## 📂 Project Structure

```
Server-Monitor/
├── server_stats.py   # Python version
├── server_stats.sh   # Bash version
└── README.md
```

---

## 🐍 Python Script Usage

Run the Python script:

```
python3 server_stats.py
```

Or make it executable:

```
chmod +x server_stats.py
./server_stats.py
```

---

## 🐚 Bash Script Usage

Make the script executable:

```
chmod +x server_stats.sh
```

Run the script:

```
./server_stats.sh
```

---

## 📊 Example Output

```
========================================
SERVER PERFORMANCE REPORT
========================================

CPU Usage:
Used: 23%

Memory Usage:
Used: 1024MB (50%)
Free: 1024MB (50%)

Disk Usage:
Used: 10G (40%)
Free: 15G
```

---

## 🔐 Security Feature

The scripts check for failed SSH login attempts using:

* /var/log/secure (RHEL/CentOS)
* /var/log/auth.log (Debian/Ubuntu)

This helps detect unauthorized access attempts.

---

## 🎯 Learning Objectives

This project demonstrates:

* Linux system monitoring
* Automation using Python
* Bash scripting
* Use of system commands
* Git and GitHub workflow

---

## 🚀 Future Improvements

* Add colored output
* Save reports to a file
* Automate execution using cron jobs
* Add alert notifications

---

## 👨‍💻 Author

Tsepang Seturumane

---

## 📁 Repository

Server-Monitor

