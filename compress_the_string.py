import itertools
data = input()
x = itertools.groupby(data)
for k,v in x:
    print(((len(list(v)), int(k))),end=" ")
    
