if __name__ == '__main__':
    n = int(input())
    x = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i , v in student_marks.items():
        if i == query_name:
            
            for j in v:
                x += j
            avr = x*1.00/3
    formatted_avr = "{:.2f}".format(avr)
    print(formatted_avr)
