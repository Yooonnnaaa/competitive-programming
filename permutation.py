from itertools import permutations
word = input().split()
x = sorted(permutations(word[0],int(word[1])))

for i in x:
    j = "".join(i)
    print(j)
