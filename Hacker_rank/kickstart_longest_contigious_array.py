#Problem statement is mentioned below
N = int(input())
for i in range(1,N+1):
    n_i = int(input())
    nums = [int(j) for j in input().split()]
    dif = []
    for k in range(1,n_i):
        dif.append(nums[k] - nums[k-1])
    d_ = 1
    ans = 1
    for k in range(1,n_i-1):
        if dif[k] == dif[k-1]:
            d_+=1
        else:
            d_ = 1
        ans = max(ans , d_)
    print("Case #{}: {}".format(i,ans+1))

"""Problem
An arithmetic array is an array that contains at least two integers and 
the differences between consecutive integers are equal. 
For example, 
[9, 10], 
[3, 3, 3], 
and [9, 7, 5, 3] 
are arithmetic arrays, 
while [1, 3, 3, 7], 
[2, 1, 2], and [1, 2, 4] 
are not arithmetic arrays.

Sarasvati has an array of N non-negative integers. 
The i-th integer of the array is Ai. She wants to choose a 
contiguous arithmetic subarray from her array that has the maximum length. 
Please help her to determine the length of the longest contiguous arithmetic subarray.

Input
The first line of the input gives the number of test cases, T. 
T test cases follow. Each test case begins with a line containing the integer N. 
The second line contains N integers. The i-th integer is Ai.

Output
For each test case, output one line containing Case #x: y, 
where x is the test case number (starting from 1) and y is the length of the 
longest contiguous arithmetic subarray.
"""