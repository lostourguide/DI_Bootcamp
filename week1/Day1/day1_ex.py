#Exercise 1 : Hello World
#Print the following output in one line of code:
print("hello world\nhello world\nhello world\nhello world")

#Exercise 2 : Some Math
#Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
print((99^3) * 8)

#Exercise 3 : What is the output ?
#Predict the output of the following code snippets:
# if 5 < 3:
#     print("true")
# else:
#     print("false")
# if 3 == 3:
#     print("true")
# else:
#     print("false")
# if 3 == "3":
#     print("true")
# else:
#     print("false")
# if "3" > 3:
#     print("true")
# else:
#     print("false")
# if "Hello" == "hello":
#     print("true")
# else:
#     print("false")
#Honestly, I did not understand fully above excercise, nervermind...thanks Aaron.

#Exercise 4 : Your computer brand
#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
computer_brand = "Asus"
print(f"I have a {computer_brand} computer.")


#Exercise 5 : Your information
#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
#Have your code print the info message.
#Run your code
name = "Ryan Bigglesworth"
age = 46
shoe_size = 44
info = f'hello, peasant, I am {name}. I am {age} years old and I wear size {shoe_size} shoes. I am dubm.'
print(info)


#Exercise 6 : A & B
#Create two variables, a and b.
#Each variable value should be a number.
#If a is bigger then b, have your code print Hello World.
a = 10
b = 1
if a > b:
    print('monkey')


#Exercise 7 : Odd or Even
#Write code that asks the user for a number and determines whether this number is odd or even.
number = int(input("enter a number"))
if number % 2==0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")



#Exercise 8 : What’s your name ?
#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
my_name = "Ryan"
user_name = input("What's your name?")
if user_name == my_name:
    print(f"LOOK AT{user_name} HE LOOKS FANTASTIC PEOPLE!!!")
else:
    print(f"{user_name}? I'm Rick James bitch.")

#Exercise 9 : Tall enough to ride a roller coaster
#Write code that will ask the user for their height in centimeters.
#If they are over 145cm print a message that states they are tall enough to ride.
#If they are not tall enough print a message that says they need to grow some more to ride.
height = float(input("Enter your height in centimeters:"))

if height > 145:
    print("Get on the ride Lebron")
else:
    print("Sorry Munchkin, go talk to the wizard")

#1 Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.
#If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
user_string = input("Enter string(must be exactly 10 characters long):")

if len(user_string) < 10:
    print("string not long enough.")
elif len(user_string) > 10:
    print("string too long. That's what she said.")
else:
    print("Perfect! That's what she said")


# 2 Then, print the first and last characters of the given text   
user_input = input("enter a text")

print(user_input[0])
print(user_input[-1])


#3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
user_input = input("Enter a text")

constructed_string = ""

for char in user_input:
    constructed_string += char
    print(constructed_string)


#4 Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
import random

user_import = input("Enter a string to jumble:")

char_list = list(user_input)

random.shuffle(char_list)

jumbled_string = ''.join(char_list)

print("jumbled string:", jumbled_string)