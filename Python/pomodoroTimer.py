# Pomodoro Timer Using Tkinter
# Requirements:
# 1. Select the study length
# 2. Select the break length
# 3. Select the overall length
# 4. Implement some kind of indication that the timer is switching between states (sound/visual)

import tkinter as tk
from tkinter import simpledialog


def start_timer():
    # Logic will go here
    print("Timer started with study length:", study_length.get(), "minutes and break length:", break_length_sent.get(),
          "minutes")


root = tk.TK()
root.title("Pomodoro Timer")


# User input for study length
study_length_label = tk.Label(root, text="Enter study length (mins):")
study_length_label.pack()

study_length = tk.Entry(root)
study_length.pack()

# Break length
break_length_label = tk.Label(root, text="Enter break length (mins)")
break_length_label.pack()

break_length = tk.Entry(root)
break_length.pack()

# Start
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()


root.mainloop()