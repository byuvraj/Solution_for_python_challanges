def pair():
    n = int(input())
    ar = [int(i) for i in input().split()]
    ar.sort()
    tem=ar
    print(ar)
    pair=0
    for i in range(1,n+1,2):
        if i==n:
            break
        if ar[i-1] == tem[i]:
            ar[i-1]=0
            ar[i]=0
            print(("Pair found"))
            pair += 1
        

    print(ar)
    print(pair)


if __name__ =="__main__":
    pair()