# Every time a new file is added to C:\Users\colin\OneDrive\Documents\Trackmania2020\Replays\My Replays, move it to D:\Trackmania Replays

import os
import shutil
import time

# Set the path to the folder you want to monitor
path_to_watch = "C:\\Users\\colin\\OneDrive\\Documents\\Trackmania2020\\Replays\\My Replays"

# Set the path to the folder you want to move the files to
path_to_move = "D:\\Trackmania Replays"

# Set the time to wait between checking for new files
wait_time = 5

if (os.path.isdir(path_to_watch) == False):
    print("Path to watch does not exist")
    exit()
    
if (os.path.isdir(path_to_move) == False):
    print("Path to move does not exist")
    exit()

