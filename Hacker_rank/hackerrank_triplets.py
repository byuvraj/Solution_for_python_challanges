def countTriplets(arr, r):
    count = 0
    dict = {}
    dictPairs = {}
    
    for i in reversed(arr):
            if i*r in dictPairs:
                print(i*r)
                count += dictPairs[i*r]
            if i*r in dict:
                dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]
            dict[i] = dict.get(i, 0) + 1

    return count
if __name__=='__main__':
    n,r=[int(i) for i in input().split()]
    arr=[int(i) for i in input().split()]
    print(countTriplets(arr, r))