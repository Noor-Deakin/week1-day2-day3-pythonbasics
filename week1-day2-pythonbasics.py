#python basics 
#While loops 
#basic syntax for a while loop
i=1
while i<=5:#condition enforced 
    print(i)#task assigned within the loop 
    i=i+1
print("done")

#building a car game using a while loop 
print("welcome to the car game big drip ")

while True: 
    user_command = input("Please enter your command to start/stop/quit the game : ").lower()
    if user_command == "start":
        print("the car has started")
    elif user_command == "stop":
        print("the car has stopped")
    elif user_command == "quit":
        print("you quit the game man!!")
        break
    else:
        print("unable to understand that , my bad")

#FOR LOOPS 
#basic syntax 
for items in range(1,10):#here range is a function 
    print(items)

#SHOPPING CART CALCULATOR 
total =0 
shopping_cart = 10,20,30,40,50
for items in shopping_cart:
    total+=items
print("total = "+str(total))

#LISTS 
#basic syntax
names = ['priyanka','noor','aman','preet']
print(names)#[] brackets can be used to specify index of the list 

# program to find largest number in a list 
num_list = [1,2,3,4,5,6]
max_number = num_list[0]
for i in num_list:
    if i > max_number:
        max_number = i

print("max_number : "+str(max_number))

#questions based on list 
# largest and smallest numbers using nested loops 
question_list1 = [23,56,77,43,21,66]
max_number = question_list1[0]
min_number = question_list1[1]

for i in question_list1:
    for j in question_list1:
        if j > max_number:
            max_number = j
        if j < min_number:
            min_number = j 

print("max number = "+ str(max_number))
print("min number =  "+ str(min_number))

#2D LISTS
#basically lists within lists can be made 
#basic syntax 
matrix  = [
    [2,5,3],
    [5,9,7],
    [9,4,6]
]
for row in matrix:
    for item in row:
        print(item)

#LIST METHODS (Functions based on lists )

numbers = [23,45,76,20,32]
#Append - to add any item at end of list 
numbers.append(11)
print(numbers)

#Insert - is used to insert a number at a particular index in 
#list 
numbers.insert(0,10)

#Remove - to remove a particular item from list 
numbers.remove(45)
print(numbers)

# #pop - to remove last item from a list 
numbers.pop()

# #to check existence of an item in a list INDEX function is used
print(numbers.index(10))

# #apart from that 'in' operator can also be used
# #for example 
print(10 in numbers) #provides answer in boolean avoids error

# #SORT - method is used to arrange items of a list in ascending 
# #or descending order 
# #ASCENDING 
numbers.sort()
print(numbers)

#DESCENDING 
numbers.sort()
numbers.reverse()
print(numbers)

#clear - clear function is used to clear the whole list 
# numbers.clear()

#A PROGRAMME TO REMOVE DUPLICATES IN A LIST 
#given list of numbers 
A_list = [23,67,45,21,45,99]
empty_list = []

for items in A_list:
    if items not in empty_list:
        empty_list.append(items)

print("original list = "+str(A_list))
print("fixed list  = "+str(empty_list))

#A PROGRAMME TO ROTATE A LIST by K POSITIONS 
b_list = [10,20,30,40,50]
k = 2 
for items in range(k):#range here creates sequence of numbers 
    #telling the loop number of times to repeat 
    last = b_list.pop()#pop removes the last element 
    b_list.insert(0,last)#insert adds it at the beginning 

print("list after rotating by ",k," positions : "+str(b_list))

#TUPLES 
#a datatype that is similar to lists but immatuable i.e.
#cannot be modified 
c_list = (1,2,3)
#c_list[0]=10#no changes can be made in a tuple 
print(c_list[0])


#unpacking - helps to avoid programme complexity when using 
#lists or tuples 
#for example 
coordinates = (1,2,3)
x,y,z = coordinates
print(y)


#DICTIONARY 
#A datatype in python used to store key value pairs where each key is associated with a value 
#for example , 
customer = {

    "name":"Gurnoor Singh",
    "age":20,
    "is_verified" :True
}

print(customer.get("name"))
customer["birthdate"] = "2005 feb 1 "
print(customer.get("birthdate"))

#Write a programme that takes input as digits and returns output as words
print("Number conversion programme ")
phn_number = input("Please enter your phone number : ")
digits_mapping = {
    "1":"One",
    "2":"two",
    "3":"three",
    "4":"four"
}

output = ""
for ch in phn_number:
    output += digits_mapping.get(ch,"!") + " "
print(output)

#FUNCTIONS -> refers to container of a code or a programme that perform a specific task 
#def here is used to define a function
#parameters are used to pass info to a function 

#basic syntax 
def greet_user(first_name,last_name):#first_name in this case is a parameter
    print(f"hi {first_name} {last_name} ")
    print("how you doin ? ")

print("start")
greet_user("singh",first_name="noor")#an example of keyword argument here is first_name. 
#keyword arg are used mainly with numbers to avoid confusion 
print("finish")

#mini programme to calculate square of a function 
def square(value):
    return value*value

print("hello and welcome to number square programme")
number = int(input("Please enter your desired value - "))
result = square(number)
print("square value = "+str(result))

