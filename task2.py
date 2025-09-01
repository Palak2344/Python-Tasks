# Function to create a personalized greeting
def personalized_greeting():
    # Taking input from the user
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Concatenating first name and last name
    full_name = first_name + " " + last_name

    # Printing personalized greeting message
    print(f"Hello, {full_name}! Welcome!")

# Calling the function
personalized_greeting()
