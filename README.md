# Server Performance Monitoring Script

## 📌 Overview

This project is a **Python-based server monitoring script** that analyzes and reports system performance metrics in real time.

It is designed to quickly check the health of a Linux server.

---

## 🚀 Features

The script provides the following system information:

* ✅ CPU Usage
* ✅ Memory Usage
* ✅ Disk Usage
* ✅ Top 5 Processes (CPU & Memory)
* ✅ Load Average (1, 5, 15 minutes)
* ✅ Failed Login Attempts
* ✅ System Uptime
* ✅ Operating System Info
* ✅ Logged-in Users

---

## 🛠️ Technologies Used

* Python 3
* Linux system commands (`top`, `free`, `df`, `ps`, `uptime`, `who`)
* Bash utilities via Python (`subprocess` module)

---

## 📂 Project Structure

```
Server-Monitor/
│── server_stats.py
│── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone git@github.com:tsepang-beep/Server-Monitor.git
```

2. Navigate into the directory:

```
cd Server-Monitor
```

3. Make the script executable:

```
chmod +x server_stats.py
```

---

## ▶️ Usage

Run the script using:

```
./server_stats.py
```

OR

```
python3 server_stats.py
```

---

## 📊 Example Output

```
========================================
        SERVER PERFORMANCE REPORT
========================================

CPU Usage:
Used: 23.45%

Memory Usage:
Used: 1024MB (50.00%)
Free: 1024MB (50.00%)

Disk Usage:
Used: 10G (40%)
Free: 15G

...
```

---

## 🔐 Security Feature

The script checks for:

* Failed SSH login attempts
* Uses system log files:

  * `/var/log/secure` (RHEL/CentOS)
  * `/var/log/auth.log` (Ubuntu/Debian)

---


## 👨‍💻 Author

**Tsepang Seturumane**

---

## 📌 Future Improvements

* Add colored output
* Export report to file
* Email alerts
* Use Python libraries like `psutil`

---



