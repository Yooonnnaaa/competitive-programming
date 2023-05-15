def count_substring(string, sub_string):
    x=0
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            y=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    y=0
                    
            if y==1:
                x += 1
    return x

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
