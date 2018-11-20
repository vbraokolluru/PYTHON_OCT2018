#*** Loop function in print

#x={1:'raju',2:'hyd',3:'first'}
#print([i for i in x.items()])
#print([i for i in x.keys()])

# function definationn and calling
def disp():
    print ('python program')
disp()    

#Function with arguments
def stddt(name,rank):
    print('student Name: ' , name,'student Rank: ', rank )
stddt('ram',2)

# function with default arguments

def add(a,c,b=40):
    tot = a+b+c
    print ('sum is:  ' , tot)

add(10,20,5)
add(10,20)

# Function with nothing return 
def pnt():
    print('hello first function')
    return 
pnt()

# function with return value
def add(a,b,c):
    tot = a+b+c
    return tot

total = add(10,5,20)
print(total)

# input as variable number of arguments for function
def dis(name,*argv):
    print('student details: ', name)
    for i in argv:
        print (i)
#    return

math=input('enter math marks:')
eng=input('enter math eng:')
social=input('enter math social:')

dis('xyz',math,eng,social)

# input as keyword arguments for function

def kwargsfun(a,**kwargs):  
    print('roll number: ' , a)
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
kwargsfun(10,stname ='Abhi',stclass= 2, rank=3,school='dps')


# Global and local variables 
sum = 0
def add(a,c,b):
    sum = a+b+c
    print ('in function sum : ' , sum )
    return sum
print ('before function call sum is : ' , sum )
add(10,20,5)
print ('after function call sum : ' , sum )


# Fibonacci numbers module
print ("Module program calling")
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()

fib(50)

# return Fibonacci series up to n write in list
def fib2(n):  
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fib2(100)
#dir(functions)
locals()
globals()

