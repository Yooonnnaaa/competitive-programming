n = int(input())
for i in range(n):
    x = input().split()
    try:
        z =int(x[0])//int(x[1])
        print(z)
    except ZeroDivisionError as a:
        print("Error Code:",a)
    except ValueError as b:
        print("Error Code:", b)
