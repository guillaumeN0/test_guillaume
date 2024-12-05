import csv,re
import numpy as np


with open("input.txt","r",encoding="utf-8") as f:
    reader=csv.reader(f,delimiter=',')
    lines_list=[row for row in reader]
    
instructions_list=[]
updates_list=[]
is_instruction=True
for line in lines_list:
    if len(line)==0 :
        is_instruction=False
    elif is_instruction:
        instructions_list.append(line[0].split('|'))
    else:
        updates_list.append(line)
    
middle_true=0
for update in updates_list:
    is_fine=True
    for rule in instructions_list:
        if rule[0] in update and rule[1] in update:
            index_0=update.index(rule[0])
            index_1=update.index(rule[1])
            if index_0 > index_1 :
                is_fine=False
                break
    if is_fine:
        middle_true+=int(update[len(update)//2 ])
        
        
print(middle_true)
        