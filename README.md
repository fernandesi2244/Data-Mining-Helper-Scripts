# Data-Mining-Helper-Scripts
Some useful scripts for dealing with seemingly trivial data organization operations

CountFiles.py
This script is designed to quickly count the number of files that exist within a specified directory. You can also specify the file types you want to check. This also means that this script can be used to check how many files have a certain substring within their names. Note that the directory can either be given as a relative path or absolute path. This means that no matter where this script is, you can use it to determine the number of files in a directory that is anywhere on the cluster file system (provided there are no access restrictions). 

Usage:
To count all of the files within directory x:
python CountFiles.py x

To count all of the bitmap files within directory x:
python CountFiles.py x bitmap

To count all of the bitmap and Br files within directory x:
python CountFiles.py x bitmap Br

And so on...

CountCorruptedFiles.py
This script is designed to count the number of corrupt files that exist within the specified directory. You can also specify the file types you want to check. However, unlike CountFiles.py, this script will not give a count for each file type but instead for all file types; this is done to save time. Just as before, this script allows for substring searches within the file name. A file is considered corrupt if it has a file size of 0 kilobytes, has corrupt FITS headers (as determined by an error when opening the Sunpy map), or contains NaN values in the associated map’s data array. Again, the directory may be given either as a relative or absolute path.

Usage:
To count all of the corrupt files within directory x:
python CountCorruptedFiles.py x

To count all of the corrupt bitmap files within directory x:
python CountCorruptedFiles.py x bitmap

To count all of the corrupt bitmap and Br files within directory x:
python CountCorruptedFiles.py x bitmap Br

And so on...

MoveFiles.py
This script is designed to move files from one directory to another. If no file types are specified, all of the files from the source directory will be transferred to the destination directory. Otherwise, only files that are of the type specified by the user will be transferred. Again, this functionality also allows for substring searches within file names. Note that this script will still work even if the source and destination directories are on different file systems/partitions. However, this will take a longer time as the program will have to internally copy the files and then delete them from the source directory.

Usage:
To move all of the files from directory x to directory y:
python MoveFiles.py x y

To move all of the bitmap files in directory x to directory y:
python MoveFiles.py x y bitmap

To move all of the bitmap and Br files in directory x to directory y:
python MoveFiles.py x y bitmap Br

And so on...

RemoveFiles.py
This script is designed to delete massive amounts of files at a time from a particularly directory. Like before, file types can be specified for greater control. Moreover, directories may be provided as absolute or relative at the user’s discretion. However, note that at the time this paragraph was last edited, the script only supported removing ‘Br,’ ‘Bt,’ ‘Bp,’ ‘bitmap,’ and ‘magnetogram’ files if no file types were specified. Keep in mind that if file types are specified, you do not need to worry about this.

Usage:
To delete all of the ‘Br,’ ‘Bt,’ ‘Bp,’ ‘bitmap,’ and ‘magnetogram’ files from directory x:
python RemoveFiles.py x

To delete all of the bitmap files in directory x:
python RemoveFiles.py x bitmap

To delete all of the bitmap and Br files in directory x:
python RemoveFiles.py x bitmap Br

And so on...

Note that all of the above scripts can be run with nohup, allowing their processes to run in the background even if the ssh connection times out. This can be very useful for operations like moving hundreds of thousands of files.
