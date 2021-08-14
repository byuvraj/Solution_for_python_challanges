
def hourglassSum(arr):
    ans = 0
    sol = 0
    for i in range(0,4):
        for j in range(0,4):
            ans = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            sol = max(sol,ans)
    return sol
if __name__ == '__main__':
    arr=[]
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
