#!/usr/bin/env python3

# ==========================================
# Server Performance Monitoring Script
# This script analyzes system performance
# ==========================================

import os
import subprocess

print("========================================")
print("        SERVER PERFORMANCE REPORT       ")
print("========================================\n")

# -------------------------------
# CPU Usage
# -------------------------------
print("CPU Usage:")
cpu = subprocess.getoutput("top -bn1 | grep 'Cpu(s)'")
try:
    idle = float(cpu.split()[7])
    used = 100 - idle
    print(f"Used: {used:.2f}%")
except:
    print("Unable to fetch CPU usage")
print()

# -------------------------------
# Memory Usage
# -------------------------------
print("Memory Usage:")
mem = subprocess.getoutput("free -m").splitlines()[1].split()
total = int(mem[1])
used = int(mem[2])
free = int(mem[3])

print(f"Used: {used}MB ({used * 100 / total:.2f}%)")
print(f"Free: {free}MB ({free * 100 / total:.2f}%)\n")

# -------------------------------
# Disk Usage
# -------------------------------
print("Disk Usage:")
disk = subprocess.getoutput("df -h /").splitlines()[1].split()

print(f"Used: {disk[2]} ({disk[4]})")
print(f"Free: {disk[3]}\n")

# -------------------------------
# Top 5 Processes by CPU
# -------------------------------
print("Top 5 Processes by CPU Usage:")
cpu_processes = subprocess.getoutput(
    "ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6"
)
print(cpu_processes + "\n")

# -------------------------------
# Top 5 Processes by Memory
# -------------------------------
print("Top 5 Processes by Memory Usage:")
mem_processes = subprocess.getoutput(
    "ps -eo pid,comm,%mem --sort=-%mem | head -n 6"
)
print(mem_processes + "\n")

# -------------------------------
# Load Average
# -------------------------------
print("Load Average (1, 5, 15 min):")
load = subprocess.getoutput("uptime")
print(load.split("load average:")[1].strip() + "\n")

# -------------------------------
# Failed Login Attempts
# -------------------------------
print("Failed Login Attempts:")

log_file = ""
if os.path.exists("/var/log/secure"):
    log_file = "/var/log/secure"
elif os.path.exists("/var/log/auth.log"):
    log_file = "/var/log/auth.log"

if log_file:
    failed = subprocess.getoutput(
        f"grep 'Failed password' {log_file} | wc -l"
    )
else:
    failed = "0"

print(f"Total Failed Login Attempts: {failed}\n")

# -------------------------------
# System Uptime
# -------------------------------
print("System Uptime:")
print(subprocess.getoutput("uptime") + "\n")

# -------------------------------
# OS Version
# -------------------------------
print("Operating System:")
os_version = subprocess.getoutput(
    "grep PRETTY_NAME /etc/os-release | cut -d= -f2"
)
print(os_version + "\n")

# -------------------------------
# Logged in Users
# -------------------------------
print("Logged in Users:")
print(subprocess.getoutput("who") + "\n")

print("========================================")
print("           END OF REPORT                ")
print("========================================")
