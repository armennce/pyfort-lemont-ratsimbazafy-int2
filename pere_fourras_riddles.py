import json
import random

def load_riddles(file_path):
    #print("Début de la fonction `load_riddles`.")  # on vérifie que la fonction est appelée
    try:
        with open("/Users/maxence/Documents/pyfort-project/pyfortproject/PFRiddles.json", 'r') as file:
            print("Fichier trouvé. Chargement du JSON...")
            riddles = json.load(file)

    except FileNotFoundError:
        print(f"Erreur : le fichier {file_path} est introuvable.")
    except json.JSONDecodeError as e:
        print(f"Erreur dans le fichier JSON : {e}")
    return None

def pere_fouras_riddle():
    #loading of the riddles
    file_path = "/Users/maxence/Documents/pyfort-project/pyfortproject/PFRiddles.json"
    riddles = load_riddles(file_path)

    if not riddles:
        print("Aucune énigme disponible. Assurez-vous que le fichier est correct.")
        return False

    # random selection of a riddle
    riddle, correct_answer = random.choice(list(riddles.items()))
    print("Welcome to Père Fouras riddles challenge !")
    print(f"Here is your riddle :  {riddle['question']}")

    # alternative turn of the players
    attempts = 3
    for attempt in range(1, attempts + 1):
        player_answer = input(f"Attempt {attempt}/{attempts} - Your answer : ").strip()

        if player_answer.lower() == correct_answer.lower():
            print("Congratulations ! You answered correctly to Père Fouras ' riddle ! ")
            return True

        if attempt < attempts:
            print("Wrong answer... Try again !")
        else:
            print("This was your last shot...")

    # 4 - if the player lose...
    print(f"Too bad you lost... The right answer was : {riddle['answer']}")
    return False


