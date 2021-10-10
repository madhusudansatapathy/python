
"""
n=123

print(n%100)
print(n/100)

if (n%10 ==0):
    l=n//10
    n=l
else:
    n=n//10
print(n)
"""
#Even-odd sorting
from array import *
arr = array('i',[2,3,4,59,98,76,12,35,67,8])
n= len(arr)
y=-1

for i in range(n):
    if arr[i] % 2 == 0:
        y= y+1
        temp=arr[i]
        arr[i]=arr[y]
        arr[y]=temp
        
print(arr)
