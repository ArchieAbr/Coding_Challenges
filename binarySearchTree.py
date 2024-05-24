# Challenge One: Create a Binary Search Tree

# TODO: Create an array of integers to be searched

array = [1, 2, 3, 4, 5, 6, 7, 68, 92, 1034, 256, 344]

# TODO: Let the user select a number
def selection:
    user_number = input("Please enter a the number you want to find in the array:/n")
    return user_number

# TODO: Find the midpoint of the array and compare, if larger go right if smaller go left
def binary_search(user_number):
    mid_point = len(array) / 2
    print(mid_point)
    return 0