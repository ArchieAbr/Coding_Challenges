def find_discount():
    price = float(input("Please entre the original price of the item:\n"))
    discount = float(input("Please enter the discount percentage:\n"))
    # Calculate discount
    div_val = float(discount / 100)
    discounted_price = float(price - (price * div_val))
    return discounted_price


# Main
def main():
    discount = float(find_discount())
    discount = round(discount, 2)
    print(f"The discounted price is: £{discount}\n")
    return 0


if __name__ == "__main__":
    main()
