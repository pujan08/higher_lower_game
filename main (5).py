import random
import game_data
import art
from replit import clear

def get_data():
    return random.choice(game_data.data)

def format_data(choice):
    name = choice['name']
    description = choice['description']
    country = choice['country']
    return f"{name}, a {description}, from {country}"

def get_follower(choice):
    return choice['follower_count']

game = True
number = 0

while game:
    clear()
    print(art.logo)

    choice_A = get_data()
    choice_B = get_data()
    choice_A_follower = get_follower(choice_A)
    choice_B_follower = get_follower(choice_B)

    print(f"Choice A: {format_data(choice_A)}")
    print(art.vs)
    print(f"Choice B: {format_data(choice_B)}")

    user_choice = input("Who has more followers? Type 'a' or 'b': ").lower()

    if (user_choice == 'a' and choice_A_follower > choice_B_follower) or (user_choice == 'b' and choice_B_follower > choice_A_follower):
        number += 1
        print(f"You're right! Current score: {number}.")
    else:
        print(f"Sorry, that's wrong. Final score: {number}")
        game = False

    game_start = input("Play again? Type 'y': ").lower()
    if game_start != 'y':
        game = False
