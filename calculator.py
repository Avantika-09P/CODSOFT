def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"

def main():
    print("Simple Calculator")
    
    # Take user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Display operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Take user input for the operation
    choice = input("Enter your choice (1/2/3/4): ")
    
    # Perform the appropriate calculation based on the user's choice
    if choice == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Invalid operation choice. Please select from 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
