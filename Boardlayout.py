"""
   Yuwei Wu
   CS5001, Fall 2022
   Final Project: The Game Puzzle Slider
   
   This is the graphics for the puzzle slider game. It sets windows, 
   draws the splash screen, board, buttons, lose, win, and quit screens.
"""
import time
import turtle


class Boardlayout:
    """
    class: 
        Boardlayout. It creates the layout of the window. 
    methods: 
        splash_screen, setup, play_area, leaderboard_area, control_area,
        player_moves, control_buttons, run_graphics, win, lose, quit_button
    """  

    def __init__(self):
        """
        constructor: 
            create new instances of wn and pen
        return: 
            nothing 
        """
        self.wn = turtle.Screen()
        self.pen = turtle.Turtle()
        self.pen.speed("fastest")
        self.pen.hideturtle()
        self.pen.pensize(5)


    def splash_screen(self):
        """
        method:
            create splash screen
        return: 
            nothing
        """
        self.wn = turtle.Screen()
        self.wn.bgpic("Resources/splash_screen.gif")
        self.wn.update()
        time.sleep(2)
        self.wn.bgpic("")


    def setup(self):
        """
        method:
            create title of the window and set its dimension and color 
        return: 
            nothing
        """
        self.wn.setup(width=800, height=800)
        self.wn.title("CS5001 Sliding Puzzle Game")
        self.wn.bgcolor("white")


    def play_area(self):
        """
        method:
            create the box area of the puzzle section 
        return: 
            nothing
        """
        self.pen.color("black")
        self.pen.up()
        self.pen.goto(-350, 350)  # start from top left corner
        self.pen.down()
        self.pen.goto(100, 350)  
        self.pen.goto(100, -200) 
        self.pen.goto(-350, -200)  
        self.pen.goto(-350, 350)  
        self.pen.up()


    def leaderboard_area(self):
        """
        method:
            create leaderboard area and writes leaders at top 
        return: 
            nothing
        """
        self.pen.color("blue")
        self.pen.up()
        self.pen.goto(140, 350)  # top left corner
        self.pen.down()
        self.pen.goto(350, 350)  
        self.pen.goto(350, -200)  
        self.pen.goto(140, -200)  
        self.pen.goto(140, 350) 
        self.pen.up()
        self.pen.goto(150, 310)
        self.pen.write("Leaders:", font=("helvetica", 18, "normal"))


    def control_area(self):
        """
        method:
            create outline of the contol section area
        return: 
            nothing
        """
        self.pen.pensize(5)
        self.pen.color("black")
        self.pen.up()
        self.pen.goto(-350, -230)  # top left corner
        self.pen.down()
        self.pen.goto(350, -230) 
        self.pen.goto(350, -330)  
        self.pen.goto(-350, -330)  
        self.pen.goto(-350, -230)  
        self.pen.up()


    def player_moves(self):
        """
        method:
            write out player moves in control area
        return: 
            nothing
        """
        self.pen.up()
        self.pen.goto(-320, -280)
        self.pen.write(f"Player Moves:", font=("helvetica", 20, "bold"))
        self.pen.up()


    def control_buttons(self):
        """
        method:
            stamp control buttons for reset, load, and quit
        return: 
            nothing
        """
        load_button_gif = "Resources/loadbutton.gif"
        reset_button_gif = "Resources/resetbutton.gif"
        quit_button_gif = "Resources/quitbutton.gif"
        self.wn.addshape(load_button_gif)
        self.wn.addshape(reset_button_gif)
        self.wn.addshape(quit_button_gif)
        # reset button
        self.pen.goto(80, -280)
        self.pen.shape(reset_button_gif)
        self.pen.stamp()
        # load button
        self.pen.up()
        self.pen.goto(180, -280)
        self.pen.shape(load_button_gif)
        self.pen.stamp()
        # quit button
        self.pen.goto(280, -280)
        self.pen.shape(quit_button_gif)
        self.pen.stamp()


    def run_graphics(self):
        """
        method: 
            condense board graphics and make the game board
        return: 
            nothing
        """
        self.play_area()
        self.leaderboard_area()
        self.control_area()
        self.player_moves()
        self.control_buttons()


    def win(self):
        """
        method: 
            present the image when player wins
        return: 
            nothing
        """
        self.wn.addshape("Resources/winner.gif")
        self.pen.shape("Resources/winner.gif")
        self.pen.showturtle()
        time.sleep(3)
        self.pen.hideturtle()


    def lose(self):
        """
        method: 
            present the image when player loses and 
            then show credits.gif
        return: 
            nothing
        """
        self.wn.addshape("Resources/Lose.gif")
        self.pen.shape("Resources/Lose.gif")
        self.pen.showturtle()
        time.sleep(3)
        self.pen.hideturtle()
        
        # credits.gif
        self.wn.addshape("Resources/credits.gif")
        self.pen.shape("Resources/credits.gif")
        self.pen.showturtle()
        time.sleep(3)
        self.pen.hideturtle()
        turtle.bye()


    def quit_button(self):
        """
        method: 
            present the image and log out when player presses quit button 
        return: 
            nothing
        """
        self.wn.addshape("Resources/quitmsg.gif")
        self.pen.shape("Resources/quitmsg.gif")
        self.pen.showturtle()
        time.sleep(3)
        self.pen.hideturtle()
        turtle.bye()