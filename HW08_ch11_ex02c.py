#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports
import itertools

# Body
'''
def reverse_lookup_old(d, v):
	lst = []
	lt = []
	for k in d:
		if d[k] == v:
		lst.append(k)
		continue
		else:
			return lt
		return lst
'''


def reverse_lookup_new(d, v):
	lst = []
	lt = []
	for k in d:
		if d[k] == v:
			lst.append(k)
		else:
			continue
	if len(lst) == 0:
		return lt
	else:
		return(lst)



###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_old(s):
    d = dict()
    for c in s:
        d[word] = d.get(word,0) +1  
    return d


def histogram_new(pledge_list):
    counts=dict()
    for word in pledge_list:
        counts[word] = counts.get(word,0) +1  
    return counts

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    pledge_list = []
    handle= open('pledge.txt')
    for line in handle:
        lines = line.strip().split()
        #print (lines)
        if len(line) > 1:
            if lines[-1][-1] == ',' or lines[-1][-1] == '.' or lines[-1][-1] == ':' :
                #print(lines)
                lines[-1]= lines[-1][:-1]
                #print(lines)
                pledge_list.append(lines)
                continue
            else:
                pledge_list.append(lines)
                continue
    pledge_list = list(itertools.chain.from_iterable(pledge_list))
    return pledge_list 

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():   # DO NOT CHANGE BELOW
	pledge_histogram = histogram_new(get_pledge_list())
	print(reverse_lookup_new(pledge_histogram, 1))
	print(reverse_lookup_new(pledge_histogram, 9))
	print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
