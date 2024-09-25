
#addition
def function(a, b):
    ab = (a + b)
    print("The sum of these numbers is: " + str(ab))
#subtraction
def functiontwo(a, b):
    ab = (a-b)
    print("The difference of these numbers is: " + str(ab))
#multiplication
def functionthree(a, b):
    ab = (a*b)
    print("The product of these numbers is: " + str(ab))
#division
def functionfour(a, b):
    ab = (a/b)
    print("The quotient of these numbers is: " + str(ab))
while True:
    print("Please select an operation:")
    print("1. Addition") #choices
    print("2. Subtraction") #choices
    print("3. Multiplication") #choices
    print("4. Division") #choices
    op = int(input("Enter the number representing your choice: "))
    if(op == 1):
        a = int(input("Please enter the first number: ")) #first number
        b = int(input("Please enter the second number: ")) #second number
        function(a, b)
    elif (op == 2):
        a = int(input("Please enter the first number: ")) #first number
        b = int(input("Please enter the second number: ")) #second number
        functiontwo(a, b)
    elif (op == 3):
        a = int(input("Please enter the first number: ")) #first number
        b = int(input("Please enter the second number: ")) #second number
        functionthree(a, b)
    elif (op == 4):
        a = int(input("Please enter the first number: ")) #first number
        b = int(input("Please enter the second number: ")) #second number
        functionfour(a, b)
    flag = input("Would you like to try another operation? (y/n): ")
    if(flag.lower() == "y"):
        continue
    elif(flag.lower() == "n"):
        break