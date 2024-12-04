#Exercise 7 : Temperature Advice

import random

def get_random_temp(season):
    """
    Generates a random temperature based on the season.
    """
    if season == 'winter':
        return round(random.uniform(-10, 16), 1)
    elif season =='spring':
        return round(random.uniform(0,23), 1)  
    elif season == 'summer':
        return round(random.uniform(16, 40), 1)
    elif season == 'autumn':
        return round(random.uniform(0, 23), 1)
    else:
        raise ValueError("Invalid month. Please provide a number between 1 and 12.")  

def determine_season(month):
    """
    Determines the season beases on the month.
    """
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    elif month in [9, 10, 11]:
        return 'autumn'
    else:
        raise ValueError("Invalid month. Please provide a number between 1 and 12.")

def main():
    """
    Main function to display tempature and advice.
    """
    try:
        month = int(input("enter the number of the month(1-12):"))
        season = determine_season(month)
        temperature = get_random_temp(season)
        print(f"The temperature right now is {temperature} degrees celsius.")

        if temperature < 0:
            print("Brrr, thats freezing!")
        elif 0 <= temperature <=16:
            print("Chilly!")
        elif 16 < temperature <= 23:
            print("Mild weather.")
        elif 24 <= temperature <= 32:
            print("Warm and pleasant.")
        else:
            print("Really Hot!")   
    except ValueError as e:
        print(f"Error; {e}")

main()         

