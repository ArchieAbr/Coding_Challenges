# Pomodoro Timer Using Tkinter
# Requirements:
# 1. Select the study length
# 2. Select the break length
# 3. Select the overall length
# 4. Implement some kind of indication that the timer is switching between states (sound/visual)

import tkinter as tk
from tkinter import simpledialog, messagebox
import time
import pygame
import os
import sys

# Initialize pygame mixer for playing sound
# Determine if running in a bundle or a normal Python environment
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Construct the path to the MP3 file
alarm_file_path = os.path.join(base_path, 'clock-alarm-8761.mp3')

pygame.mixer.init()
alarm_sound = pygame.mixer.Sound(alarm_file_path)


def countdown(count):
    global timer_id  # To keep track of the after() call for cancellation
    if count > 0:
        label.config(text=f"{current_session} Time remaining: " + time.strftime("%H:%M:%S", time.gmtime(count)))
        timer_id = root.after(1000, countdown, count - 1)
    else:
        play_sound()
        switch_state()


def switch_state():
    global is_study_time, num_sessions, current_session
    if is_study_time:
        if num_sessions > 0:
            num_sessions -= 1
            current_session = "Break"
            label.config(text="Time for a break!")
            countdown(int(break_length.get()) * 60)  # Break period
        else:
            messagebox.showinfo("Session Info", "All sessions complete!")
            label.config(text="All done!")
    else:
        current_session = "Study"
        label.config(text="Back to work!")
        countdown(int(study_length.get()) * 60)  # Study period
    is_study_time = not is_study_time  # Toggle the state


def play_sound():
    pygame.mixer.Sound.play(alarm_sound)


def start_timer():
    global is_study_time, num_sessions, timer_id, current_session
    num_sessions = simpledialog.askinteger("Input", "How many study sessions?", minvalue=1)
    if num_sessions:
        is_study_time = True
        current_session = "Study"
        timer_id = None  # Reset the timer ID
        countdown(int(study_length.get()) * 60)


def cancel_timer():
    global timer_id
    if timer_id:
        root.after_cancel(timer_id)
        label.config(text="Timer cancelled. Set new times and start again.")
        timer_id = None


root = tk.Tk()
root.title("Pomodoro Timer")

study_length_label = tk.Label(root, text="Enter study length (minutes):")
study_length_label.pack()
study_length = tk.Entry(root)
study_length.pack()

break_length_label = tk.Label(root, text="Enter break length (minutes):")
break_length_label.pack()
break_length = tk.Entry(root)
break_length.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

cancel_button = tk.Button(root, text="Cancel Timer", command=cancel_timer)
cancel_button.pack()

label = tk.Label(root, text="Please enter the durations and start the timer.")
label.pack()

root.mainloop()
