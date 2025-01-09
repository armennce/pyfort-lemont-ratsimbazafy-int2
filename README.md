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

- main.py() --> menu ()
- utility_functions.py --> introduction(), compose_equipe(), challenges_menu(), chose_player(), (*bonus) record_history()
- math_challenge.py --> factorial(n), math_challenge_function(), is_prime(), nearest_prime(), math_challenge_prime(), solve_linear_equation(), linear_equation_test()
- logical_challenge.py --> display_sticks(), player_move(), master_move(), nim_challenge(), tic_tac_toe(), initialize_grid(), display_grid(), check_victory, full_grid(), player_turn(), master_turn(), tictactoe_game()
- chance_challenge.py --> 
- pere_fouras_riddles.py --> load_riddles(file_path), pere_fouras_riddle()
- final_challenge.py --> treasure_room

* websites and sources that we used during this project: 

* input and error managment:

- la plupart des erruers que j'ai pu faire venait souvent d'oublis en écrivant print("__") au lieu de print(f"__) ce qui ne rendait pas du tout le même résultat. 

- pour faire des tests de fonction , j'ai parfois utilisé des "balises" pour tester chaque étape de l'execution et ainsi retrouver plus vites de potentiels erreurs ou bugs/ ou pour l'ouverture de fichier pour vérifier qu'il s'ouvrait bien.



- pour faire en sorte que l'execution du code soit fluide ou qu'elle ne s'interrompt pas à "n'importe quel moment", j'ai utilisé les mots-clés **try** et **Except** qui fonctionnent un peu comme une boucle while pour s'arrêter "à la condition que".

<img width="869" alt="debut treasure_room" src="https://github.com/user-attachments/assets/d0f26b45-49a5-479f-bb54-5d7f4038aeab" />


  

* logbook :

1 - répartition des tâches + découverte du projet 
2 - 
