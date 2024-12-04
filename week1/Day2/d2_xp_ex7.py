#Exercise 7 : Odd or Even
#Write code that asks the user for a number and determines whether this number is odd or even.

number = int(input("Enter number:"))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")