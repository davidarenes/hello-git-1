from datetime import datetime
import os

now = datetime.now()
date = now.strftime("%Y-%m-%d-%X")

dir = "action_created_files"

if not os.path.exists(dir):
    os.mkdir(dir)

if not os.path.exists(f"{dir}/{date}.txt"):
    file = open(f"{dir}/{date}.txt", "x")
