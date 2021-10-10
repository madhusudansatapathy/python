from array import *
"""
vals = array('i',[4,5,6,7,8])
characters = array('u',['a','e','i'])
#print(vals)
n= len(vals)
for i in range(n):
    print(vals[i])
for e in characters:
    print(e)
"""
arr = array('i',[2,3,4,5,6,7,8])
new_arr = array('i',[])
n= len(arr)
x=0
y=n-1

#print(n)
#for i in range(n):
#    print(arr[i])
#"""
for i in range(n):
    if arr[i] % 2 == 0:
        arr.insert(y,arr[i])
        y= y-1
    else:
        arr.insert(x,arr[i])
        x=x+1
print(arr)

#"""

