#!/usr/bin/env python
#find large files
import sys
import os

def find_large(path,size):
	#print "Here!"
	done = {}
	for folder, subfolders, filenames in os.walk(path):
		for filename in filenames:
			if os.path.isfile(filename):
				if filename not in done:
					done[filename] = True
					file_size = os.path.getsize(filename)
					#print "File_size:",file_size, file_size > size
					if file_size > size:
						print os.path.abspath(filename), "has size", os.path.getsize(filename) 



def main():
	if len(sys.argv) not in [2,3]:
		print "USAGE: python -m find_large_files PATH_TO_FILE (OPTIONAL_MAX_SIZE)"
	path = sys.argv[1]
	max_size = int(sys.argv[2]) if len(sys.argv) == 3 else 80000
	#print 'path =', path, 'max_size =', max_size
	find_large(path, max_size)



if __name__ == '__main__':
	main()

