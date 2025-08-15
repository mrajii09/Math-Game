import tkinter as tk
from selectmd import select_mode

# This code defines a simple GUI application using Tkinter in Python.
# Main window class gets set up with a welcome label.

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Starting Screen")
        self.geometry("1280x720")
        
        self.config(bg="#000000")  # Set background color to black
        
        # Initialize the main frame
        self.main_frame=tk.Frame(self) # Create a frame for the main content
        self.main_frame.pack(fill=tk.BOTH, expand=True) # Pack the frame to fill the window

        # Add a label to the main frame
        self.label=tk.Label(self.main_frame, # Create a label with welcome text
                              text="Welcome to the Game!",
                              font=("Segoe UI", 50, "bold"),
                              bg="Orange",
                              fg="Red",
                              padx=20,
                              pady=20,
                              relief=tk.GROOVE
                              )
        self.label.pack(pady=20, padx=20) # Pack the label with padding
        
        # Configure a button for start and close
        self.Start_Button=tk.Button(self.main_frame,
                                 text="Start Game",
                                    font=("Segoe UI", 20, "bold"),
                                    bg="Green",
                                    fg="White",
                                    command=self.start_game
                                    )        
        self.Start_Button.place(x=250, y=300, width=200, height=50)  # Place the button at a specific position
        
        #Create and place an End Game button
        self.End_Button=tk.Button(self.main_frame,
                                 text="End Game",
                                    font=("Segoe UI", 20, "bold"),
                                    bg="Red",
                                    fg="White",
                                    command=self.end_game
                                    )
        self.End_Button.place(x=800, y=300, width=200, height=50)        

        self.choice=None  # Store selected mode here
        
    def start_game(self):
        """Start the game by selecting a mode."""
        
        #Destroy all content in the main window
        self.label.destroy()
        self.Start_Button.destroy()
        self.End_Button.destroy()
        
        # Create a select button to choose the game mode
        select_mode(self)




    def end_game(self):
        """End the game and close the main window."""
        
        self.destroy() # Destroy the main window to end the game
        
