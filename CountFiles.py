"""
Determines the number of files in the specified directory.

Developed by Ian Fernandes
"""

import sys
import os

args = sys.argv
dirs_to_check = list()
count_dirs = True

if len(args) < 2:
	for file in os.listdir('.'):
		if os.path.isdir(file):
			dirs_to_check.append(file)
else:
	for arg in args[1:]:
		dirs_to_check.append(arg)

for dir in dirs_to_check:
	print('-'*60)

	num_files = 0
	num_dirs = 0
	
	if count_dirs:
		for file in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, file)):
				num_files += 1
			if os.path.isdir(os.path.join(dir, file)):
				print(file)
				num_dirs += 1
		
		print(f"Number of files in '{dir}' directory: {num_files:,d}")
		print(f"Number of directories in '{dir}' directory: {num_dirs:,d}")
	else:
		print(f"Number of files in '{dir}' directory: {len(os.listdir(dir)):,d}")
	print('-'*60)