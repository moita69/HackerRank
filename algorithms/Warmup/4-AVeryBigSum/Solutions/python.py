import os

with open('./input.txt', 'r') as f:
    n = f.readline()
    line = f.readline()
    sum = 0
    for item in line.split(" "):
        sum += int(item)
    
print (sum)

    
