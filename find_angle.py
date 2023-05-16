import math
ab = int(input())
bc = int(input())
x = (math.atan(ab/bc))
y = round(math.degrees(x))
print(f"{y}\N{DEGREE SIGN}")
