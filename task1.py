# Function to perform basic mathematical operations
def basic_math_operations():
    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # Checking for division by zero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero)"

    # Displaying the results
    print(f"\nResults:")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

# Calling the function
basic_math_operations()

