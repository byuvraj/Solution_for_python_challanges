if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    avg=0
    print(marks)
    n_ =len(marks)
    for i in range(0,n_):
        avg=marks[i]+avg
    avg = avg/n_
    print("{0:.2f}".format(avg))