#Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.
#If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

user_input = input("please enter a string that is 10 characters long:")

if len(user_input) < 10:
    print("string not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Prefect string. You may proceed.")