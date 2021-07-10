n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
max=arr[-1]
arr.remove(max)
maxIn = True
while maxIn:
    if arr[-1] == max:
        arr.remove(max)
    else:
        maxIn = False 
print(arr[-1])