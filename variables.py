"""
Python variables:

Basic Data types:
    Numbers: int, float
    String: str
    Boolean: bool

Types of variables:
1. Local variable: The variable declared inside the function  and also the variable declare as function argument is local var. 
2. Global variable: The variable declared outside the function

Functions: 
Case1:
def disp1():
    print("Ratant")
def disp2(name):                     #local variable
    print("good morning",name)
def disp3():     
    name= 'ratan'                    #local variable
    print("good morning",name)
disp1
disp2("ratan")

Case2:
name= "ratan"                        #Global variable
def disp1():
    print("This is my name:",name)
def disp2():
    print("This is my name:",name)

disp1()
disp2()

Case3:
a,b=10,20
def add(x,y):
    print(x+y)
    print(a+b)

def mul(x,y):
    print(x*y)
    print(a*b)

add(3,3)
mul(4,4)


Case4:  #in this case the priority will goes to local variable, if we have same var in both global and local. 
a,b=10,20
def add(a,b):
    print(a+b)
    print(a+b)

def mul(a,b):
    print(a*b)
    print(a*b)

add(3,3)
mul(4,4)

Case5: If we want to use Global variable specifically, then we need to provide globals() keywrd infornt of the var.
a,b=10,20
def add(a,b):
    print(a+b)
    print(globals()['a']+ globals()['b'])

def mul(a,b):
    print(a*b)
    print(globals()['a']*b)

add(3,3)
mul(4,4)

Case6: Inside the function, once we use Global var, then with the same name , it is not possible declare local var.
#UnboundLocalError: local variable 'name' referenced before assignment 
name= "ratan"
def disp():
    print(name)
    name="durga"
    print(name)

disp()

Case7:
x=10
def disp():
    x=1
    x=x+10
    print (x)
print(x)
disp()

case8:
x=10
def disp():
    x=1
    x=x+10
    print (x)
print(x)
disp()

Case9: if we have declared global var, then with the same name we cannot declare local var. UnboundLocalError: local variable 'x' referenced before assignment
x=10
def disp():
    x=x+10  #here x+10, in which x cannot be locally defined again, as we have declaregloabl var x(same name)
    print (x)
print(x)
disp()

Case10: the above case can be solved, if we use global keyword.
x=10
def disp():
    global x
    x=x+10
    print (x)
disp()

TypeError: whenever we combine two different types of data, concat not possible
ValueError: whenever we try to conversion
NameError: when Name is not defined
unboundLocalError: Once we use global variable with the same name local var, then we got unbounded local variable

Number Systems:
binary : base 2:  0b 0B
octal : base 8:   0O  0o
decimal: base 10
hexa decimal: base 16

#Binary: base 2: 0b 0B
a= 0b010101010
b= 0B111111
print(a)
print(b)

#Octal: base 8: 0o 0O
a= 0o12237467
b= 0O12272372
print(a)
print(b)

#decimal :
a=10
print(a)
b=9090
print(b)

#Hexa decimal: 0-9 A-f : base16: 0X 0x
a=0x000000aF
print(a)

separator:
print(10,2,3,4, sep='****')
print(1,2,3,4,5,6, sep='+=+=')

#To find out ASCII value of any character/number:
c = input("Enter a character:")
print(ord(c))

#to find binary/octal/hexadecimal
a=100
print(bin(a))
print(oct(a))
print(hex(a))

a= 12.5555
print('%g'%a)  #%g will give 6 digit output

a= 1222222222222222.5555
print('%f'%a)  #%g will give 17 digit output
#output: 1222222222222222.500000

%s: String
%d: int
%f & %g : float

python identifier:

    rule 1: a-z A-Z __ but should not start with numerics and special symbols
    class 123hjuk  --invalid
    class hg124    --valid
    class *ghty    --invalid

    rule 2: case sensitive
    num=10   --valid
    Num=10   --invalid

    rule 3: no length limit
    class myclass()  #although there is no limit, but in real world, we do not give a lengthy names. 

    rule4: Duplicate (invalid), but variable duplicacy is allowed as we are reassigning. 
    class Myclass
    class Myclass

    rule5: keywords are not identifiers
    try=100  --invalid
    self=100  -invalid

    rule6: predefined class name we can use as identifiers but it is not recommended. 
    ABC=10  

#Global keyword
inside the function with keyword "global", we can declare global keyword
case1:
def disp():
    global s
    s="ratan"
    print(s)

case2: 
s=10
def disp():
    print(s) #SyntaxError: name 's' is used prior to global declaration
    global s
    s= 20
    print(s)

case3:
s=10
def disp():
    print(s) #UnboundLocalError: local variable 's' referenced before assignment
    s= 20
    print(s)
disp()
print(s)

#nonlocal variable
    #to use outer function variable in inside function, we use nonlocal variables
def outer():
    name1=10
    def inner():
        nonlocal name1
        name1 = 20
    print(name1)
    inner()  #calling inner function
    print(name1)
outer()
"""





