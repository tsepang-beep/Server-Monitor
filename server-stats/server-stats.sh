#!/bin/bash

# ==========================================
# Server Performance Monitoring Script
# This script analyzes system performance
# ==========================================

echo "========================================"
echo "        SERVER PERFORMANCE REPORT       "
echo "========================================"
echo ""

# -------------------------------
# CPU Usage
# -------------------------------
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)" | awk '{print "Used: " 100 - $8 "%"}'
echo ""

# -------------------------------
# Memory Usage
# -------------------------------
echo "Memory Usage:"
free -m | awk 'NR==2{
    printf "Used: %sMB (%.2f%%)\nFree: %sMB (%.2f%%)\n",
    $3, $3*100/$2,
    $4, $4*100/$2
}'
echo ""

# -------------------------------
# Disk Usage
# -------------------------------
echo "Disk Usage:"
df -h / | awk 'NR==2{
    print "Used: " $3 " (" $5 ")"
    print "Free: " $4
}'
echo ""

# -------------------------------
# Top 5 Processes by CPU
# -------------------------------
echo "Top 5 Processes by CPU Usage:"
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6
echo ""

# -------------------------------
# Top 5 Processes by Memory
# -------------------------------
echo "Top 5 Processes by Memory Usage:"
ps -eo pid,comm,%mem --sort=-%mem | head -n 6
echo ""

# -------------------------------
# Load Average
# -------------------------------
echo "Load Average (1, 5, 15 min):"
uptime | awk -F'load average:' '{ print $2 }'
echo ""

# -------------------------------
# Failed Login Attempts
# -------------------------------
echo "Failed Login Attempts:"

# Check log file based on system type
if [ -f /var/log/secure ]; then
    count=$(grep "Failed password" /var/log/secure | wc -l)
elif [ -f /var/log/auth.log ]; then
    count=$(grep "Failed password" /var/log/auth.log | wc -l)
else
    count=0
fi

echo "Total Failed Login Attempts: $count"
echo ""

# -------------------------------
# System Uptime
# -------------------------------
echo "System Uptime:"
uptime
echo ""

# -------------------------------
# OS Version
# -------------------------------
echo "Operating System:"
grep PRETTY_NAME /etc/os-release | cut -d= -f2
echo ""

# -------------------------------
# Logged in Users
# -------------------------------
echo "Logged in Users:"
who
echo ""

echo "========================================"
echo "           END OF REPORT                "
echo "========================================"
