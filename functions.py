"""
#python functions:
    1. Predefined functions
    2. user-defined functions

we use function to write the logic one time and can call the function multiple times. 
def disp():   #declaring function
    print("ratan")

disp()  #calling the function


def disp(a,b):
    print(a+b)

disp(1,2)

x,y=3,4
def disp(a,b):
    print(a+b)
    print(x+y)
def disp1(a,b):
    print(a+b)
    print(x+y)

disp(1,2)
disp1(5,6)


Function Arguments:


1. Default arguments:
def disp(eid=111,ename="ratan",esal=1000.98):
    print(eid,ename,esal)
    print("****************")
disp()
disp(222)
disp(333,"durga")
disp(222,1000.87)


#2. Required argument: tere are no values and it will require argments from user
def disp(eid,ename,esal):
    print(eid, ename, esal)
    print("***********")
    
disp(111,"ratan",12133.567 )

def disp(eid,ename="ratan",esal=1000.87):  #mix of default and required arguements
    print(eid, ename, esal)
    print("***********")
    
disp(111)


def disp(eid,ename="ratan",esal): #invalid #Non-default argument follows default argument, means once we provided default arguement, then followed arguements should be default. 
    print(eid, ename, esal)
    print("***********")
    
disp(111)

def disp(eid,ename,esal= 10998.87): #valid
    print(eid, ename, esal)
    print("***********")
    
disp(111,"ratant")


#3. Keyword argument: we pass arguement keyname and value while caling the function. In that case, order is not important
def disp(eid,ename,esal): 
    print(eid, ename, esal)
    print("***********")
    
disp(eid=111,ename="ratant",esal=123.45)
disp(ename="durga",esal=88978,eid=111)
disp("durga",esal=88978,eid=111)

def disp(eid,ename,esal): 
    print(eid, ename, esal)
    print("***********")
    
disp(eid=111,ename="ratant",esal=123.45)
disp(ename="durga",esal=88978,eid=111)
#disp("durga",esal=88978,eid=111) #TypeError: disp() got multiple values for argument 'eid'
disp(111,ename="ratanit",esal=8787)
#disp(111,ename="ratanit",8787) #SyntaxError: positional argument follows keyword argument; once the keyword argument started, next all should be keyword arguments


#4. var arguement

#case1:
def disp(*a):
    for x in a:
        print(x)
print()
print(1,2,3)
print("ratantit", "durga")
print(1,2.3)
print(1,2,3.5,"ratant")

#case2:
def disp(name,*a):
    print(name)
    for x in a:
        print(x)
#disp()  #TypeError: disp() missing 1 required positional argument: 'name', as it is a required argument
disp(1,'a')
disp("ratan","durga")
disp(1,1.2)


#case3:
def disp(*a, name):
    print(name)
    for x in a:
        print(x)
#disp("ratanit") #TypeError: disp() missing 1 required keyword-only argument: 'name'
disp(1,2,3,"ratant",name=10)


def disp():
    print("ratan")
    return 10
x= disp()
print(x)
#or
print(disp())  #returning the value


#case2:
def disp():
    print("ratant")
    return 10
    return 20  #it will be ignored, as we can return only one value
print(disp())

#Case3
def disp():
    if 10>20:
        return 10
    else:
        return 20 #if we want to return other than first value, then we can go with condotion statement.
x= disp()
print(disp())

#case4:
def disp():
    print("Ratanat")
x= disp()
print(x) #since we didnot return anything in function, then it will return "None". 

"""
from array import *

arr= array('i',[1,2,3,4,5])
#arr= [1,2,3,4,5]
n= len(arr)
mul=1

for i in range(0,n):
    mul=mul*arr[i]

mul=(mul%10)%10
print(mul)




