"""
   Yuwei Wu
   CS5001, Fall 2022
   Final Project: The Game Puzzle Slider
   
   Create Leaderboard class to read, write, and present the players in the leaderboard.
"""

import turtle
import time

class Leaderboard:
    """
    class: 
        Leaderboard. It creates the leaderboard section. 
    methods: 
        read_leaderboard, update_leaderboard, sort_leaderboard,
        draw_leaderboard
    """  
    def __init__(self, player_info=list):
        """
        constructor:
            Create leaderboard_turtle to write player names in the leaderboard.
        attributes:
            player_info
        return: 
            nothing 
        """
        self.leaderboard_turtle = turtle.Turtle()
        self.player_info = player_info  
        self.sorted_leaderboard = []
        self.leaderboard_turtle.hideturtle()
        self.leaderboard_turtle.speed("fastest")


    def read_leaderboard(self):
        """
        method:
            Read the leaderboard.txt file so as to write leaderboard.
            If not find the file, pop up an error image and close the program. 
        return: 
            nothing
        """
        try:
            with open("leaderboard.txt", mode="r") as infile:
                self.leaderboard_data = infile.read().split("\n")
                self.leaderboard_data.pop()
        except FileNotFoundError:
            turtle.Screen().addshape("Resources/leaderboard_error.gif")
            self.leaderboard_turtle.shape("Resources/leaderboard_error.gif")
            self.leaderboard_turtle.showturtle()
            time.sleep(3)
            self.leaderboard_turtle.hideturtle()


    def update_leaderboard(self):
        """
        method:
            When player wins, take in the moves amount and player name 
            and update in the txt file. 
        return: 
            nothing
        """
        with open("leaderboard.txt", mode="a") as outfile:
            outfile.write(f"{self.player_info[0]}:{self.player_info[1]}\n")


    def sort_leaderboard(self):
        """
        method:
            Sort leaderboard data using sorted method, 
            make comparison with the previous one every time
        return: 
            nothing
        """
        for player in self.leaderboard_data:
            temporary = player.split(":")
            self.sorted_leaderboard.append([int(temporary[0]), temporary[1]])
        self.sorted_leaderboard = sorted(self.sorted_leaderboard, key=lambda
            x: x[0])


    def draw_leaderboard(self):
        """
        method:
            Write move : name in leaderboard area and update it every time 
            when game is relaunched. 
        return: 
            nothing
        """
        self.leaderboard_turtle.up()
        self.leaderboard_turtle.goto(155, 280)
        self.leaderboard_turtle.right(90)
        
        # draw each player's move and name
        for player in self.sorted_leaderboard:
            self.leaderboard_turtle.write(f"{player[0]} : {player[1]}",
                                          font=("helvetica", 18, "normal"))
            self.leaderboard_turtle.forward(20)