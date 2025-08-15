import tkinter as tk
from game_logic import *
from game_logic import start_game_logic


def select_mode(self):
        """Create a selection interface for the game mode."""
        
        # Placeholder for mode selection logic
        
        # Label to show what screen the user is on
        self.label=tk.Label(self.main_frame,
                                        text="Select Game Mode",
                                        font=("Segoe UI", 30, "bold"),
                                        bg="Orange",
                                        fg="Red")
        self.label.pack(pady=20)

        # Button for Addition mode, passes the mode to the game function
        self.Addition=tk.Button(self.main_frame,
                                                          text="Addition", 
                                                          font=("Segoe UI", 20, "bold"),
                                                          bg="Green",
                                                          fg="White",
                                                          command=lambda: game(self, "Addition"))
        self.Addition.pack(pady=10)

        # Button for Subtraction mode, passes the mode to the game function
        self.Subtraction=tk.Button(self.main_frame,
                                                          text="Subtraction", 
                                                          font=("Segoe UI", 20, "bold"),
                                                          bg="Blue",
                                                          fg="White",
                                                          command=lambda: game(self, "Subtraction"))
        self.Subtraction.pack(pady=10)

        # Button for Multiplication mode, passes the mode to the game function
        self.Multiplication=tk.Button(self.main_frame,
                                                                   text="Multiplication",
                                                                   font=("Segoe UI", 20, "bold"),
                                                                   bg="Purple",
                                                                   fg="White",
                                                                   command=lambda: game(self, "Multiplication"))
        self.Multiplication.pack(pady=10)

        # Button for Division mode, passes the mode to the game function
        self.Division=tk.Button(self.main_frame,
                                                          text="Division",
                                                          font=("Segoe UI", 20, "bold"),
                                                          bg="Orange",
                                                          fg="White",
                                                          command=lambda: game(self, "Division"))
        self.Division.pack(pady=10)
        
        # Create a button to end the game
        end_button = tk.Button(self.main_frame,
                               text="End Game",
                               font=("Segoe UI", 20, "bold"),
                               bg="Red",
                               fg="White",
                               command=self.destroy)
        end_button.pack(pady=10)

def game(self, mode):
        """Start the game with the selected mode."""
        
        self.choice=mode  # Set the choice to the selected mode on the MainWindow instance
        print("Starting {} Game...".format(mode))
        self.destroy()

        start_game_logic(mode)