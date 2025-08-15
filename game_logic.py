import random
from selectmd import *


# Main logic for the game window.
def start_game_logic(mode):
    """returns the mode of the game."""
    print(f"Game logic started with mode: {mode}")
    # Store mode in a variable or use it as needed
    # This is where you would implement the game logic based on the selected mode
    return mode


def math(self, mode):
    """Chooses digits and sets answer based on the game mode."""
    self.mode=start_game_logic(mode)
    
    # Generate random digits based on the mode
    
    #Since addition is easy, select a wider range of numbers
    if mode == "Addition":
        # Generate two random numbers for addition
        digitone=random.randint(1, 900)
        digittwo=random.randint(1, 900)
        answer=digitone + digittwo # Combine digitone and digittwo for addition answer
        
    # Subtraction is simple, so select a range where digitone is always greater than digittwo
    if mode == "Subtraction":
        # Generate two random numbers for subtraction
        digitone=random.randint(1, 900)
        digittwo=random.randint(1, digitone-1)  # Ensure digitone is always greater than digittwo
        answer=digitone - digittwo # Take away digittwo from digitone for subtraction answer
        
    # Multiplication is more complex, so select a range of numbers that is manageable
    if mode == "Multiplication":
        # Generate two random numbers for multiplication
        digitone=random.randint(1, 20)
        digittwo=random.randint(1, 20)
        answer=digitone * digittwo # Multiply digitone and digittwo for multiplication answer
        
    # Division is more complex, so select a range of numbers that is manageable
    if mode == "Division":
        digitone=random.randint(1, 100)
        digittwo=random.randint(1, 10)
        answer=digitone / digittwo # Divide digitone by digittwo for division answer
    
    # Return the generated digits and answer
    return digitone, digittwo, answer
    # This function can be expanded to include more game logic as needed