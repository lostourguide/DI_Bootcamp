#Exercise 6 : While Loop
#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.


my_name = "Your Name"

while True:
    user_input = input("What is your name?")
    if user_input == my_name:
        print("Thats my name tool")

    else:
        print("That's not my name. Try Again")