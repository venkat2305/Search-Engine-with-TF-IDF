import re

arr = []
with open("lc.txt" , "r") as file:
    for link in file:
        if '/solution' not in link:
            arr.append(link)
        else:
            print('removed : ' + link)

arr = list(set(arr))
print(len(arr))

with open("lc_problems.txt" , 'a') as file:
    for j in arr:
        file.write(j)