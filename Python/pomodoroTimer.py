# Pomodoro Timer Using Tkinter
# Requirements:
# 1. Select the study length
# 2. Select the break length
# 3. Select the overall length
# 4. Implement some kind of indication that the timer is switching between states (sound/visual)

import tkinter as tk
from tkinter import simpledialog, messagebox
import time


def countdown(count):
    # Update label with the remaining time
    label.config(text="Time remaining: " + time.strftime("%H:%M:%S", time.gmtime(count)))

    if count > 0:
        root.after(1000, countdown, count - 1)
    else:
        # Timer has finished
        switch_states()


def switch_states():
    global is_study_time, num_sessions

    if is_study_time:
        if num_sessions > 0:
            num_sessions -= 1
            messagebox.showinfo("Session Info", "Time for a break!")
            countdown(int(break_length.get() * 60))  # Break
        else:
            messagebox.showinfo("Session Info", "All sessions complete!")
            label.config(text="All done!")
    else:
        messagebox.showinfo("Session Info", "Back to work!")
        countdown(int(study_length.get()) * 60)  # Study

    is_study_time = not is_study_time  # Toggle the state


def start_timer():
    global is_study_time, num_sessions

    is_study_time = True
    num_sessions = simpledialog.askinteger("Input", "How many study sessions?", minvalue=1)
    if num_sessions:
        countdown(int(study_length.get()) * 60)


root = tk.Tk()
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

label = tk.Label(root, text="")
label.pack()

root.mainloop()
