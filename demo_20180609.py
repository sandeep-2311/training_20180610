"""""

This file covers the following topics
1. Tuples, set, boolean datatype
2. Conditional statement
3. Looping statement
4. Break and continue


# tuples
# how to declare

my_tuple = ('a', 'b', 'c')
my_list = ['a', 'b', 'c']
my_set = set(['a', 'b', 'x'])
my_list2 = list()
print(my_set)
print(type(set(my_list)), set(my_list))
unique_char = list()

for item in my_list:
    if item in unique_char:
        continue
    unique_char.append(item)

print (unique_char)

if type(my_list) is list:
    print("this is list")

def func_1():
    print ("This is function 1")

if my_list2:
    print ("this is list 2")
else:
    print("My list 2 is blank")



Looping


1. for loop

first = int(input("Enter the first number"))
print(type(first), first)

second = int(input("Enter the second number"))

for item in range(first, second, 1):
    print(item)



2. while loop


x = 0
while True:
    if x == 11:
        break
    print(x)
    x += 1

"""
"""
Assignments
1. print maximum value from two variables
2. print minimum value from two variables
3. print maximum value from 10 variables
4. print the minimum value from 10 variables

"""


#to print the maximum of two numbers
"""
first = int(input("enter the first number"))
second = int(input("enter the second number"))

if first > second:
 print("first number is greater")
else:
 print("second number is greater")

first = int(input("enter the first nunmer"))
second = int(input("enter the second number"))
if first < second: 
    print("first number is smaller")
else:
    print("second number is smaller")

"""
#to find the maximum  from 10 variables

value = int(input("enter the range  "))
max =0
for item in range(1, value, 1):
    item = int(input(" Enter ur choice of number :- ")
               if max > value (item)
                   max = value (item)

print("The maximum number of the list is :- " max )

