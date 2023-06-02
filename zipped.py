n = list(map(int, input().split()))
li = []
av = []
for i in range(n[1]):
    stu = list(map(float, input().split()))
    li.append(stu)
for j in li:
    av += [j]
main = list(zip(*av))
for k in main:
    m = sum(k)/n[1]
    print(f"{m:.1f}")
