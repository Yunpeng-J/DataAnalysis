#!/usr/bin/python3
import os
import numpy as np
import sys


def readFromFile(filename, marker=" ", n=0):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            temp = line[:-1].split(marker)
            data.append(float(temp[n]))
    return data

def readFromStdin():
    data = []
    for line in sys.stdin:
        temp = line.split()
        for x in temp:
            data.append(float(x)) 
    return data


if len(sys.argv) == 4: # read from file with parameter
    data = readFromFile(sys.argv[1], sys.argv[2], int(sys.argv[3]))
elif len(sys.argv) == 2: # read from file 
    data = readFromFile(sys.argv[1])
else:
    data = readFromStdin()

data = np.array(data)

print("source data:\n", data[:10])

print("\n######")
print("# len: %d" % len(data))
print("# sum: %f" % np.sum(data))
print("# ave: %f" % np.average(data))
print("# median: %f" % np.median(data))
print("######\n")
