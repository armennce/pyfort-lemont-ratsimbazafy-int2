#armence
# tic-tac-toe ou morpion : done
# nim game en premier : done
# battle_ship en dernier : done
import random


def logical_challenge():
    print("Welcome welcome player ! ")
    print("In this section, you'll be ")
    print("able to chose between three ")
    print("challenges. The nim game, ")
    print("tic-tac-toe, and finally the ")
    print("battle-ship. Which one will")
    print("you ? ")

    challenges = [nim_challenge(), tic_tac_toe(), battleship_challenge()]

    #choisir un challenge aléatoirement
    challenge = random.choice(challenges)

    #je sais pas quoi mettre ptdrrr
    res = challenge
    print(f"You will play to {res}. Good luck !")


"""nim game """
def display_sticks(n):
    " displays the resting sticks "
    print(f"There are {n} sticks left.")
    print("| " * n)
    print()

def player_move(n):
    # take away a sticks
    while True:
        try:
            move = int(input("How many sticks would like to remove (1, 2 or 3 )? "))
            if move in [1, 2, 3] and move <= n:
                return move
            else:
                print("Not valid. Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter an integer.")

def master_move(n):
    # the AI will make its moves thanks to the euclidean division by 4
    return (n-1)/4 or 1

def nim_challenge(n):
    sticks = 20  # initial number of sticks
    print("Welcome to the Nim game ! ")
    print(" Here are the rules : ")
    print(" Each player can remove ")
    print("from 1 to 3 sticks. the ")
    print("loser is the player who'll")
    print("remove the last stick. ")

    while sticks > 0:
        # player turn
        display_sticks(sticks)
        move = player_move(sticks)
        sticks -= move

        if sticks <= 0:
            print("You lost ! The last stick is for you. ")
            return False

        # game master turn
        master_move_count = master_move(sticks)
        print(f"The game master removes {master_move_count}  sticks.")
        sticks -= master_move_count

        if sticks <= 0:
            print("Congratulations ! The game master lost. ")
            return True

"""""
tic-tac-toe
"""
def tic_tac_toe():
    # initialization of the grill
    print(" ")

def initialize_grid():
    """initialization of the grid as a 2D list"""
    grid = []
    for i in range(3):  # 3 lines
        row = []  # one row corresponds to one empty line
        for j in range(3):  # 3 columns
            row.append(" ")  # we add a cell to the empty line
        grid.append(row)  # we add the completed line to the grill
    return grid

# we display the 2D grid with separations
def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

def check_victory(grid, symbol):
    """we check if a player wins. """
    # check line+ columns
    for i in range(3):
        if all(cell == symbol for cell in grid[i]):  # lines
            return True
        if all(grid[j][i] == symbol for j in range(3)):  # columns
            return True

    # checks diagonals
    if all(grid[i][i] == symbol for i in range(3)):  # diagonal
        return True
    if all(grid[i][2 - i] == symbol for i in range(3)):  # anti-diagonal
        return True

    return False

def full_grid(grid):
    """checks if the grid is full"""
    return all(cell != " " for row in grid for cell in row)

def player_turn(grid):
    while True:
        try:
            move = input("Please, enter your move (line,column) : ").strip()
            row, col = map(int, move.split(","))
            if grid[row - 1][col - 1] == " ":  # checks if the cell is empty
                grid[row - 1][col - 1] = "X"
                return
            else:
                print("Cell already taken. Please chose another one.")
        except (ValueError, IndexError):
            print("Invalid input. Please, enter coordinates in the format line,column (ex: 1,2).")

def master_turn(grid):
    """master game moves ."""
    # strategy : find the first empty cell
    for row in range(3):
        for col in range(3):
            if grid[row][col] == " ":
                grid[row][col] = "O"
                return

def tictactoe_game():
    grid = initialize_grid()  # 1 - initialize the grid
    print("Welcome to the tic-tac-toe game dear player !")
    print("You will play with the 'X' and the game master with 'O'.\n")

    while True:
        # 2 - player turn
        display_grid(grid)
        print("Your turn.")
        player_turn(grid)
        if check_victory(grid, "X"):
            display_grid(grid)
            print("Congratulations, you won ! 🎉")
            return True
        if full_grid(grid):
            display_grid(grid)
            print("HA ! It's a draw. 🤝")
            return False

        # 3 - Game master's turn
        print("It's the master game's turn...")
        master_turn(grid)
        if check_victory(grid, "O"):
            display_grid(grid)
            print("The game master won")
            return False
        if full_grid(grid):
            display_grid(grid)
            print("Too bad, it's a draw.")
            return False

""' battle-ship game '
def initialize_grid():
    grid = []
    for i in range(5):  # 3 lines
        row = []  # one row corresponds to one empty line
        for j in range(5):  # 3 columns
            row.append(" ")  # we add a cell to the empty line
        grid.append(row)  # we add the completed line to the grill
    return grid

import random

def place_ships(grid, num_ships=3):
    """we place the 3 ships"""
    size = len(grid)
    ships = 0
    while ships < num_ships:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        if grid[row][col] == " ":
            grid[row][col] = "S"  # S for ship
            ships += 1

def display_grid(grid, hide_ships=True):
    """Displays the grid. The ships are hidden if hide_ships is True."""
    for row in grid:
        display_row = [" " if cell == "S" and hide_ships else cell for cell in row]
        print(" | ".join(display_row))
        print("-" * (len(grid) * 4 - 1))

def player_turn2(grid):
    """Lets the player shot in a cell of the grid."""
    while True:
        try:
            coords = input("Enter coordinates in the format (line,column) : ").split(",")
            row, col = int(coords[0]), int(coords[1])
            if grid[row][col] in ["X", "O"]:
                print("You already shot there. Try somewhere else ....")
            else:
                return row, col
        except (ValueError, IndexError):
            print("Your coordinates are invalid. Try again.")

def check_hit(grid, row, col):
    """Check if the shot touched the ship."""
    if grid[row][col] == "S":
        grid[row][col] = "X"  # X for a ship down
        print("Touch !")
        return True
    else:
        grid[row][col] = "O"  # O for a shot in water
        print("In the water.")
        return False

def check_victory2(grid):
    # checks if every ship is destroyed
    for row in grid:
        if "S" in row:
            return False
    return True


def battleship_challenge():
    # initialization of the grid
    grid = initialize_grid()
    place_ships(grid)

    print("Welcome in this battleship game !")

    while True:
        print("\nHere is the grid :")
        display_grid(grid)

        #player turn
        row, col = player_turn2(grid)
        check_hit(grid, row, col)

        # check if player won
        if check_victory2(grid):
            print("Congratulations, you destroyed every single ship of mine ... !")
            return True

        print("\nSteady for your next shot !")












