#Exercise 7: Favorite fruits

favorite_fruits = input("Enter your favorite fruits seperated by space:").split()

chosen_fruit = input("Enter the name of a fruit:")

if chosen_fruit in favorite_fruits:
    print("you chose one of your favorite fruits! Enjoy!")
else:
    print("You chise a new fruit. I hope you enjoy.")