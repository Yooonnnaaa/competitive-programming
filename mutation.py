def mutate_string(string, position, character):
    x = []
    for i in string:
        x.append(i)
    x[position] = character
    y = "".join(x)
    return y

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
