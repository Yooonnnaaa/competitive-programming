m = input()
s1 = set(input().split())
n = input()
s2 = set(input().split())
x =s1.symmetric_difference(s2)  
li = sorted(map(int, list(x)))
for i in li:
    print(i) 
