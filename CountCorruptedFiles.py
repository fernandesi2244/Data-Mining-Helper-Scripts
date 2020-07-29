"""
Determines the number of corrupt files of the specified type in the specified directory.

Developed by Ian Fernandes
"""

import sys
import os

import sunpy.map


args = sys.argv
file_types = list()

if len(args) < 2:
	print('CORRECT USAGE:')
	print('\tpython CountCorruptedFiles.py <directory path> <optional space-delimited list of file types to check>')
	print('EXAMPLE USAGE:')
	print('\tpython CountCorruptedFiles.py TestTrainingData bitmap Br')
	sys.exit()
else:
	dir = args[1]
	file_types.extend(args[2:])

if len(file_types) == 0:
	file_types.append('')	# Matches any file name if no file types specified

corrupt_file = open('corrupt_files.txt', 'a')
corrupt_file.write('-'*100+'\n')

num_files = 0

for file in os.listdir(dir):
	if not any(file_type in file for file_type in file_types):
		continue

	try:
		if not os.path.getsize(file) > 0:
			raise Exception()
		map = sunpy.map.Map(file)
		hasNan = np.isnan(np.sum(map.data))
		if hasNan:
			raise Exception()
	except:
		num_files += 1
		corrupt_files.write(file+'\n')
		# Use flush and fsync to make sure we can see updates live
		corrupt_file.flush()
		os.fsync(corrupt_file)
print('Number of corrupt files:', num_files)
corrupt_file.close()