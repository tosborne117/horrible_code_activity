
#function returns the sum of the given arguments
def addition(a, b):
    print("The sum of these numbers is: " + str(a + b))

#function returns the difference of the given arguments
def subtraction(a, b):
    print("The difference of these numbers is: " + str(a - b))

#function returns the product of the given arguments
def multiplication(a, b):
    print("The product of these numbers is: " + str(a * b))

#function returns the quotient of the given arguments
def division(a, b):
    print("The quotient of these numbers is: " + str(a / b))

while True:
    #Display operation options for user
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    #request and store user choice
    op = int(input("Enter the number representing your choice: "))

    #Request user to input numbers, and store as function arguments
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))

    #Perform function depending on user choice
    if(op == 1):
        addition(a, b)
    elif (op == 2):
        subtraction(a, b)
    elif (op == 3):
        multiplication(a, b)
    elif (op == 4):
        division(a, b)

    #Ask user whether to continue operations or terminate program
    flag = input("Would you like to try another operation? (y/n): ")
    if(flag.lower() == "n"):
        break