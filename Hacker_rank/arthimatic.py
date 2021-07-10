import datetime
from numpy import array
now =datetime.datetime.now()
class Case():
    def __init__(self, A, N):
        self.A = sorted(array(A))
        self.N = N
    def subArray(self):
        diff = []
        for i in range(1,self.N):
            diff.append(self.A[i-1]-self.A[i])
        diff.sort()
        univalues=[]
        unicount=0
        for var in diff :
            if var != 0:
                if not var in univalues:
                    univalues.append(var)
                    unicount+=1

        count=[0 for i in range(unicount)]
        for j in range(unicount):
            for k in diff:
                if univalues[j] == k :
                    count[j]=count[j]+1
        count.sort()
        return count[-1]
t = int(input())
for i in range(1,t+1):
    n = int(input())
    a = [int(k) for k in input().split()]
    case = Case(a,n)
    print("Case #{}: {}".format(i,case.subArray()+1))
end = datetime.datetime.now()
print(end.second-now.second)