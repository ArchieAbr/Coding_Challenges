# Coding_Challenges

## Contents
- [Find the Discount](#find-the-discount)
- [Internet Speed Tester](#internet-speed-tester)
- [Pomodoro Timer](#pomodoro-timer)

## Introduction
Coding challenges I have decided to take on in my spare time. So far I have just been googling various challenges to try and solve. I will be adding more challenges as I go along.
The code is split up into folders based on the language used to solve the challenge.

## Find the Discount

### Details
Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

### How to Run the App
- Via the terminal, navigate to the directory where the file is located and run the following command:
'python3 findTheDiscount.py'
  - You will be prompted to enter the original price and the discount percentage. Enter the values as integers and press 'Enter'.
  - The final price after the discount will be displayed in the terminal.
- Alternatively, you can try running the .exe file in the 'dist' folder.

## Internet Speed Tester

### Details
Create a program that tests the internet speed of the user. The program should be able to:
- Version 1:
  - Handle network errors
  - Test the user's download speed
  - Test the user's upload speed
  - Test the user's ping
  - Display the results in the terminal
- Version 2:
  - Does the same as above but uses a more user-friendly GUI

### Dependencies
- Install requirements by running the following command in the terminal: 'pip install -r speed_test_requirements.txt'

### How to Run the App
- Install requirements by running the following command in the terminal: 'pip install -r speed_test_requirements.txt'
- Via the terminal, navigate to the directory speed_test_project and run the following command:
  - Version 1: 'python3 speedTest.py' 
  - Version 2: 'python3 speedTest2.0.py'


## Pomodoro Timer

### Details
Create a Pomodoro Timer application that helps users manage their time effectively. The application should:
- Allow users to set a timer for any amount of time in minutes
- Allow user to set break time
- Display the time remaining in the timer
- Play a sound when the timer is up

### Dependencies
- Install requirements by running the following command in the terminal: 'pip install -r pomodoro_timer_requirements.txt'

### How to Run the App
- Via the terminal, navigate to the directory pomodoroTimer and run the following command: 'python3 pomodoroTimer.py'
- Or you can try running the .exe/.app file in the 'dist' folder. (Note: The .app file is only available for MacOS users, 
and this might not work because of path issues when the app tries to find the alarm sound).


