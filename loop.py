def calculator():
    firstNumber = int(input("Enter the first number  :  "))
    secondNumber = int(input("Enter the second number  :  "))

    operation = input("Enter the arithmetic operation you want to be executed (additon , sustraction , ultiplication , division ): ")

    if operation == "additon":
        print("The sum is:", firstNumber + secondNumber)
    elif operation == "-":
        print("The difference is:", firstNumber - secondNumber)
    elif operation == "*":
         print("The product is:", firstNumber * secondNumber)
    elif operation == "/":
        if secondNumber != 0:
            print("The quotient is:", firstNumber / secondNumber)
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid operation selected.")

calculator()