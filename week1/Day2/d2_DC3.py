#Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

#The user enters "HelloWorld"
#Then, you have to construct the string character by character
#H
#He
#Hel
#... etc
#HelloWorld

user_input = input("Enter a string:")

constructed_string = " "

for char in user_input:
    constructed_string += char

    print(constructed_string)

#Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). 
import random

my_string = "HelloWorld"

char_list = list(my_string)

random.shuffle(char_list)

shuffled_string = ''.join(char_list)

print("shuffled string:", shuffled_string)

