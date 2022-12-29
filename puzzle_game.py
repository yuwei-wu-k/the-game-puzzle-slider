"""
   Yuwei Wu
   CS5001, Fall 2022
   Final Project: The Game Puzzle Slider
   
   Puzzle game driver. Log any errors to an error file called 5001_puzzle.err
   and the game will be closed. 
"""

import turtle
from Boardlayout import Boardlayout
from Leaderboard import Leaderboard
from Puzzleclicks import Puzzleclicks


def player_name():
    """
    function:
        prompt the player to enter thier name 
    return: 
        player name
    """   
    name = turtle.Screen().textinput("CS 5001 Puzzle Slide", "Your Name:")
    return name


def player_moves():
    """
    function:
        Prompt the player to enter the number of moves they want.
        Prompt a warning message if the number is out of range and ask 
        player to enter again. 
    return: 
        the number of moves player enters
    """  
    moves = 0
    moves = int(turtle.Screen().numinput("5001 Puzzle Slide - Moves",
                                         "Enter the number of moves"
                                         "(chances) you want (5 - 200)?",
                                         None, minval=5, maxval=200))
    return moves


def main():
    try:
        board_layout = Boardlayout()
        board_layout.setup()
        board_layout.splash_screen()

        puzzle_click = Puzzleclicks(player_name(), player_moves())
        leaderboard = Leaderboard()

        board_layout.run_graphics()
        leaderboard.read_leaderboard()
        leaderboard.sort_leaderboard()
        leaderboard.draw_leaderboard()

        puzzle_click.player_moves_number()
        puzzle_click.puzzle_thumbnail()
        puzzle_click.puzzle_pieces(puzzle_click.shuffle_numbers)
        puzzle_click.click_coordinates()

        turtle.done()

    except Exception as error:
        with open("5001_puzzle.err", mode="a") as outfile:
            outfile.write(f"An error happened - {error}\n")

if __name__ == '__main__':
    main()