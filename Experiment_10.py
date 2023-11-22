# Write a program to create a simple calculator using switch case and function for every operation.


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"
def calculator(operation, x, y):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    operation_function = operations.get(operation.lower())
    if operation_function:
        result = operation_function(x, y)
        return result
    else:
        return "Invalid operation"
def display_menu():
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        if choice in ['1', '2', '3', '4']:
            operation = {
                '1': 'add',
                '2': 'subtract',
                '3': 'multiply',
                '4': 'divide'
            }[choice]
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator(operation, num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
