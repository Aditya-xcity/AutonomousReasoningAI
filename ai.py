# Question: Simulate message sending with delay and colored output

# Name - ADITYA BHARDWAJ
# Section - D2
# Roll No - 07
# Course – B TECH
# Branch – CSE

import time
import sys

# ANSI color codes
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

msg = input("(Coding Wali ai Gf):Enter your message: ")

# Sent message
print(GREEN + "Message Sent: " + msg + RESET)

# Thinking with seconds (same line)
for i in range(1, 4):
    sys.stdout.write(f"\rThinking {i}s...")
    sys.stdout.flush()
    time.sleep(1)

# Replace line with blocked message
sys.stdout.write("\r" + RED + "You are blocked      " + RESET + "\n")