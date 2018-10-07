#!/usr/bin/python

from __future__ import unicode_literals
import youtube_dl
import sys
from subprocess import call

# Add functionality to auto rename metadata and add to iTunes
 
def main () :

	
		if sys.argv[1] == "-a":
			command = 'pytube ' + sys.argv[2];
			call(command.split(), shell=False);

		elif sys.argv[1] == "-v":
			command = 'pytube ' + sys.argv[2];
			call(command.split(), shell=False);
		
		else :
			sys.exit("usage: " + sys.argv[0] + " [-a,-v,-av] <link>\n -a = audio\n -v = video\n -a+v = audio + video\n")

if ( __name__ == "__main__" ) :
	main();




command = 'pytube ' + sys.argv[1];
call(command.split(), shell=False);
