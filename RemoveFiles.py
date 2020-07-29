"""
Removes the specified file types in the specified directory.

Developed by Ian Fernandes
"""

import sys
import os

args = sys.argv
files_to_delete = list()
all_possible = ['Bp', 'Bt', 'Br', 'bitmap', 'magnetogram']

if len(args) == 1:
	print('CORRECT USAGE:')
	print('\tpython RemoveFiles.py <directory path> <optional space-delimited list of types of files to delete>')
	print('EXAMPLE USAGE:')
	print('\tpython RemoveFiles.py TrainingData Bp Bt Br bitmap')
	sys.exit()

file_path = args[1]

if len(args) == 2:
	# No file types specified; run for each type of file.
	for file_type in all_possible:
		files_to_delete.append(file_type)
else:
	# Args entered; run for specified types of files.
	for arg in args[2:]:
		files_to_delete.append(arg)

write_file = open('deleted_files.txt', 'a')
write_file.write('-'*100+'\n')

for file_type in files_to_delete:
	num_files = 0
	
	for file in os.listdir(file_path):
		if file_type in file:
			os.remove(os.path.join(file_path, file))
			num_files += 1
			write_file.write(file+' was deleted.\n')
			# Use flush and fsync to make sure we can see updates live
			write_file.flush()
			os.fsync(write_file)

	print('-'*60)
	print(f"Number of '{file_type}' files that were deleted: {num_files:,d}")
	print('-'*60)

write_file.close()