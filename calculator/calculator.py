def getNumbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return (num1, num2)

def calculator():
    while True:
        user_input = input ("\n\nEnter an operation you'd like to perform\n"+
            "add, subtract, multiply, divide, or quit:\n")

        if user_input == "quit":
            print ("Quitting")
            break
        
        elif user_input == "add":
            print ("Adding")
            (a, b) = getNumbers()
            result = a + b
            
        elif user_input == "subtract":
            print ("Subtracting")
            (a, b) = getNumbers()
            result = a - b
            
        elif user_input == "multiply":
            print ("Multiplying")
            (a, b) = getNumbers()
            result = a * b
            
        elif user_input == "divide":
            print ("Dividing")
            (a, b) = getNumbers()
            result = a / b
            
        else:
            print ("Unrecognized user input.")
            
        print ("The answer is ", result)

print ("This is a simple calculator")
calculator()
