__author__ = "<828'121>, <Yao>"


#input
#Eingabe
def decimal_to_binar(value):
    #we had the option of entering any number of choice
    #value = eval(input("Geben Sie eine Zahl: "))
#Procesing 
#Verarbeitung
    if value == 0:
        return "the intered value is 0."
    binary_number = ""
    original_value = value
    while value > 0:
        rest = value % 2
        binary_number = str(rest) + binary_number
        value = value // 2
    return f"the binar writing of {original_value} is {binary_number}."
    
"""we had the option to print the result 
of entering any number of choice"""
#print(dezimal_to_binar(""))

#checking of the value zero 0
#print(decimal_to_binar(0))

#Output
#Ausgabe
print(decimal_to_binar(12))
print(decimal_to_binar(20))
print(decimal_to_binar(50))

print(decimal_to_binar(2345))