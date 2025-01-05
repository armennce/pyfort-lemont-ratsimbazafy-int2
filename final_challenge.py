import random
import json

def treasure_room():
    #loading od the json file
    with open('TRClues.json', 'r') as f:
        tv_game = json.load(f)

    # random selection of the riddle
    years = list(tv_game.keys())
    year = random.choice(years)
    shows = tv_game[year]
    show = random.choice(shows)

    # we extract the clues and the code
    clues = show['clues']
    code_word = show['code_word']

    # initialization
    attempts = 3
    answer_correct = False

    while attempts > 0:
        answer = input("Enter your answer : ")
        if answer == code_word:
            answer_correct = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts left.")
            else:
                print(f"You lost haha ... Le code The code was : {code_word}")

    # display of message if winner
    if answer_correct:
        print("Congratulations, you found the treasure !")


# call of the function
treasure_room()
