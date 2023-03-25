# Dice-rolling-simulator.py
import random

def roll_dice():
    print("Rolling the dice...")
    dice_value = random.randint(1, 6)
    print("The dice rolled a", dice_value)
    return dice_value

play_again = True

while play_again:
    input("Press Enter to roll the dice...")
    roll_dice()
    user_choice = input("Do you want to roll the dice again? (y/n): ")
    if user_choice.lower() == "n":
        play_again = False

print("Thanks for playing!")
