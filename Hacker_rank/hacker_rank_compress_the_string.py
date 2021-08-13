# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
accur={}
ac=0
n=len(s)-1
for i in range(0,n):
    if s[i] in accur:
        accur[s[i]]+=1
    else:
        accur[s[i]]=1
    if not s[i]==s[i+1]:       
        print((accur[s[i]],int(s[i])),'',end='')
        accur[s[i]]=0
    if not i<n-1:
        print((accur[s[i]]+1,int(s[i])),'',end='')
if s[-1]!=s[-2]:
    print((1,int(s[-1])),'',end='')