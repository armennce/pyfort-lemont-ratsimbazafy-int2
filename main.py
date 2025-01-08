#menu at the very end 
from utility_functions import compose_equipe, challenges_menu, choose_player, introduction
from math_challenge import math_challenge_factorial, math_challenge_prime, linear_equation_test, maths_challenge
from chance_challenge import challenge_function
from logical_challenge import logical_challenge
from pere_fourras_riddles import pere_fouras_riddle
#from final_challenge import treasure_room
def menu():
    """
    Implements the main game loop.

    This function handles team composition, challenge selection,
    player choice, and game progression.
    """
    # 1 - introduction
    print(introduction())
    # Team composition
    team = compose_equipe()
    print(f"Your team is composed of :")
    for player in team:
        print(f"- {player['name']}")

    # Game loop
    keys_won = 0
    while keys_won < 3:
        print("\n--- Challenge Menu  ---")
        choice_challenge = challenges_menu()

        # Sélection du joueur
        selected_player = choose_player(team)
        print(f"\n{selected_player['name']} will complete the challenge !")

        # Lancement du défi
        if choice_challenge == 1:
            result = maths_challenge()
        elif choice_challenge == 2:
            result = challenge_function()
        elif choice_challenge == 3:
            result = logical_challenge
        elif choice_challenge == 4:
            result = pere_fouras_riddle()

        # Attribution de la clé
        elif result:
            keys_won += 1
            selected_player['keys_wons'] += 1
            print(f"Congratulations ! {selected_player['nom']} won a key ! ")
            print(f"Total number of keys : {keys_won}")

    # Fin du jeu - Gestion du trésor (à implémenter)
    print("\nYou finally obtained the three keys !")
    print("Time for the final challenge: the treasure room !")
    if keys_won == 3:
        result = treasure_room()
        print("DONE")

if __name__ == "__main__":
    menu()



"""""
from pere_fourras_riddles import load_riddles  # Import de la fonction depuis math_challenge.py
file_path = "PFRiddles.json"
riddles = load_riddles(file_path)  # Appel de la fonction
print(" HELLOOOOOOOOOO :", riddles)
"""

from final_challenge import treasure_room
file_path = "TRClues.json"
resultat = treasure_room("/Users/maxence/Documents/pyfort-project/pyfortproject/TRClues.json")
print("RESULTAT -->", resultat)



