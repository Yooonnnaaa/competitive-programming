if __name__ == '__main__':
    dic = {}
    both_list = []
    score_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic[name] = score
        score_list.append(score)
    x= min(score_list)
    y = score_list.count(x)
    for i in range(y):
        score_list.remove(x)
    for i,v in dic.items():
        if v == min(score_list):
            both_list.append(i)
            sort = sorted(both_list)
    for i in sort:
        print(i)  
        
