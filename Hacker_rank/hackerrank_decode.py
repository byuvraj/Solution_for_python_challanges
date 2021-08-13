import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(list(matrix_item))
st=''
for i in matrix:
    st =st+str(i[0])
for i in matrix:
    st =st+str(i[1])
for i in matrix:
    st =st+str(i[2])
ans=''
for i in st:
    while i.isalnum():
        ans =ans+i
        break
    else:
        ans=ans+' '
    while '  ' in ans:
        ans= ans.replace('  ',' ')
l=list(ans)
[l.pop(-1)]and[l[-1]==' ']
ans=str(''.join(l))

print(ans,end='')
print('#  %!')
