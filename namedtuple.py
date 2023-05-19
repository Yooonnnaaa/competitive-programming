from collections import namedtuple
n = int(input())
x = ",".join(input().split())
student = namedtuple("student", x)
sum = 0
for i in range(n):
    result = input().split()
    x = student(*result)
    sum += int(x.MARKS)
print("{:2f}".format(sum/n))
