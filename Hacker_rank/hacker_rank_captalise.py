
# Complete the solve function below.
from os import sep


def solve(s):
    s
    n = len(s)
    try:
        for i in range(n):
            if s[i]!=' ' and i==0:
                s=s[i].upper()+s[1:]
            elif s[i] ==' ' and s[i+1]!=' ':
                s=s[:i] +' ' + s[i+1].upper()+s[i+2:]
    except IndexError:
            return s
    return s
    # res=''
    # for j in capWord:
    #     if res=='0':
    #         res=j
    #     else:
    #         res=res+' '+j
    # return(res)
if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)