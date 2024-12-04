#Exercise 8: Who ordered a pizza ?

toppings = []

while True:
    topping = input("Enter a pizza topping(or type 'quit' to finish):")

    if topping.lower() == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"I'll add{topping}to your pizza!")

base_price = 10
topping_price = 2.5
total_price = base_price + len(toppings) * topping_price

print("\n ---Pizza Order Summary---")
print("Toppings added: ", ", ".join(toppings))
print(f"Total price: ${total_price:.2f}")
