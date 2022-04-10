# -*- coding: UTF-8 -*-
def iter_count(file_name):
    from itertools import (takewhile, repeat)
    buffer = 1024 * 1024
    with open(file_name) as f:
        buf_gen = takewhile(lambda x: x, (f.read(buffer) for _ in repeat(None)))
        return sum(buf.count('\n') for buf in buf_gen)

from os import times
import sys

print(len(sys.argv))

if len(sys.argv) != 2 + 1:
    print("Wrong parameter!")

filename1 = sys.argv[1]
filename2 = sys.argv[2]

SUM = 0

map1 = dict()
map2 = dict()

max_index = -1

with open(filename1) as f1:
    with open(filename2) as f2:
        LEN = iter_count(filename1)
        if  LEN != iter_count(filename2):
            print("line not match")
            exit(-1)
        for line1, line2 in zip(f1, f2):
            line1_ = line1.split()
            line2_ = line2.split()
            vertex1 = int(line1_[0])
            vertex2 = int(line2_[0])

            max_index = max(max_index, vertex1, vertex2)
            
            value1 = float(line1_[-1])
            value2 = float(line2_[-1])

            map1[vertex1] = value1
            map2[vertex2] = value2

print(LEN, len(map1), len(map2))
print(max_index)

# for i in range(max_index + 1):
#     if i not in map1:
#         print(i)

for item in map1:
    SUM += abs(map1[item] - map2[item]) / map2[item]            

print(SUM)
print(SUM / LEN)
            
