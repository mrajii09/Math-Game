# import
import tkinter as tk
from selectmd import select_mode, game

from game_logic import math


class GameWindow(tk.Tk):
    def __init__(self, mode):
        
        game=True  # Control variable for the game loop
        
        colorbg1="#000000"  # Set background color to black
        colorbg2="White"
        
        super().__init__() # Initialize the Tkinter window
        self.mode=mode # Store the selected mode
        self.title("Game Window") # Set the title of the window
        self.geometry("1280x720") # Set the size of the window
        
        # Initialize the main frame
        self.main_frame=tk.Frame(self) # Create a frame for the main content
        
        self.main_frame.pack(fill=tk.BOTH, expand=True) # Pack the frame to fill the window
        
        # Display the selected mode
        self.label=tk.Label(self.main_frame,
                              text=f"Game Mode: {self.mode}",
                              font=("Segoe UI", 30, "bold"),
                              bg="Orange",
                              fg="Red",
                              relief=tk.SUNKEN) # Create a label to show the game mode
        
        self.label.pack(pady=20)
        
        
        # mode-specific settings and colorways
        
        # Set the operator and colors based on the mode
        
        if mode == "Addition":
            self.operator="+"
            colorbg="Green"
            colorbg2="Yellow"
        elif mode == "Subtraction":
            self.operator="-"
            colorbg="#FF5733"
            colorbg2="Blue"
        elif mode == "Multiplication":
            self.operator="*"
            colorbg="Purple"
            colorbg2="Pink"
        elif mode == "Division":
            self.operator="/"
            colorbg="Orange"
            colorbg2="LightBlue"
        
        
        # Store digit 1 and digit 2, and the answer as instance variables
        self.digitone, self.digittwo, self.answer = math(self, mode)

        # Make labels for the numbers and operator, as well as a place for user to put in the answer
        
        self.first_number_label = tk.Label(self.main_frame,
                                      text=f"{self.digitone}",
                                      font=("Segoe UI", 50),
                                      bg=colorbg,
                                      width=3,
                                      relief=tk.SUNKEN) # First number label

        self.second_number_label = tk.Label(self.main_frame,
                                       text=f"{self.digittwo}",
                                       font=("Segoe UI", 50),
                                       bg=colorbg2,
                                       width=3,
                                       relief=tk.SUNKEN) # Second number label

        operator_label = tk.Label(self.main_frame,
                                  text=f" {self.operator} ",
                                  font=("Segoe UI", 50)) # +, - , * or / operator

        equal_label = tk.Label(self.main_frame,
                               text="=",
                               font=("Segoe UI", 50)) # =


        # Place labels in the appropriate order
        self.first_number_label.place(x=300, y=200)
        operator_label.place(x=475, y=200)
        self.second_number_label.place(x=600, y=200)
        equal_label.place(x=750, y=200)

        # Entry for user answer
        self.entry = tk.Entry(self.main_frame, font=("Segoe UI", 50), justify="center")
        self.entry.place(x=875, y=200, width=400, height=100)

        # Result label
        self.result_label = tk.Label(self.main_frame,
                                        text="",
                                        font=("Segoe UI", 30, "bold"),
                                        bg="white",
                                        fg="black",
                                        width=20,
                                        relief=tk.SUNKEN)
        self.result_label.place(x=310, y=400)

        # Submit button
        self.submit_button = tk.Button(self.main_frame,
                                  text="Submit",
                                  font=("Segoe UI", 20, "bold"),
                                  bg="Blue",
                                  fg="White",
                                  command=self.submit)
        self.submit_button.place(x=1000, y=350, width=200, height=50)

        # Refresh numbers button
        refresh_button = tk.Button(self.main_frame,
                                   text="Refresh Numbers",
                                   font=("Segoe UI", 20, "bold"),
                                   bg="Orange",
                                   fg="White",
                                   width=20,
                                   command=self.refresh_numbers)
        
        refresh_button.place(x=925, y=450, height=50)
        
        # Create a button to end the game
        end_button = tk.Button(self.main_frame,
                               text="End Game",
                               font=("Segoe UI", 20, "bold"),
                               bg="Red",
                               fg="White",
                               command=self.destroy)
        end_button.place(x=1000, y=550, width = 200, height=50)  # Place the end button

    def submit(self):
        """Check the user's answer and provide feedback."""
        
        #Get the user answer from the entry field
        user_answer = self.entry.get()
        
        try:
            
            # Check if the user answer matches the correct answer
            if float(user_answer) == self.answer:
                
                self.result_label.config(text="Correct!", fg="Green") # On the label display correct
                
                self.submit_button.config(state=tk.DISABLED) # Disable submit button so they can't submit again
                
            else:
                
                self.result_label.config(text=f"Incorrect! Answer: {self.answer}.", fg="Red") # On the label display incorrect and the answer
                
                self.submit_button.config(state=tk.DISABLED) # Disable submit button so they can't submit again
        except ValueError:
            self.result_label.config(text="Please enter a valid number.", fg="Red") # Handle invalid input

    def refresh_numbers(self):
        """Refresh the numbers and reset the game state."""
        
        # Makes new randomized numbers and answer, inserts them into the labels
        self.digitone, self.digittwo, self.answer = math(self, self.mode) # Generate new numbers
        
        self.first_number_label.config(text=f"{self.digitone}") # Change the first number label
        
        self.second_number_label.config(text=f"{self.digittwo}") # Change the second number label
        
        self.submit_button.config(state=tk.NORMAL) # Re-enable the button
        
        self.entry.delete(0, tk.END) # Clear the entry field
        
        self.result_label.config(text="") # Clear the result label to reset the game state


