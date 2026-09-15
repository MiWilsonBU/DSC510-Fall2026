"""
DSC 510 - Week 3 - 3.1 Assignment
Author: Andrew Bach
Date: 9/14/2026

Program used to calculate the cost of an order of fiber optic cable while calculating amount based on feet ordered
"""
import locale
locale.setlocale(locale.LC_ALL, 'C')


def format_currency(amount):
    return '${:,.2f}'.format(amount)


def calculate_price(amount_ordered):
    if amount_ordered > 500:
        return 0.55
    elif amount_ordered > 250:
        return 0.75
    elif amount_ordered > 100:
        return 0.85

    return 0.95


def get_company():
    company_name = ""

    while not company_name:
        company_name = input("\nWhat company are you ordering for: ").strip()

        if not company_name:
            print("Please enter a company name.")

    return company_name


def get_order_details():
    quantity = 0
    total = 0
    price = 0

    while quantity <= 0:
        try:
            quantity = int(input("\nHow many feet of fiber optic cable would you like to order: "))

            if quantity <= 0:
                print("Please enter a number greater than 0 for your order.")
                continue

            price = calculate_price(quantity)
            total = quantity * price

            print(
                f"\n{quantity} feet of fiber optic cable will cost a total of {format_currency(total)} "
                f"at {format_currency(price)} per foot."
            )

            user_input = input("Would you like to proceed? (Y/N): ").upper()

            if user_input in ("N", "NO", "NOPE"):
                quantity = 0

        except ValueError:
            print("An invalid value was entered, please enter a numeric value for your order.")

    return quantity, price, total


def main():
    continue_ordering = True
    while continue_ordering:
        print("Welcome to the Bach Fiber Optics. Lets get ready to place your order!")

        company = get_company()

        print(
            f"\nWe are looking forward to helping {company} with their Fiber Optic Cable Order."
            "\n-Current Costs-"
            "\nFiber Optic Cable | 1-100   | $0.95 per foot"
            "\nFiber Optic Cable | 101-250 | $0.85 per foot"
            "\nFiber Optic Cable | 251-500 | $0.75 per foot"
            "\nFiber Optic Cable | 501+    | $0.55 per foot"
        )

        order_quantity, line_price, order_total = get_order_details()

        # Print Receipt
        print(
            "\nYour order has been placed!"
            "\nHere is your receipt:"
            "\n-------------------------------------------"
            "\nBach Fiber Optics"
            "\n-------------------------------------------"
            f"\nSales Receipt for {company}"
            "\n-------------------------------------------"
            "\nQty     | Product                | Price"
            f"\n{order_quantity}     | Fiber optic cable      | {format_currency(line_price)}\n"
            f"\nTotal: {format_currency(order_total)}"
            "\n-------------------------------------------"
        )

        user_input = input("\nWould you like to place another order? (Y/N): ").upper()

        if user_input in ("N", "NO", "NOPE"):
            continue_ordering = False

    print("Have a great day!")

if __name__ == "__main__":
    main()