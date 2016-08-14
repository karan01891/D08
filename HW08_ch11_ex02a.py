#!/usr/bin/env python3
# HW08_ch11_ex02a
# This is discussed in ThinkPython2 but not formally an exercise.
# Dictionaries have a method called 'get' that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
###############################################################################
# Imports
import itertools

# Body
pledge_histogram = {}


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

#print(get_pledge_list())

###############################################################################
def main():  # DO NOT CHANGE BELOW
    print(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
