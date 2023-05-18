from collections import Counter
x =[]
price = 0
n = int(input())
size = list(map(int, input().split()))
customer = int(input())
counter = Counter(size)
for i in range(customer):
    no = list(map(int, input().split()))
    if no[0]in counter.keys():
        price += no[1] 
        counter[no[0]] -= 1
        if counter[no[0]] == 0:
            del counter[no[0]]
print(price)
    
