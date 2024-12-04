import csv,re
import numpy as np
first_list=[]
second_list=[]

with open("input.txt","r",encoding="utf-8") as f:
    processed_lines = (re.sub(r'\s+(?=\S)', ';', line) for line in f)
    reader=csv.reader(processed_lines,delimiter=';')
    for row in reader:
        first_list.append(int(row[0]))
        second_list.append(int(row[1]))
        
sorted_first_list=np.array(first_list)
sorted_second_list=np.array(second_list)
sorted_first_list.sort()
sorted_second_list.sort()

print(abs(sorted_second_list-sorted_first_list).sum())

from itertools import groupby

frequencies=groupby(sorted_second_list)
keys=[]
values=[]
for element in frequencies:
    keys.append(element[0])
    values.append(len(list(element[1])))
counts=dict(zip(keys,values))
s=0
for n in sorted_first_list:
    if n in counts:
        s+=counts[n]*n
        
print(s)
    