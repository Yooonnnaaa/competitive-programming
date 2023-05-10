if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)
    x = max(arr_list)
    y = arr_list.count(x)
    for i in range(y):
        arr_list.remove(x)
    print(max(arr_list))





