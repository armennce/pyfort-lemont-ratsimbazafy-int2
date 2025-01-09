# pyfortproject
**1 - global presentation of the project**

name project *Fort Boyard Simulator*

contributors : 

- Mathis LEMONT
- Armence RATSIMBAZAFY 

* global description of the project : the aim of this project was to recreate the Game of Fort Boyard (TV show) where a team of players must complete multiple challenges of various kind, to win three keys that will give them acces to the *treasure room*. 

Here, we had only **4 kind of challenges** to implement: 

- maths challenges
- logical challenge
- chance challenge
- final challenge

programming language: Python 

We decided to divide the project into 7 files, where all the basic functions were put to generate the whole game, so that each function is stored in t-type kind challenge. 

For the function like mathematical challenge, we directly implemented the functions BUT for the functions in logical challenges or chance challenges we built them with **sub-functions** the we would call later in a general function. for exemple tic-tac-toe. 



**2 - Technical documentation of algorithm** 

**main.py** --> menu () 
To use the the menu of the game, we need to import the "main" functions that manages the rest of the subfunctions 
<img width="699" alt="import main " src="https://github.com/user-attachments/assets/34793880-85ed-4536-94c6-44d554a54a4e" />

<img width="535" alt="menu debut" src="https://github.com/user-attachments/assets/d35ff68b-103d-43cd-9a9f-6dddded3cc15" />


**utility_functions.py** --> introduction(), compose_equipe(), challenges_menu(), chose_player(), (*bonus) record_history()
<img width="593" alt="def intro" src="https://github.com/user-attachments/assets/7e477c70-f373-4e4a-ae3e-033246c915f6" />
<img width="772" alt="def compose equipe" src="https://github.com/user-attachments/assets/50aa2216-7af2-4a4a-9e7f-904cb5581d7d" />
<img width="597" alt="def choose player" src="https://github.com/user-attachments/assets/bdd0f6d8-9cde-4edf-8392-c2ed5e8d23ef" />
<img width="548" alt="def challenge menu " src="https://github.com/user-attachments/assets/979740a9-5b2a-4ebd-99d6-e419c39aa35e" />
<img width="664" alt="def record history" src="https://github.com/user-attachments/assets/ad5440ea-3334-462b-95fe-38356723d88d" />

**math_challenge.py** --> factorial(n), math_challenge_function(), is_prime(), nearest_prime(), math_challenge_prime(), solve_linear_equation(), linear_equation_test()

**logical_challenge.py** --> display_sticks(), player_move(), master_move(), nim_challenge(), tic_tac_toe(), initialize_grid(), display_grid(), check_victory, full_grid(), player_turn(), master_turn(), tictactoe_game()
**chance_challenge.py** --> 
**pere_fouras_riddles.py** --> load_riddles(file_path), pere_fouras_riddle()
**final_challenge.py** --> treasure_room

* websites and sources that we used during this project: 

* input and error managment:

- la plupart des erruers que j'ai pu faire venait souvent d'oublis en écrivant print("__") au lieu de print(f"__) ce qui ne rendait pas du tout le même résultat. 

- pour faire des tests de fonction , j'ai parfois utilisé des "balises" pour tester chaque étape de l'execution et ainsi retrouver plus vites de potentiels erreurs ou bugs/ ou pour l'ouverture de fichier pour vérifier qu'il s'ouvrait bien.


- pour faire en sorte que l'execution du code soit fluide ou qu'elle ne s'interrompt pas à "n'importe quel moment", j'ai utilisé les mots-clés **try** et **Except** qui fonctionnent un peu comme une boucle while pour s'arrêter "à la condition que".

<img width="869" alt="debut treasure_room" src="https://github.com/user-attachments/assets/d0f26b45-49a5-479f-bb54-5d7f4038aeab" />






* logbook :

1 - répartition des tâches + découverte du projet

<img width="499" alt="planner 1" src="https://github.com/user-attachments/assets/48f1c7fe-69f7-4e12-963a-41c632ea4da5" />

<img width="542" alt="planner 2" src="https://github.com/user-attachments/assets/cd8fd6b8-fa3f-47d7-b315-2eb7063351f0" />


