from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
li = list(map(str,(list(product(a,b)))))
car = " ".join(li)
print(car)
