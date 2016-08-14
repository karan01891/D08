#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports
import itertools

# Body
def print_hist_old(counts):
    for c in sorted(counts):
   		print(c, counts[c])
    

def print_hist_new(pledge_list):
    counts=dict()
    for word in pledge_list:
        counts[word] = counts.get(word,0) +1  
    return(print_hist_old(counts))

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


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################

def main():  # DO NOT CHANGE BELOW
	print_hist_new(get_pledge_list())

if __name__ == '__main__':
    main()
