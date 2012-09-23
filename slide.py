#!/usr/bin/env python
import sys

def openfile(fname):								#open file in read mode
    f=open(fname,"r")								#
    window_size=int(f.readline())					#read first line i.e (sliding window size)
    stream=f.readline()								#read second line i.e (input stream) 
    return window_size,stream
    f.close()										#closed file

fname=raw_input("Enter filename: => ")				#input from user (filename)
window_size,stream=openfile(fname)					#called function 'openfile' to read file

stream_a=[int(i) for i in stream.split()]			#converted input stream into array

while len(stream_a)-window_size+1: 					#
	l=min(stream_a[:window_size])					#find minimum element
	sys.stdout.write("%d " %l)
	sys.stdout.flush()
	stream_a.pop(0)									#poped first element and again find min(window_size)
