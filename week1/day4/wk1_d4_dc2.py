#Challenge 2
#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
#user's word : "ppoeemm" ➞ "poem"

user_string = input("Enter string:")

new_string = ""
for char in user_string:
    if not new_string or char != new_string[-1]:
        new_string += char

print(f"New string with cosecutive duplicates removed:{new_string}")