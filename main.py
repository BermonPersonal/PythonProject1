#remember that indentations are the most important part of python
#this is how you print basic text to the console
print("Hello and welcome to hell bitch.")
print("It is nice and toastie in here.")

#Variables and how to use them in python 👇

#strings:
first_name = 'Bermon'
food = 'pasta'
print(f"Hello, {first_name}.")
print(f"You're favourite food is {food}.")

#integer:
age = 21
food_amount = 3
print(f"You are {age} years old.")
print(f"The amount of {food} that you can eat is {food_amount}.")

#float
price = 10.99
gpa = 3.9
print(f"The price is ${price}.")
print(f"Your GPA is {gpa}.")

#boolean
is_human = False
is_student = True
print(f"Are you human? -> {is_human}")

#if statement
if is_human:
     print("You are a human.")
else:
     print("You are not a human.")

if is_student:
     print("You are a student.")
else:
     print("You are not a student.")

#for loops
#making use of range to set a specific range for the for loop
for count in range(5, 11):
     print(count)
     count += 1

#Makign use of step fucntion within range fucntion
#                  start,stop,step
for count in range(1,    10,  2):
     print(count)

#Looping through dictionaries or other list structures
foods = ['pasta', 'pizza', 'alfredo']
for food in foods:
     print(food)

#switch cases


#for each loops
