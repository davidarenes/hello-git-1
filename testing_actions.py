from datetime import datetime
import os

today = datetime.today()
dir = "action_created_files"

if not os.path.exists(dir):
    os.mkdir(dir)

if not os.path.exists(dir):
    file = open(f"{dir}/{today}.txt", "x")
