#Exercise 9: Cinemax

def calculate_ticket_cost(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15
    
def family_ticket_cost():
    total_cost = 0
    print("Enter the ages of the family members (type 'done' to finish):")
    while True:
        age_input = input("Age: ")
        if age_input.lower() == 'done':
            break
        try:
            age = int(age_input)
            total_cost += calculate_ticket_cost(age)
        except ValueError:
            print("Please enter a valid number.")
    print(f"Total cost for the family tickets: ${total_cost}")

def filter_teenagers_for_movie(teenagers):
    allowed_list = []
    print("Checking ages for movie restrictions (16-21 not allowed):")
    for name in teenagers:
        try:
            age = int(input(f"Enter the age of {name}:"))
            if 16 <= age <= 21:
                print(f"{name} is not allpowed to watch the movie. ")
            else:
                allowed_list.append(name)
        except ValueError:
            print(f"Invalid age input for {name}. Skipping.")
    print("Final list of teenagers allowed to watch the movie:", allowed_list)

    print("=== Family Ticket Cost Calculation ===")
    family_ticket_cost()

    print("\n === Tenager Movie Restriction Check ===")
    teenager_names = ["Alice", "Bob", "Charlie", "Daisy",]
    filter_teenagers_for_movie(teenager_names)
