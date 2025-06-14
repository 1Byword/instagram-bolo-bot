import os
import time
from instagrapi import Client

USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")

cl = Client()
cl.login(USERNAME, PASSWORD)
print(f"🔐 Logged in as {USERNAME}, bot started.")

replied = set()

while True:
    inbox = cl.direct_threads(amount=10)
    for thread in inbox:
        user = thread.users[0]
        uid = user.pk
        uname = user.username
        last = thread.messages[0]
        if uid not in replied and last.user_id != cl.user_id:
            cl.direct_send(f"@{uname} bolo fast", [uid])
            print(f"➡️ Replied to @{uname}")
            replied.add(uid)
    time.sleep(10)
