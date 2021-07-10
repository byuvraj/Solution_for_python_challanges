N = int(input())
arr=[]
for i in range(N):
    ins=[i for i in input().split()]
    if ins[0] == "insert":
        arr.insert(int(ins[1]),int(ins[2]))
    elif ins[0] == "remove":
        arr.remove(int(ins[1]))
    elif ins[0] == "append":
        arr.append(int(ins[1]))
    elif ins[0] == "sort":
        arr.sort()
    elif ins[0] == "pop":
        arr.pop()
    elif ins[0] == "reverse":
        arr.reverse()
    else:
        print(arr)