from sys import exit


def find_discount():
    price = float(input("Please entre the original price of the item:\n"))
    discount = float(input("Please enter the discount percentage:\n"))
    # Calculate discount
    div_val = float(discount / 100)
    discounted_price = float(price - (price * div_val))
    return discounted_price


# Main
def main():
    main_loop = True
    while main_loop:
        discount = float(find_discount())
        discount = round(discount, 2)
        print(f"The discounted price is: £{discount}\n")
        # Loop so that the user can reuse the program
        while True:
            choice = str(input("Do you want to calculate another discount?(y/n)\n"))
            if choice == "y":
                break
            elif choice == "n":
                exit("Program will now exit")
            else:
                print("Invalid input, please make a selection from the options provided(y/n)\n")

    return 0


if __name__ == "__main__":
    main()
