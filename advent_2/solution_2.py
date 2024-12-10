import csv, re
import numpy as np

reports_list = []

with open("input.txt", "r", encoding="utf-8") as f:
    processed_lines = (re.sub(r"\s+(?=\S)", ";", line) for line in f)
    reader = csv.reader(processed_lines, delimiter=";")
    for row in reader:
        reports_list.append([int(level) for level in row])


def is_safe(report):
    n = len(report)
    first = report[1] - report[0]
    for i in range(n - 1):
        s = report[i + 1] - report[i]
        if not 1 <= abs(s) <= 3:
            return 0
        if first * s < 0:
            return 0
    return 1


total_safe = 0
for report in reports_list:
    total_safe += is_safe(report)

print(total_safe)

"""
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
    """
