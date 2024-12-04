#Exercise 10 : Sandwich Orders

sandwich_orders = [
    "Tuna",
    "Pastrami",
    "Chicken",
    "Pastrami",
    "Veggie",
    "Pastrami",
]

print(" '86' on Pastrami!")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Preparing{current_sandwich}...")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"-{sandwich}")