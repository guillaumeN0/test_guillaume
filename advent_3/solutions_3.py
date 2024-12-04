import csv,re
import numpy as np
reports_list=[]

with open("input.txt","r",encoding="utf-8") as f:
    instruction=f.read()
    
instructions_list=re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",instruction)
s=0
test=1
for instruction in instructions_list:
    if "mul" in instruction:
        if test==1:
            numbers=re.findall(r"\d{1,3}",instruction)
            s+=int(numbers[0])*int(numbers[1])
    elif instruction == "do()":
        test=1
    else:
        test=0
    
print(s)