"""
Moves the files from one directory to another.

Developed by Ian Fernandes and Yash Kadadi
"""

import os
import sys
import time
import shutil

args = sys.argv
file_types = ['']

if len(args) < 3:
    print('CORRECT USAGE:')
    print('\tpython MoveFiles.py <source directory path> <destination directory path> <optional space-delimited list of file types to move>')
    print('EXAMPLE USAGE:')
    print('\tpython MoveFiles.py TestTrainingData TrainingData bitmap Br')
    sys.exit()
else:
    old_path = args[1]
    new_path = args[2]
    if len(args[3:]) == 0:
        file_types = [''] # Allow any file if no type specified
    else:
        file_types = args[3:]

now = time.time()
counter = 0

# time_interval = 17.83*3600 # Program run at 5:50 PM -> 17.83 hours since 12 AM, each hour = 3600s

for filename in os.listdir(old_path):
    abs_path = os.path.join(old_path, filename)
    #if os.stat(abs_path).st_mtime < now - (56000):
    # and ('.2017' in filename or '.2018' in filename or '.2019' in filename)
    is_correct_file_type = any(a in filename for a in file_types)
    if is_correct_file_type and os.path.isfile(abs_path) and not os.path.exists(os.path.join(new_path, filename)):
        # if now - os.stat(abs_path).st_mtime < time_interval:
        # Using shutil lets you move files across different file systems/partitions.
        shutil.move(abs_path, new_path)
        counter += 1 # Count number of files added today
        if counter%1000 == 0:
            print("Counter at", counter)

print(str(counter) + " files were moved.")