# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from art import logo
from random import choice
from os import name, system

print(logo)

def clear():
    """Clear the console"""
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def dealcard():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def calculate_score(cards):
    """Returns the score of the hand"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """Compare the scores and declare the results"""
    if user_score == computer_score:
        return "It's a draw!"

    elif computer_score == 0:
        return "You Lose!"

    elif user_score == 0:
        return "You Win!"

    elif user_score > 21:
        return "You Lose!"

    elif computer_score > 21:
        return "You Win!"

    elif computer_score > user_score:
        return "You Lose!"

    elif computer_score < user_score:
        return "You Win!"

def main():
    user_cards = []
    computer_cards = []
    
    for _ in range(2):
        user_cards.append(dealcard())
        computer_cards.append(dealcard())

    end = False
    while not end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            end = True
            print("You Lose!")
        
        else:
            another_card = input("Do you want another card? (yes/no): ").lower()
            
            if another_card == "yes":
                user_cards.append(dealcard())
            
            elif another_card == "no":
                end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealcard())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's Final Hand: {computer_cards}, Final Score: {computer_score}")
    compare(user_score, computer_score)

restart = input("Do you want to play a game of Blackjack? (y/n): ")
while restart == "y":
    clear()
    main()