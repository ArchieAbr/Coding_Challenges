# Challenge One: Create a Binary Search Tree

def selection():
    user_number = int(input("Please enter a the number you want to find in the array:\n"))
    return user_number


def binary_search(array, lo, hi, user_number):
    # Check base case
    if hi >= lo:
        mid = (hi + lo) // 2
        if array[mid] == user_number:
            return mid
        #         If element is smaller than mid then it must be left in the array
        elif array[mid] > user_number:
            return binary_search(array, lo, mid - 1, user_number)

        #         else it must be right of the mid-point
        else:
            return binary_search(array, mid + 1, hi, user_number)

    else:
        #  Element is not present in array
        #  Value not present
        return -1


array = [1, 2, 3, 4, 5, 6, 7, 68, 92, 128, 256, 344]
x = selection()
result = binary_search(array, 0, len(array)-1, x)
if result != -1:
    print("Your number (", x, ") is present at index", str(result), "\n")
else:
    print("Value not present.\n")
