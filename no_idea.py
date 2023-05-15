count = 0
x = list(map(int, input().split()))
arr = list(map(int, input().split()))
s1 = list(map(int, input().split()))
s2 = list(map(int,input().split()))
for i in arr:
    if i in s1:
        count += 1
    elif i in s2:
        count -= 1
    else:
        pass
print(count)
