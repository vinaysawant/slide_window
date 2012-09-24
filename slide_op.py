#!/usr/bin/env python
import sys												#for printing on same
														#line

fname=raw_input("Enter filename: => ")                  #input file from user
f=open(fname,"r")									 	#file open in read mode
window_size=int(f.readline())							#get slide window size	
sequence=f.readline()									#get sequence & convert
sequence=[int(element) for element in sequence.split()] #into integer array
f.close()												#close file

def findmin(window_size,sequence):						#function to calc min
	for i in xrange(len(sequence) - window_size + 1):	#and print on same line
		sys.stdout.write("%d " %min(sequence[i:i+window_size]))

findmin(window_size,sequence)							#call finction 'findmin'
