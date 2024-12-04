#Challenge 1
#Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until the list length reaches length.

#number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

number = int(input("Enter number:"))
length = int(input("Enter the desirtred length of the list:"))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

    print(f"The list of multiples: {multiples}")