from collections import defaultdict
n = list(map(int, input().split()))
group_A , group_B = [], []
d = defaultdict(list)
for i in range(n[0]):
    x = input()
    group_A.append(x)
for j in range(n[1]):
    y = input()
    group_B.append(y)
for k in group_B:
    if k not in group_A:
        d[k].append(-1)
    elif len(d[k])> 0:
        pass
    else:
        for l in range(len(group_A)):
            if k == group_A[l]:
                d[k].append(l+1)
for m in group_B:
    print(*d[m])
