#!/usr/bin/env python
#regex search 
import sys
import re
import os


def findall(regex):
	for filename in os.listdir(os.getcwd()):
		if os.path.isfile(filename):
			with open(filename) as f:
				for line in f:
					if re.search(regex, line) is not None:
						print "Match:", line, "Filename:", filename
					


	

def main():
	if len(sys.argv) != 2:
		print "Usage: python -m regex_search REGULAR_EXPRESSION_IN_QUOTES"
		sys.exit(0)
	regex = sys.argv[1]

	findall(regex)

if __name__ == '__main__':
	main()