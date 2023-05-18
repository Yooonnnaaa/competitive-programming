from itertools import combinations
n = int(input())
str = input().split()
index = int(input())
possibility = list(combinations(str, index))
counter = 0
for i in possibility:
    if "a" in i:
        counter += 1
print(counter/len(possibility))
