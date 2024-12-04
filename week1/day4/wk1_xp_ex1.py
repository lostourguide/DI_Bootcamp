#Exercise 1 : Favorite Numbers
#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {3, 7, 14, 21}

my_fav_numbers.add(28)
my_fav_numbers.add(35)

my_fav_numbers.remove(max(my_fav_numbers))

friend_fav_numbers = {5, 10, 15, 20}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(f"My favorite numbers: {my_fav_numbers}")
print(f"My friend's favorite numbers: {friend_fav_numbers}")
print(f"Our favorite numbers: {our_fav_numbers}")