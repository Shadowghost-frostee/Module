__author__ = "8284121, Yao"

import os 

from epr_functions import decimal_to_octal, decimal_to_basis, chaos_turtle

menu_epr_functions = """
1 - Function to convert decimal to octal
2 - Function to convert decimal to basis
3 - Chaos Turtle
4 - Quit
"""

def program():
    """Program is a function that imports functions from the
    epr_functions module based on user choice."""

    while True:
        print(menu_epr_functions)
        choice = input("Make your choice (or '4' to quit): ")

        if choice == "4":
            break  # Quit the loop and end the program

        while choice not in {"1", "2", "3"}:
            print(menu_epr_functions)
            choice = input("Invalid choice. Make your choice: ")

        if choice == "1":
            decimal_number = int(input("Enter a decimal number: "))
            result = decimal_to_octal(decimal_number)
            print(result)

        elif choice == "2":
            number_of_basis_ten = int(input("Enter a number in base 10: "))
            new_base = int(input("Enter the new base: "))
            result = decimal_to_basis(number_of_basis_ten, new_base)
            print(result)

        elif choice == "3":
            iterations = int(input("Enter the number of iterations: "))
            start_position = eval(input("Enter the start position as a tuple (x, y): "))
            chaos_turtle(iterations, start_position)

# print(dir(menu_epr_functions))

if __name__ == "__main__":
    program()

