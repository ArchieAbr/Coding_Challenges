# TODO: Create a function that takes in two arguments, a price and a
#  discount percentage and returns the final price
#  to 2 dp

def find_discount():
    price = float(input("Please entre the original price of the item:\n"))
    discount = float(input("Please enter the discount percentage:\n"))
    # Calculate discount
    div_val = discount / 100
    discounted_price = price - (price * div_val)
    return discounted_price


# Main
def main():
    discount = find_discount()
    print("The discount is:", discount, "\n")
    return 0


if __name__ == "__main__":
    main()
