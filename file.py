#Data Types 
num1 = 42 #Numbers
num2 = 2.3 #Numbers
boolean = True #Boolean
string = 'Hello World' #String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List Initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #Tuples initialize
print(type(fruit)) # Type check
print(pizza_toppings[1]) #list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) # Dictionary access
person['name'] = 'George' #Dictionary change value
person['eye_color'] = 'blue' #add value
print(fruit[2]) #Tuples access value

if num1 > 45: #if
    print("It's greater")
else: #else
    print("It's lower")

if len(string) < 5: #if
    print("It's a short word!")
elif len(string) > 15: #else if
    print("It's a long word!")
else: #else
    print("Just right!")

for x in range(5): #for loop start at 0 end at 4 increment +1
    print(x)
for x in range(2,5): #for loop start at 2 end at 4 increment +1
    print(x)
for x in range(2,10,3): #for loop start at 2 increment +3
    print(x)
x = 0
while(x < 5): #while loop start at 0 stop at 4 increment +1
    print(x)
    x += 1

pizza_toppings.pop() #remove end of list
pizza_toppings.pop(1) #remove 2nd of list

print(person) 
person.pop('eye_color') #remove dictionary
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if
        continue #continue allows you to skip the next line of code
    print('After 1st if statement')
    if topping == 'Olives':
        break# ends for loop

def print_hello_ten_times(): #function 
    for num in range(10): # for loop 
        print('Hello') #log statement

print_hello_ten_times() #function call

def print_hello_x_times(x): #function and x is the parameter
    for num in range(x): #argument
        print('Hello') #argument

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function and x is the parameter
    for num in range(x): #argument for loop
        print('Hello') #argument

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section ##multi line comment
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)