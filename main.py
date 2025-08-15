# Author: Miraj Acharya
# Date: August 2025
# Description: This script is an attempt to create a simple game using Python.
# Simple calculator game

#Import necessary modules from other files and libraries
import random
from main_window import *
from game_logic import start_game_logic
from selectmd import select_mode, game
from game_window import *


def main():
    
    # Creates the main window and mainloops until closed
    mainWin=MainWindow()
    mainWin.mainloop()
    
    # Sets a mode variable based on the user's choice in the main window
    mode=mainWin.choice
    
    # Print the selected mode for debugging purposes
    print(mode)
    
    # If a mode is selected, create and run the game window
    if mode:
        gameWin=GameWindow(mode)
        gameWin.mainloop()

# call the main function to start the application
if __name__ == "__main__":
    main()