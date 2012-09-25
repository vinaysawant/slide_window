#!/usr/bin/env python
fname=raw_input("Enter filename: => ")    	#input file from user
from datetime import datetime
f=open(fname,"r")						  	#file open in read mode
t1=datetime.now()
window_size=int(f.readline())				#get slide window size	
sequence=f.readline()						#get sequence & convert
sequence=[int(element) for element in sequence.split()] #into integer array
f.close()												#close file

def findmin(window_size,sequence):						#function to calc min
	cnt=0
	for i in xrange(len(sequence) - window_size + 1):	#and print on same line
		s=sequence[i:i+window_size]						#take Window_Size sequence in s
		s.sort()										#sort the sequence
		print s[0],										#print min of sequence
		cnt=cnt+1
	return cnt
cnt=findmin(window_size,sequence)				#call finction 'findmin'
print '\nTotal Number of elements are (sequence - window_size)',
print cnt
t2=datetime.now()
diff=t2-t1
print 'time taken to execute ',
print diff


