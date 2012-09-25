#!/usr/bin/env python
fname=raw_input("Enter filename: => ")    	#input file from user
f=open(fname,"r")						  	#file open in read mode
window_size=int(f.readline())				#get slide window size	
sequence=f.readline()						#get sequence & convert
sequence=[int(element) for element in sequence.split()] #into integer array
f.close()												#close file

def findmin(window_size,sequence):						#function to calc min
	for i in xrange(len(sequence) - window_size + 1):	#and print on same line
		s=sequence[i:i+window_size]						#take Window_Size sequence in s
		s.sort()										#sort the sequence
		print s[0],										#print min of sequence
		
findmin(window_size,sequence)				#call finction 'findmin'


