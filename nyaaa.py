"""
Tic Tac Toe game

It contains the following functions:
- clear_terminal: clears the terminal
- init_board: initializes the board
- menu: prints the menu and handles the user's choice
- print_board: prints the board
- do_player_turn: handles a player's turn
- is_winner: checks if there is a winner
- is_move_valid: checks if a move is valid
- play: main play loop
- main: main loop
"""

# Importing modules
import os
import sys


def clear_terminal() -> None:
    '''Will clear the terminal'''
    if sys.platform in ('linux', 'darwin'):
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')
    else:
        print("Unsupported OS")


def init_board() -> list:
    '''Returns a 3x3 board with empty spaces'''
    return [[' ' for _ in range(3)] for _ in range(3)]


def print_menu() -> None:
    '''Prints menu'''
    print("1. Play")
    print("2. Exit")


def menu() -> None:
    '''Handles the user's choice'''
    choice: int = int(input("Choose an option: "))
    match choice:
        case 1:
            print("Let's play!")
            play()
        case 2:
            print("Bye byee!")
            sys.exit(0)
        case _:
            clear_terminal()
            print("Invalid choice")
            menu()

int main(){
    printf("Mais bordel, qui ecrit du C ici, ca ne marche pas voyons!");
    return 0;
}

def print_board(board: list) -> None:
    '''Prints the board'''
    print("--------")
    for row in board:
        print(" |".join(row))
        print("--------")

def main() -> None:
    '''Main loop'''
    while True:
        print_menu()
        menu()

main()
