class Buy():
    def __init__(self, no_of_houses,buyer_bugget, price_of_ith_house):
        self.no_of_houses = no_of_houses
        self.buyer_bugget = buyer_bugget
        self.price_of_ith_house = price_of_ith_house
        
T = int(input())
for i in range(1,T+1) :
    N, B = [int(j) for j in input().split()]
    A = [int(k) for k in input().split()]
    buy = Buy(N,B,A)
    buy.price_of_ith_house.sort()
    possible_number_of_houses = 0
    for j in range (N):
        buy.buyer_bugget=buy.buyer_bugget - buy.price_of_ith_house[j]
        if buy.buyer_bugget <0:
            break
        possible_number_of_houses +=1
    print("Case #{}: {}".format(i, possible_number_of_houses))