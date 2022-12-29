"""
   Yuwei Wu
   CS5001, Fall 2022
   Final Project: The Game Puzzle Slider
   
   The class writes the puzzle file reader, puzzle creator, thumbnail 
   creator, and move counter. 
"""
import turtle
import random
import time
import glob
from Leaderboard import Leaderboard
from Boardlayout import Boardlayout

class Puzzleclicks:
    """
    class: 
        Puzzleclicks
    methods: 
        puzzle_data, puzzle_thumbnail, update_puzzle, player_moves_number, 
        check_moves, create_turtle_pieces, puzzle_pieces, click_controller,
        swap_tiles, check_win, reset_button, load_button, click_coordinates
    """  

    def __init__(self, player_name, moves):
        """
        constructor: 
            Create an instance of Puzzleclicks class 
        parameters:
            player_name, moves
        return: 
            nothing 
        """
        self.error_turtle = turtle.Turtle()
        self.error_turtle.hideturtle()
        self.wn = turtle.Screen()
        self.puzzle_dict = self.puzzle_data()
        self.moves_turtle = turtle.Turtle()
        self.moves_total = moves
        self.moves_completed = 0
        self.player_name = player_name
        self.total_pieces = int(self.puzzle_dict["number"])
        self.rows_columns = int(self.total_pieces ** 0.5)
        self.piece_size = int(self.puzzle_dict["size"])
        self.thumbnail_gif = self.puzzle_dict["thumbnail"]
        self.turtle_dict = {}
        self.ordered_numbers = list(range(1, self.total_pieces + 1))
        self.shuffle_numbers = self.ordered_numbers.copy()
        random.shuffle(self.shuffle_numbers)


    def puzzle_data(self, puzzle_file="mario.puz"):
        """
        method:
            Open the puzzle file, pull the existing data, display an error 
            scrren if none exist or file isn't in the right format. 
        parameters:
            self, puzzle_file="mario.puz"
        return: 
            nothing
        """
        try:
            # open the puzzle file and pull the existing data
            with open(puzzle_file, mode="r") as infile:
                file_data = infile.read().split("\n")

                # create a dictionary of the puzzle data
                puz_dict = {}
                for line in file_data:
                    if line != "":
                        line = line.split(": ")
                        for i in range(len(line)):
                            puz_dict[line[0]] = line[1]
                    else:
                        continue

            # check to make sure file has a square of pieces
            total_pieces = int(puz_dict["number"])
            square_number = total_pieces ** 0.5
            if int(square_number + 0.5) ** 2 == total_pieces:
                return puz_dict
            else:
                self.wn.addshape("Resources/file_error.gif")
                self.error_turtle.shape("Resources/file_error.gif")
                self.error_turtle.showturtle()
                time.sleep(4)
                self.error_turtle.hideturtle()
                print("Current puzzle is invalid")

        except FileNotFoundError:
            self.wn.addshape("Resources/file_error.gif")
            self.error_turtle.shape("Resources/file_error.gif")
            self.error_turtle.showturtle()
            time.sleep(4)
            self.error_turtle.hideturtle()
            print("Invalid Puzzle Name")


    def puzzle_thumbnail(self):
        """
        method:
            Put thumbnail of the puzzle at top right of the window,
            update every time a new puzzle loaded.
        parameters:
            self
        return: 
            nothing
        """
        self.thumbnail = turtle.Turtle()
        self.thumbnail.speed("fastest")
        self.thumbnail.up()
        self.thumbnail.goto(315, 330)
        self.wn.addshape(self.thumbnail_gif)
        self.thumbnail.shape(self.thumbnail_gif)


    def update_puzzle(self, new_file):
        """
        method:
            Load new puzzle into puzzle_data, clears the puzzle, 
            updates the puzzle and thumbnail to match user's selection
        parameters:
            self, new_file
        return: 
            nothing
        """
        # load new puzzle
        self.puzzle_dict = self.puzzle_data(new_file)
        self.thumbnail_gif = self.puzzle_dict["thumbnail"] 

        # clear and update puzzle
        for i in range(1, self.total_pieces + 1):
            self.turtle_dict[i].hideturtle()
        self.total_pieces = int(self.puzzle_dict["number"])
        self.rows_columns = int(self.total_pieces ** 0.5)
        self.piece_size = int(self.puzzle_dict["size"])
        self.ordered_numbers = list(range(1, self.total_pieces + 1))
        self.shuffle_numbers = self.ordered_numbers.copy()
        random.shuffle(self.shuffle_numbers)
        self.turtle_dict = {}
        self.create_turtle_pieces()
        self.puzzle_pieces(self.shuffle_numbers)

        # update thumbnail
        self.thumbnail.hideturtle()
        self.puzzle_thumbnail()


    def player_moves_number(self):
        """
        method:
            write the moves the player has and update the total moves
        parameters:
            self
        return: 
            nothing
        """
        self.moves_turtle.clear()
        self.moves_turtle.hideturtle()
        self.moves_turtle.speed("fastest")
        self.moves_turtle.up()
        self.moves_turtle.goto(-170, -280)
        self.moves_turtle.write(f"{self.moves_completed} / {self.moves_total}",
                                font=("helvetica", 20, "bold"))


    def check_moves(self):
        """
        method:
            check if user uses up all the remaining moves
        parameters:
            self
        return: 
            nothing
        """
        if self.moves_completed == self.moves_total:
            Boardlayout().lose()


    def create_turtle_pieces(self):
        """
        method:
            create turtle with pieces and leave the last one blank
        parameters:
            self
        return: 
            nothing
        """
        for i in range(1, self.total_pieces + 1):
            self.turtle_dict[i] = turtle.Turtle()
            self.turtle_dict[i].hideturtle()
            self.turtle_dict[i].speed("fastest")
            self.wn.addshape(self.puzzle_dict[str(i)])
            self.turtle_dict[i].shape(self.puzzle_dict[str(i)])
            self.turtle_dict[i].up()


    def puzzle_pieces(self, list_of_numbers):
        """
        method:
            write the board and set the length of the columns and rows
        parameters:
            self
            list_of_numbers: sequence of the puzzle pieces
        return: 
            nothing
        """
        self.create_turtle_pieces()
        piece = 0
        y_cord = 250
        for row in range(self.rows_columns):
            x_cord = -270
            for col in range(self.rows_columns):
                self.turtle_dict[list_of_numbers[piece]].goto(x_cord, y_cord)
                self.turtle_dict[list_of_numbers[piece]].showturtle()
                piece += 1
                x_cord += self.piece_size + 3
            y_cord -= self.piece_size + 3
        

    def click_controller(self, x, y):
        """
        method:
            Write a controller for player clicks. If player clicks on a puzzle
            within a certain distance, the piece will be swapped with the blank. 
            Update moves, check if the puzzle has been completed.
        parameters:
            self
            x: The x coordinate of the click
            y: The y coordinate of the click
        return: 
            nothing
        """
        #  Load Button
        if (43 <= x <= 117) and (-305 <= y <= -235):
            self.reset_button()
        #  Reset Button
        elif (x - 180) ** 2 + (y - -270) ** 2 <= 39 ** 2:
            self.load_button()
        #  Quit Button
        elif (242 <= x <= 320) and (-295 <= y <= -250):
            Boardlayout().quit_button()

        else:
            for i in range(1, len(self.turtle_dict) + 1):
                if abs(x - self.turtle_dict[i].xcor()) ** 2 + \
                        abs(y - self.turtle_dict[i].ycor()) ** 2 \
                        <= (self.piece_size / 2) ** 2:
                    if self.turtle_dict[i].distance(self.turtle_dict[
                                                        self.total_pieces]) \
                            == self.piece_size + 3:

                        original_tile = self.turtle_dict[i].pos()
                        blank_tile = self.turtle_dict[self.total_pieces].pos()
                        self.swap_tiles(i, original_tile, blank_tile)
                        self.moves_completed += 1
                        self.player_moves_number()
                        self.check_moves()
                        self.check_win()


    def swap_tiles(self, original_turtle, original_tile, blank_tile):
        """
        method:
            Swap positions of the clicked tile and the blank one. 
            The list associated with the tiles order changed to show the correct order. 
        parameters:
            original_turtle: number of the turtle swapped with blank tile
            original_tile: the positions of the tile swapped with blank tile
            blank_tile: position of the blank tile
        returns:
            nothing
        """
        # Swaps turtle positions
        self.turtle_dict[original_turtle].setpos(blank_tile)
        self.turtle_dict[self.total_pieces].setpos(original_tile)

        # Changes list positions
        blank = self.shuffle_numbers.index(self.total_pieces)
        other_tile = self.shuffle_numbers.index(original_turtle)
        self.shuffle_numbers[blank], self.shuffle_numbers[other_tile] = \
            self.shuffle_numbers[other_tile], self.shuffle_numbers[blank]


    def check_win(self):
        """
        method:
            Check if the shuffled list matches the ordered list. If match, 
            player wins, update leaderboard and show win image.
        parameters:
            self
        return: 
            nothing
        """
        if self.shuffle_numbers == self.ordered_numbers.copy():
            Leaderboard([self.moves_completed,
                         self.player_name]).update_leaderboard()
            Boardlayout().win()


    def reset_button(self):
        """
        method:
            reset puzzle pieces in order 
        parameters:
            self
        return: 
            nothing
        """
        self.create_turtle_pieces()
        self.puzzle_pieces(self.ordered_numbers)
        self.shuffle_numbers = self.ordered_numbers.copy()


    def load_button(self):
        """
        method:
            show window for player to enter the puzzle they want
        parameters:
            self
        return: 
            nothing
        """
        existing_puz = glob.glob("*.puz")
        existing_puz = "\n".join(existing_puz)
        load_file = turtle.textinput(f"Load Puzzle",
                                     "Enter the name of the puzzle you wish to load. "
                                     f"Choices are:\n {existing_puz}")
        self.update_puzzle(load_file)
        self.moves_completed = 0
        self.player_moves_number()


    def click_coordinates(self):
        """
        method:
            feed x, y coordinated to click_controller 
            and will be called in main driver
        parameters:
            self
        return: 
            x, y coordinated to click controller when button is clicked
        """
        return turtle.onscreenclick(self.click_controller, 1)