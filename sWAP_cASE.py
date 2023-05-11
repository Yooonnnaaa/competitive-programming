def swap_case(s):
    x = []
    for i in s:
        if i == i.upper():
            y = i.lower()
            x.append(y)   
        else:
            y = i.upper()
            x.append(y)
    z = "".join(x)
    return z

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
