num1 = 42 #variable declaration, number
num2 = 2.3 #variable declaration, float
boolean = True #variable declaration, float, boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #initialize tuple
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, access value of list
pizza_toppings.append('Mushrooms') #add item to list
print(person['name']) #log statement, acess value of dictionary
person['name'] = 'George' #change value of list
person['eye_color'] = 'blue' #add value to list
print(fruit[2]) #log statement, access value of tuple

if num1 > 45: #conditional, if statement
    print("It's greater") #log statement
else: #conditional, else statement
    print("It's lower") #log statement

if len(string) < 5: #length check ,conditional, if statement
    print("It's a short word!") #log statement
elif len(string) > 15: #length check ,conditional, else if statement
    print("It's a long word!") #log statement
else: #conditional, else statement
    print("Just right!") #log statement

for x in range(5): #for loop, end 
    print(x) #log statement
for x in range(2,5): #for loop, start, end
    print(x) #log statement
for x in range(2,10,3):
    print(x) #log statement
x = 0 # initialize variable
while(x < 5): # while loop, conditional
    print(x) #log statement
    x += 1 #change value, increment

pizza_toppings.pop() #calling function
pizza_toppings.pop(1) #calling function, argument

print(person) #log statement
person.pop('eye_color') #log statement
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': # if statement
        continue #continue statement
    print('After 1st if statement') # log
    if topping == 'Olives': #if statement
        break #break statement

def print_hello_ten_times(): #define function, 
    for num in range(10): # for loop, 
        print('Hello') #log statement

print_hello_ten_times() #calling function

def print_hello_x_times(x): #defining function, parameter
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #define function, default parameter
    for num in range(x): #for loop, argument
        print('Hello') #log statement

print_hello_x_or_ten_times() #calling function
print_hello_x_or_ten_times(4) #calling function, argument


""" 
Bonus section #multi-line-comment
"""

# print(num3)  #log statement, #single-line-comment. 
# num3 = 72 #single-line-comment, initialize variable
# fruit[0] = 'cranberry' #single-line-comment, TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])   #single-line-comment, KeyError: 'favorite_team'
# print(pizza_toppings[7])  #single-line-comment, IndexError: list index out of range
#   print(boolean)  #single-line-comment, boolean
# fruit.append('raspberry')  #single-line-comment,  AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  #single-line-comment, AttributeError: 'tuple' object has no attribute 'pop'