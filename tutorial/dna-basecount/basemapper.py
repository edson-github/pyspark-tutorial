#!/usr/bin/python

def mapper(seq):
	freq = {}
	for x in list(seq):
		if x in freq:
			freq[x] +=1
		else:
			freq[x] = 1
	return [(x, freq[x]) for x in freq]
#
#print mapper("ATCGATCGATAT")	
