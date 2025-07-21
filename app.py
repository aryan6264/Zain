# Created by MANI LEGEND - DAKU 302 🐯🔥
# This script sends messages using multiple tokens to a Facebook convo UID.
# Supports: token.txt, convo.txt, file.txt (message file), time.txt, hatersname.txt

import os
import time
import requests
import platform

# Setup
system_type = platform.system()
clear_cmd = 'cls' if system_type == 'Windows' else 'clear'
os.system(clear_cmd)

# Read files
with open('token.txt', 'r') as f:
    tokens = [line.strip() for line in f if line.strip()]

with open('convo.txt', 'r') as f:
    convo = f.read().strip()

with open('file.txt', 'r') as f:
    msg_file = f.read().strip()

with open(msg_file, 'r', encoding='utf-8') as f:
    messages = [line.strip() for line in f if line.strip()]

with open('time.txt', 'r') as f:
    delay = int(f.read().strip())

with open('hatersname.txt', 'r', encoding='utf-8') as f:
    hater = f.read().strip()

print(f"🐯 MANI LEGEND PANEL STARTED\n📨 Messages loaded: {len(messages)}\n🧠 Delay: {delay}s\n")

while True:
    for token in tokens:
        for msg in messages:
            message_text = f"{hater} {msg}"
            try:
                res = requests.post(
                    f"https://graph.facebook.com/v18.0/t_{convo}/messages",
                    data={"access_token": token, "message": message_text}
                )
                if res.status_code == 200:
                    print(f"SENT ✅: {message_text}")
                else:
                    print(f"FAIL ❌: {message_text} — {res.text}")
                time.sleep(delay)
            except Exception as e:
                print(f"ERROR ❌: {e}")
