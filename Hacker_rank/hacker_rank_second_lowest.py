if __name__ == '__main__':
    stu_lis=[]
    min_=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu_lis.append([name,score])
        min_.append(score)
    min_.sort()
    min_num=min_[0]
    min_.remove(min_num)
    minIn = True
    while minIn:
        if min_[0] == min_num:
            min_.remove(min_num)
        else:
            minIn = False 
    min_num=min_[0]
    res_=[]
    for i in stu_lis:
        if i[1]==min_num:
            res_.append(i[0])
    res_.sort()
    for i in res_:
        print(i)