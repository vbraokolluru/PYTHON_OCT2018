# Looping programs

# while Loops

count = 1
while count < 3:
    name = input('enter student name: ')
    marks = int(input('enter student marks: '))
    print('student name----: ', name, 'Marks----: ', marks)
    count = count + 1
print('end of while and count is:', count)

count = 0
while (count < 3):    
    count = count+1
    print("Hello python:", count)
    
computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
computer_brands[0]
computer_brands[1]
computer_brands[2]
computer_brands[3]

len(computer_brands)

i = 0
while i < len(computer_brands): # i < 4
    print (computer_brands[i])
    i = i + 1
print('sucessfull')

cont = 'y'
while cont == 'y':
    name = input('enter student name: ')
    marks = int(input('enter student marks: '))
    print('student name----: ', name, 'Marks----: ', marks)
    cont=input('want to continue -y- else press any other')
print('end of while and count is:', cont)

    
#For Loops

for i in range(0,100):
    print(i)
print('range for loop done sucessfully')    


l1 = [1,2,3,4,5,6]
for i in l1:
    print(i)
print('for loop done sucessfully' )
    
#Examples
computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
for brands in computer_brands:
    print (brands)

numbers = [1,10,20,30,40,50]
sum = 0
for number in numbers:
    sum = sum + number
print (sum)

for i in range(1,10):
    print (i)
    
li = [4,5,6,2,9,1]    
for i in range(0, len(li)):
    print (li[i], end="     ")

#1
#2   2
#3   3   3
#4   4   4   4
#5   5   5   5   5


for i in range(1, 6):
    for j in range(i):
         print(j, end=' ')
    print()

# continue statement
# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks': 
    if letter == 'e' or letter == 's':
         continue
    print ('Current Letter :', letter)

#Break statement
for letter in 'geeksforgeeks': 
 
    # break the loop as soon it sees 'e' 
    # or 's'
    if letter == 'e' or letter == 's':
         break
 
print ('Current Letter :', letter)  

#pass statement
for letter in 'geeksforgeeks':
    pass
print ('Last Letter :', letter)

# Write tables.
for x in range(1, 11):
    for y in range(1, 11):
        print ('%d * %d = %d' % (x, y, x*y))  