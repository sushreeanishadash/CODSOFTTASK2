# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator function
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result:", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print("Invalid input. Please enter a valid choice.")
#Function to call calculator
calculator()
