#armence
import random

def challenge_function():
    challenges = [chance_challenge(), roll_dice_game(), shell_game()]
    challenge = random.choice(challenges)

    res = challenge
    print(f"You'll play to {res}.")

def chance_challenge():
    # welcome message to chance challenge
    print("Welcome to the chamber of chance !")
    print("Here you'll be able to try two ")
    print("chance challenges. The shell-challenge")
    print("or the the rolling dice. ")

def shell_game():

    list_shell = ['A', 'B', 'C']  # shells list
    max_attempts = 2  # maximum attempt
    attempts = 0  # count attempts

    #2 - instructions to shell game
    print("You will play the shell-game !")
    print("I will hide a key under one of ")
    print(" the three shells. You will have ")
    print("three two attempts. If you find ")
    print("the key, you can take it. But if ")
    print("you don't, I will keep it. ")
    hidden_shell = random.choice(list_shell)

    #3 - the game goes on until there is no attempts
    while attempts < max_attempts:
        hidden_shell = random.choice(list_shell)

        #4 - we display the number of resting attempts
        print(f"Tentative {attempts} + 1/{max_attempts}.")
        print("Available shells : A, B, C")

        #5 - we ask the user to choose a shell
        player_choice = input("Choose a shell between A, B or C").strip().upper()

        #6 - check if choice is valid
        if player_choice in list_shell:
            if player_choice == hidden_shell:
                print("Congratulations ! You found the key! ")
                return True
            else:
                print("Too bad... The key isn't here :/")
        else:
            print("Ahhh too bad ... Your answer is not valid :/")

        attempts +=1
    print("\nYou have no attempts anymore.")
    print(f"The key was hidden under shell :{hidden_shell}.")
    return False

def roll_dice_game():
    max_attempts = 3
    attempts = 0

    #welcome message + instructions
    print("Welcome to the rolling dice game ! ")
    print("The aime of this game is simple: the")
    print("first one to get a six with his dices")
    print("wins. If you win, you'll get a key. If")
    print("you don't, I'll keep it. ")

    #1 - we run the loop
    while attempts < max_attempts:
        print((f"Tentative {attempts + 1}/{max_attempts}.").strip().upper())
        #2 - we ask the player to throw the dice
        #print(input("press Enter"))
        #3 - we generate randomly two integers
        player_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"You obtained : {player_dice[0]} and {player_dice[1]}")

        #4 - we check if the player has a 6
        if 6 in player_dice:
            print("Congratulations, you got a 6 !")
            print("You can have the key ;)")
            return True

        #5 - game master throws the dices
        master_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"You obtained : {master_dice[0]} and {master_dice[1]} ")

        #6 - we check if the master has a 6
        if 6 in master_dice:
            print("Well, congratulations to me :) I got a 6 ;)")
            print("Thus, I will keep the key.")
            return False
        #7 - nobody's got a 6 so keep going
        print("Nobody has a 6. We can go on.")
        attempts +=1

    #8 - if nobody has a 6, then it's a draw
    print("Well, seems like nobody won.")
    print("It's a draw.")
    return False





            




















