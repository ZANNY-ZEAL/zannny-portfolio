import time, random, sys

def type_text(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

targets = ["NASA", "Google", "CIA", "FBI"]
target = random.choice(targets)

type_text(f"Connecting to {target} server...")
time.sleep(1)
type_text("Bypassing firewall...")
time.sleep(1)
type_text("Access granted ✅")
time.sleep(1)
type_text(f"Downloading secret files from {target}...")
time.sleep(2)
type_text("Mission Complete 💻💀")

