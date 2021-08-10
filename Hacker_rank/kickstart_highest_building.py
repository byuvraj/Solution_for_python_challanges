t = int(input())
for i in range(1,t+1):
    n , a ,b , c = [int(j) for j in input().split(" ")]
    assert 1 <= c and c <= n
    assert c <= a and a <= n
    assert c <= b and b <= n

    
    print("Case #{}:".format(i),end='')
    if (a + b - c) > n or ((a + b - c) == 1 and n >= 2):
        print(' IMPOSSIBLE')
    elif n==1:
        print(' 1')
    elif n==2:
        if c==2:
            print(' 1 1')
        elif a == 2:
            print(' 1 2')
        elif b == 2:
            print(' 2 1')
        else :
            assert False 
    else:
        heights = []
        for i in range(0,a-c):
            heights.append(2)
        for i in range(0,c):
            heights.append(3)
        for i in range(0,b-c):
            heights.append(2)
        if  (n - (a + b -c)) > 0:
            extra = n - (a + b -c)
            heights.insert(1,extra)
        for i in range(0,n):
            if i+1==n:
                print('',heights[i])
            else:
                print('',heights[i],end='')
