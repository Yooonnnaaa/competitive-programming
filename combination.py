from itertools import combinations
y = []
word = input().split()
for i in range(1,int(word[1])+1):
    str=sorted(word[0])
    x = sorted(combinations(str,i))
    for i in x:
        y.append(i)      
for i in y:
    j = "".join(i)
    print(j)
