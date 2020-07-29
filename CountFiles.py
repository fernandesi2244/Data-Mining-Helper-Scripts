"""
Determines the number of files of the specified file type in the specified directory.

Can also be used to check how many files have a certain substring within them.

Developed by Ian Fernandes
"""

import sys
import os

args = sys.argv
file_types_to_check = list()

if len(args) < 2:
	print('CORRECT USAGE:')
	print('\tpython CountFiles.py <directory path> <optional space-delimited list of file types to count>')
	print('EXAMPLE USAGE:')
	print('\tpython CountFiles.py TestTrainingData bitmap Br')
	sys.exit()
else:
	dir = args[1]
	file_types_to_check.extend(args[2:])

if len(file_types_to_check) == 0:
	file_types_to_check.append('')	# If no file types specified, match all files

for file_type in file_types_to_check:
	print('-'*60)

	num_files = 0
	
	for file in os.listdir(dir):
		if os.path.isfile(os.path.join(dir, file)) and file_type in file:
			num_files += 1
		
	print(f"Number of {file_type} files in '{dir}' directory: {num_files:,d}")

	print('-'*60)