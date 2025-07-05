import time
import random

# Randomize player
player = random.choice(["Mohamed Salah", "Omar Marmoush", "Rudiger", "Cristiano Ronaldo", "Courtois", "Haaland", "Modric"])

# Identify country
def country(player):
    if player == "Mohamed Salah" or player == "Omar Marmoush":
        return "Egypt"
    elif player == "Rudiger":
        return "Gemany"
    elif player == "Cristiano Ronaldo":
        return "Portugal"
    elif player == "Courtois":
        return "Belgium"
    elif player == "Haaland":
        return "Norway"
    elif player == "Modric":
        return "Croatia"

# Identify position
def position(player):
    if player == "Mohamed Salah":
        return "RWF"
    elif player == "Omar Marmoush":
        return "SS or LWF"
    elif player == "Rudiger":
        return "CB"
    elif player == "Cristiano Ronaldo":
        return "CF OR LWF"
    elif player == "Courtois":
        return "GK"
    elif player == "Haaland":
        return "CF"
    elif player == "Modric":
        return "CMF"

# Identify club  
def club(player):
    if player == "Mohamed Salah":
        return "Played for AS Roma, Chelsea, And currently in Liverpool"
    elif player == "Omar Marmoush":
        return "Played for Stuttgart, Eintracht Frankfurt, Currently in Man City"
    elif player == "Rudiger":
        return "Played for AS Roma and Chelsea, Currently in Real Madrid"
    elif player == "Cristiano Ronaldo":
        return "Played for Sporting CF,Man United, Real Madrid, Juventus, Currently in Al Nassr"
    elif player == "Courtois":
        return "Is currently in Real Madrid"
    elif player == "Haaland":
        return "Played for Dortmund, currently in Man city"
    elif player == "Modric":
        return "Is currently in Real Madrid"

# Welcome message
print("-"*30)
print("Welcome to our game")
print("-"*30)
time.sleep(2)

# Want a quick hint
hint = input("Do you want a quick hint??[y/n] ").lower()
if hint == "yes" or hint == "y":
    print("The computer thinks of a player, then you try to guess who he is by the information about him")
elif hint == "no" or hint == "n":
    pass
else:
    print("I get you don't want a hint. So let's get started")
print("-"*30)

while True:
    # Display info
    print(f"1- He plays for {country(player)} national team")
    time.sleep(3)
    print(f"2- He is {position(player)}")
    time.sleep(3)
    print(f"3- He {club(player)}")
    print("-"*30)

    # Guesses
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    while guess != player and not out_of_guesses:
        print(f"You have {guess_limit} guesses. Good Luck!!")
        print("-"*30)
        if guess_count < 3:
            guess = input("Enter your guess: ").title()
            guess_count += 1
            guess_limit -= 1
            time.sleep(2)
            print("-"*30)
            if guess != player:
                print("Wrong guess")
                print("-"*30)
        else:
            out_of_guesses = True
            break

    if out_of_guesses:
        print(f"You Lose :( The player was {player}")
    else:
        print(f"You win")
    print("-"*30)

    # Do you want to play again??
    play_again = input("Do you want to play again??[y/n] ").lower()
    if play_again == "y" or play_again == "yes":
        player = random.choice(["Mohamed Salah", "Omar Marmoush", "Rudiger", "Cristiano Ronaldo", "Courtois", "Haaland", "Modric"])
        print("-"*30)
        pass
    elif play_again == "n" or play_again == "no":
        print("Ok Bye")
        print("-"*30)
        break
    else:
        break