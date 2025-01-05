# here are the functions that we will use to manage the whole Fort Boyard simulator
def introduction():
    print("Welcome to the Fort Boyard simulator dear players! ")
    print("The game is very simple. You will have to complete ")
    print("various challenges to win three keys in order to get access ")
    print("to the treasure room , where all your dreams come true …")
    print("You now have thirty minutes to try and win this game.")
    print("Good luck to you all, and may the winner takes it all !")

def compose_equipe():
    team = []
    while True:
        try:
            nb_players = int(input("How many players do you want in your team (maximum 3) ? "))
            if 1 <= nb_players <= 3:
                break
            else:
                print("The number of players must be between 1 and 3")
        except ValueError:
            print("Enter an integer")

    for i in range(nb_players):
        player = {}
        player['name'] = input("Name of player {} : ".format(i + 1))
        player['profession'] = input("Profession of player {} : ".format(i + 1))
        player['leader'] = input("Is he our leader (yes/no) ? ").lower() == 'yes'
        player['keys_wons'] = 0
        team.append(player)

    # if there is no leader assigned, then the first member is designed as leader
    if not any(player['leader'] for player in team):
        team[0]['leader'] = True

    return team

def challenges_menu():
    while True:
        print("""
        1 - Maths challenges 
        2 - Logical challenges 
        3 - Chance challenges
        4 - Père Fouras riddles
        """)
        try:
            choice_challenge = int(input("Chose a challenge : "))
            if 1 <= choice_challenge <= 4:
                return choice_challenge
            else:
                print("Chose a number between 1 and 4.")
        except ValueError:
            print("Please enter an integer.")

def choose_player(team):
    """""
    arguments --> team: list of dictionnaries representing the players

    returns--> dictionnary of the selected player
    """
    print("List of players :")
    for i, player in enumerate(team, start=1):
        role = "Leader" if player['leader'] else "Member"
        print(f"{i}. {player['name']} ({player['profession']}) - {role}")

    while True:
        try:
            choice = int(input("Enter player number : "))
            if 1 <= choice <= len(team):
                return team[choice - 1]
            else:
                print("Number of player invalid.")
        except ValueError:
            print("Please enter an integer.")

def record_history(player, challenge, result, time):
    """

    arguments -->:
        player: dictionnary of the player
        challenge: game challenge
        result: result of the challenge (per see --> "you won" or "you lost").
        time: time taken to end the game (in seconds).
    """

    with open("output/history.txt", "a") as f:
        f.write(f"{player['name']} - {challenge} - {result} - {time} seconds\n")

