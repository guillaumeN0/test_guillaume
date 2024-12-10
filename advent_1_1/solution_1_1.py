import csv, re
import numpy as np

first_list = []
second_list = []

with open("input.txt", "r", encoding="utf-8") as f:
    processed_lines = (re.sub(r"\s+(?=\S)", ";", line) for line in f)
    reader = csv.reader(processed_lines, delimiter=";")
    for row in reader:
        first_list.append(int(row[0]))
        second_list.append(int(row[1]))

sorted_first_list = np.array(first_list)
sorted_second_list = np.array(second_list)
sorted_first_list.sort()
sorted_second_list.sort()

print(abs(sorted_second_list - sorted_first_list).sum())
