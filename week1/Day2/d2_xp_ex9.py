#Exercise 9 : Tall enough to ride a roller coaster
#Write code that will ask the user for their height in centimeters.
#If they are over 145cm print a message that states they are tall enough to ride.
#If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input("Enter your height in centimeters:"))

if height > 145:
    print("Your are tall enough, Lebron!")
else:
    print("Hey munchkin, leave the line and go ask the wizard to grow some more.")

