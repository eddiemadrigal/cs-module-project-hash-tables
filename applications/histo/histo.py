# Your code here

from collections import defaultdict

# Read in all the words in one go
with open("/Lambda/git/cs-module-project-hash-tables/applications/histo/robin.txt") as f:
    words = f.read().split()

def count_elements(seq) -> dict:    # fn takes a sequence and returns a dictionary
    hist = {}                       # make an empty dictionary
    for i in seq:                   # for i in the sequence
        hist[i] = hist.get(i, 0) + 1# take hist dictionary at that i index and call get.  if the value is there, we'll get the value, otherwise we'll get the zero
    return hist                     # return the hist dictionary

def ascii_histogram(seq) -> None:   # def ascii histogram that will also take in a sequence and return None
    counted = count_elements(seq)   # call the count_elements function on the sequence save it as counted
    for k in sorted(counted):       # loop through and sort the dictionary
        print(f'{k} {"#" * counted[k]}')    # f-string formatting and print out 'k' as well as '#' as many times as the value 'k' appears in counted

ascii_histogram(words)              # run the ascii_histogram with the list: words as the input
