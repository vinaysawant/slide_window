#!/usr/bin/env python
from collections import deque

def slide_min(window_size,sequence):
    window = deque()
    for i, x in enumerate(sequence):
        while window and window[-1][0] >= x:
            window.pop()
        window.append((x, i))
        while window[0][1] <= i - window_size:
            window.popleft()
        yield window[0][0]

if __name__=='__main__':
	fname=raw_input("Enter filename: => ")
	f=open(fname,"r")
	window_size=int(f.readline())
	sequence=f.readline()
	s=sequence.split()
	sequence=map(int,s)
	j=0
	for x in slide_min(window_size,sequence):
			j=j+1
			if j>2:
				print x,
