import math
import numpy as np
from sys import exit


# TODO: Circle
def circle_di():
    # pir^2
    radius = float(input("Enter the radius\n"))
    dimentions = np.pi * (radius * radius)
    circle_formatted_out = round(dimentions, 2)
    print("The area of your circle is:", circle_formatted_out)
    return circle_formatted_out


# TODO: Square
def square_di():
    edge = float(input("Enter the length of an edge:\n"))
    dimensions = edge * edge
    square_formatted_out = round(dimensions, 2)
    print("The area of your square is:", square_formatted_out)
    return square_formatted_out


# TODO: Triangle
def tri_di():
    b = float(input("enter the base of the triangle:\n"))
    h = float(input("Enter the height of the triangle:\n"))
    dimensions = (b * h) / 2
    tri_formatted_out = round(dimensions, 2)
    print("Area of the triangle is:", tri_formatted_out)
    return 0


# TODO: Function to calculated based on selection
def find_areas():
    calculations_arr = ["Circle", "Triangle", "Square"]
    selection = int(input("Please select the shape: 1 (Circle), 2 (Triangle), 3 (Square)\n"))
    calculations = calculations_arr[int (selection) -1]
    if calculations == "Circle":
        circle_di()
    elif calculations == "Square":
        square_di()
    elif calculations == "Triangle":
        tri_di()
    else:
        print("Error")
        exit()
    return 0


def main():
    find_areas()


if __name__ == '__main__':
    main()