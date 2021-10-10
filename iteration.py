#iteration statements:
#range(10)  :  0...9
#range(4,10): 4....9
#range(4,10,3): 4,7  (3 is here increment value, hence first 4 will come, then (4+3)=> 7, but not 10)
#range(10,4,-3): 10,7
#range(-10,-5): -10,-9,-8,-7,-6
#range(-10,-5,2): -10,-8,-6
#range(-5,-10,-2): -5,-7,-9

#for temp-var in iteration-data:
#    print(temp-var)
"""
for x in range(10):
    print("ratan",x)

for x in range(4,10):
    print(x)
    

for x in range(4,20,3):
    print(x)

for x in range(20,4,-3):
    print(x)

for x in range(-10,-4):
    print(x)

for x in range(-10,-4,3):
    print(x)

l=[1,2,3,4] #list data
for x in l:
    print(x)

t=(1,2,3)  #tuple data
for x in t:
    print(x)


for x in range(10):
    print(x)
else:
    print("Normal execution")

#in 3 cases "else" block will not execute:
#case1: break statement
for x in range(1,10):
    if x == 4:
        break
    print(x)
else:
    print("Normal execution")

#case2: when we have exception
for x in range(10):
    print(10/0)
else: print("normal execution")

#case3: when we have problematic issue in code, like OS shutdown statement before else statement
import os
for x in range(10):
    print(x)
    os._exit(0)
else:
    print("Normal execution")
"""
######################################
"""
while loop

while(condition):
    body


a=0
while(a<10):
    print("a")
    a=a+1
print("normal execution")








box=[4,25,54,8,7,10]
rev_box=[]
for x in box:
    rev_box[6-x-1]= box[x]
    print(rev_box)
******************************
number= [10,15,2,34,65,47]
l = len(number)
rev_numbers = []
for i in range(l):
    rev_numbers.append(i) = number[l-i-1]
    print(rev_numbers) 

array_list = [1,2,3,4,5,6]
sample_list = []
l = len(array_list)
for i in range(l):
    sample_list.insert(i) = array_list[i]
    kk = sample_list
#    print(array_list(l))
    print(kk)


box=[4,25,54,8,7,10]
rev_box=[]
k = 0
for x in box:
    rev_box.insert(0,x)
    k = k+1
print(rev_box)


a=0
while(a<10):
    print("ratantit")
    a=a+1
else:
    print("Normal execution")

#in three cases else block not executed:
#case 1: break
a=0
while a<10:
    print("ratanit")
    a=a+1
    if a==5:
        break
else:
    print("Noraml execution")
#case 2: exception
a=0
while a<10:
    print("ratanit")
    a=a+1
    print(10/0)
else:
    print("Noraml execution")
#case 3: exception
import os
a=0
while a<10:
    print("ratanit")
    a=a+1
    os.exit(0)
else:
    print("Noraml execution")

difference between for and while loop
for :
    start & ending is there and we do increment or decrement
while:
    check condition and read the data

#Transer statements:
break: 
case1:
for x in range(1,10):
    if x==5:
        break
    print(x)
case2:
if True:
    print("ratanit)
    break
    print("durga")
#it will give syntaxe error: 'break' outside loop, as break statement will run only for loop(for, while), not for if condition.
continue:
if True:
    print("ratanit")
    continue
    print("durga")
#it will give syntaxe error: 'continue' not properly in loop, as continue statement will run only for loop(for, while), not for if condition.
for x in range(10):
    if x==4:
        continue
    print(x)    
    try
    return
"""






















