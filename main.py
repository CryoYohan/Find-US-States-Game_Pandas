import turtle
from turtle import Turtle, Screen
import pandas as pd


class Window:
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.title('US Guessing States Game')
        image = 'blank_states_img.gif'
        self.screen.addshape(image)
        turtle.shape(image)

class States(Turtle):
    def __init__(self, state,x,y):
        super().__init__()
        self.state = state
        self.x = x
        self.y = y
        self.hideturtle()
        self.penup()
    
    def move(self):
        """Move the Turtle that writes the state name to the given coordinates"""
        self.goto(self.x, self.y)
        self.write(f'{self.state}', move=True, align='center')

class Main:
    def __init__(self):
        self.df = pd.read_csv('50_states.csv')
        self.states_list = self.df.state.to_list()
        self.correct_guesses = []

        self.prompt = Screen()
        self.states_guessed = 0
        self.window = Window()

    def start(self):
        """Start the Game!"""
        game_is_running = True
        while game_is_running:

            # Prompt user state to guess

            state = self.prompt.textinput(title=f'{self.states_guessed}/50 guessed!', prompt="What's the next state's name?")

            if not state is None: # If none, then User clicked Cancel button. If so, the game closes
                if state.title() in self.states_list and state.title() not in self.correct_guesses:
                    print('Correct!')
                    self.states_guessed += 1
                    xcor = self.df[self.df.state == state.title()].x.to_list()[0] # Get State X coordinates from DataFrame
                    ycor = self.df[self.df.state == state.title()].y.to_list()[0] # Get State Y coordinates from DataFrame
                    print(f'X coord: {xcor} Y coord: {ycor}')

                    self.correct_guesses.append(state.title()) # Add correct guesses to validate whether the input has already been guessed

                    state = States(state=state,x=xcor, y=ycor) # Initialize State-turtle object
                    state.move() # Move the State-turtle object to the given coordinates during initialization

                elif state.title() in self.correct_guesses:
                    print('You already guessed this state.')
                else:
                    print('Meh')

            else:
                game_is_running = False


if __name__ == "__main__":
    main = Main()
    main.start()



