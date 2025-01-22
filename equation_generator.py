import random
import tkinter as tk
from tkinter import messagebox

# GLOBAL VARIABLES
correct_answer = 0
current_question = 0
score = 0
total_questions = 7

# Initialise GUI window, title and dimensions
root = tk.Tk()
root.title("Equation Generator")
root.geometry("400x200")

# FUNCTIONS

def generate_equation():
    """
    Generates equation in the form of b = a*x where a and x are randomly generated
    Equation is then assigned the relevant variable, x is assigned to correct answer variable
    Includes sub-functions to enable/disable submit and next equation buttons, and clear entry box
    Clears feedback label from previous equation when new one is generated
    """
    # Inherit global variable
    global correct_answer
    
    a = random.randint(1, 10)
    x = random.randint(1, 10)
    correct_answer = x
    
    # Construct equation
    b = a * x
    equation = f"{a}x = {b}"
    
    # Output equation to main text in window
    main_label.config(text=f"{current_question + 1}. {equation}")
    
    enable_submit()
    disable_next_equation()
    reset_entry_box()
    feedback_label.config(text="")

def start_quiz():
    """
    Starts equation generator quiz by removing start button and notes label
    Displays quiz interface with an entry box, a frame for the buttons, and packs empty feedback label
    Generates first equation to be displayed when quiz starts
    """
    # Remove initial screen widgets
    start_button.pack_forget()
    notes_label.pack_forget()
    
    # Display quiz interface widgets 
    entry_box.pack(pady=(0, 10))
    buttons_frame.pack(pady=(0, 10))
    feedback_label.pack()
    
    # Generate first equation
    generate_equation()

def submit_answer():
    """
    Validates user answer and displays relevant feedback message
    Disables entry box and submit button, enables next equation button
    Displays final score button once final answer is submitted
    
    Error Handling:
        - Ensures entry box is populated
        - Ensures submitted answer is an integer using a try-except block
    """
    # Inherit global variables
    global score, total_questions, current_question
    
    # Check to ensure entry box is populated
    if entry_box.get():
        try:
            # Convert entry box answer to integer
            user_answer = int(entry_box.get())
            
            # Increment score if correct and display relevant message
            if user_answer == correct_answer:
                feedback_label.config(text="Correct!", fg="light green")
                score += 1
            else:
                feedback_label.config(text=f"Incorrect. The correct answer was {correct_answer}", fg="red")
            
            # Increment question number
            current_question += 1
            
            disable_entry_box()
            disable_submit()
            enable_next_equation()
            
            # Checking for the end of the quiz
            if current_question == total_questions:
                disable_next_equation()
                score_button.grid(row=0, column=2)
                
        # Error popup if value entered is NOT an integer 
        except ValueError:
            feedback_label.config(text="")
            reset_entry_box()
            messagebox.showerror("ERROR!", "Please input a numerical value")
            
    # Displays message if submitted with no value in entry box
    else:
        feedback_label.config(text="No answer entered!", fg="black")

def show_score():
    """
    Displays final score in the main text in GUI window
    Removes quiz interface widgets
    """
    # Display final score in main GUI text
    main_label.config(text=f"Final sore: {score}/{total_questions}", pady=50)
    
    # Removes quiz interface widgets
    entry_box.pack_forget()
    buttons_frame.pack_forget()
    feedback_label.pack_forget()

def enable_submit():
    """Enables submit button"""
    submit_button.config(state="active")
    
def disable_submit():
    """Disables submit button"""
    submit_button.config(state="disabled")
    
def enable_next_equation():
    """Enables next equation button"""
    next_equation.config(state="active")
    
def disable_next_equation():
    """Disables next equation button"""
    next_equation.config(state="disabled")
    
def reset_entry_box():
    """Empties entry box and resets state to normal"""
    entry_box.delete(0, tk.END)
    entry_box.config(state="normal")
    
def disable_entry_box():
    """Empties entry box and resets state to normal"""
    entry_box.delete(0, tk.END)
    entry_box.config(state="disabled")

# WIDGETS

# Main text label
main_label = tk.Label(master= root, text= "Equation Generator", font=("Arial", 24))
main_label.pack(pady=(20, 10))

# Button to start quiz
start_button = tk.Button(master= root, text= "Start", font= ("Arial", 24), command= start_quiz)
start_button.pack()

# Main screen notes
notes_label = tk.Label(master= root, text= f"Total equations = {total_questions}. Solve for x. All answers are of type integer.", font=("Arial", 10))
notes_label.pack(pady=10)

# Entry box for user answers
entry_box = tk.Entry(master=root, width=10)

# Frame to house buttons
buttons_frame = tk.Frame(master=root)

# Initialise submit button and insert into frame grid
submit_button = tk.Button(master=buttons_frame, text="Submit", command=submit_answer)
submit_button.grid(padx=(0, 10), row=0, column=0)

# Initialise next equation button and insert into frame grid
next_equation = tk.Button(master=buttons_frame, text="Next Equation", command=generate_equation)
next_equation.grid(padx=(0, 10), row=0, column=1)

# Initialise show score button, button is displayed above when final equation is answered
score_button = tk.Button(master=buttons_frame, text="Show final score", command=show_score, background="light blue", width=20)

# Answer feedback text, displayed when answer is submitted
feedback_label = tk.Label(master=root, text="", font=("Arial", 18))

# Run equation generator
root.mainloop()
