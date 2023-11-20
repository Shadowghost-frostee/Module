__author__ = "8284121, Yao"

import turtle
import random

def decimal_to_octal(decimal_number):
    """Decimal to octal is a function that takes as argument a positive integer 
    (incl. the 0) in base 10 as an argument and returns a string of this in the 
    corresponding octal representation is returned.
    """
    # Use the isinstance method to check that the number entered is an integer.
    if not isinstance(decimal_number, int) or decimal_number < 0:
        return int(input("Please enter your number: "))
    
    # Initialization of variable
    result_octal = ""
    original_number = decimal_number

    # The number of steps is set to 1 if it is not less than 8.
    step_number = 1

    # Processing 
    while decimal_number > 0:
        rest_decimal = decimal_number % 8
        result_octal = str(rest_decimal) + result_octal
        decimal_number = decimal_number // 8

        # Output 
        print(f"Processing: {original_number} (decimal) to Octal...")
        print(f"Step {step_number}: {original_number} % 8 = {original_number % 8}  Rest {result_octal}.")

        # Number of steps plus one if the number entered is greater than 8.
        step_number += 1

    while decimal_number > 0:
        decimal_number = decimal_number // 8
        print(f"step {original_number // 8 + 1}: {decimal_number} % 8 = {decimal_number % 8}  Rest {result_octal}")
        # Original_number // 8 + 1, because the steps start with 1 and not 0.
    
    return f"The octal writing of {original_number} is {result_octal}.\n"

##################### ####################### #########################
##################### ####################### #########################

def decimal_to_basis(number_of_basis_ten, new_basis):
    """Decimal to basis is a function that takes two positive integers as arguments. 
    The first number corresponds to a number in base 10, the second number is to represent 
    the new base is to represent the new base. The function should return a string of the first 
    number in the corresponding base representation.
    """
    if (not isinstance(number_of_basis_ten, int) or 
    not isinstance(new_basis, int) or 
    number_of_basis_ten < 0 or 
    new_basis < 0):
        return input("Please enter the right number: ")

    result_to_new_basis = ""
    original_number = number_of_basis_ten

    # The number of steps is set to 1 if it is not less than 8.
    step_number = 1

    # Processing 
    while number_of_basis_ten > 0:
        rest_new_basis = number_of_basis_ten % new_basis
        result_to_new_basis = str(rest_new_basis) + result_to_new_basis
        number_of_basis_ten = number_of_basis_ten // new_basis

        # Output 
        print(f"Processing: {original_number} (number of basis 10) to new base {new_basis}...")
        print(f"Step {step_number}: {original_number} % {new_basis} = {rest_new_basis}", end=" ")
        print(f"Rest {result_to_new_basis}.")

        # Number of steps plus one if the number entered is greater than 8.
        step_number += 1
    
    while number_of_basis_ten > 0:
        number_of_basis_ten = number_of_basis_ten // new_basis
        print(f"step {number_of_basis_ten // new_basis + 1}: "
      f"{number_of_basis_ten} % {new_basis} = "
      f"{number_of_basis_ten % new_basis}  Rest {result_to_new_basis}")
        # Original_number // new_basis + 1, because the steps start with 1 and not 0.
    
    return f"The representation of {original_number} to the new base {new_basis} " \
       f"is {result_to_new_basis}.\n"




#################### ####################### #########################
#################### ####################### #########################
def chaos_turtle(iterations, start_position):
    # Initialisierung der Turtle
    screen = turtle.Screen()
    screen.title("Chaos Turtle")
    screen.setup(width=800, height=600)
    
    chaos_turtle = turtle.Turtle()
    chaos_turtle.speed(2)  # Geschwindigkeit der Turtle einstellen

    # Definition der Eckpunkte des Dreiecks
    points = [(-100, -50), (0, 100), (100, -50)]

    # Startpunkt der Turtle setzen
    chaos_turtle.penup()
    chaos_turtle.goto(start_position)
    chaos_turtle.pendown()

    # Schleife für die Anzahl der Iterationen
    for _ in range(iterations):
        # Zufälligen Eckpunkt auswählen
        target_point = random.choice(points)

        # Zum zufällig ausgewählten Punkt bewegen und zeichnen
        chaos_turtle.goto((chaos_turtle.xcor() + target_point[0]) / 2, (chaos_turtle.ycor() + target_point[1]) / 2)
        chaos_turtle.dot(5)  # Punkt zeichnen

    turtle.done()  # Bildschirm schließen, wenn fertig


if __name__ == "__main__":
    
     # Testcase 1
    decimal_number = 12
    result = decimal_to_octal(decimal_number)
    print(result)

    decimal_number = 20
    result = decimal_to_octal(decimal_number)
    print(result)

    decimal_number = 2452
    result = decimal_to_octal(decimal_number)
    print(result)

    print("########### ############## ############## ########### \n")

    # Testcase 2
    result = decimal_to_basis(12, 10)
    print(result)
    result = decimal_to_basis(12, 8)
    print(result)
    result = decimal_to_basis(12, 2)
    print(result)

    print("########### ############## ############## ########### \n")

    # Beispielaufruf mit 5 Iterationen und Startpunkt (0, 0)
    chaos_turtle(5, (0, 0))


