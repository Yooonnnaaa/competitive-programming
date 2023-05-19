import re
from collections import OrderedDict
n = int(input())
order = OrderedDict()
for i in range(n):
    z = input()
    x = re.split(r"(\d+)", z)
    if x[0] in order.keys():
        order[x[0]] += int(x[1])
    else:
        order[x[0]] = int(x[1])
for i, j in order.items():
    print(f"{i}{j}")
    
