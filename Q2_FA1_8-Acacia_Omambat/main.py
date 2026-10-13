# Modular Calculator

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero."
    return num1 / num2

# Get two numbers from the user
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

# lets the user choose what operation to use
print("\nChoose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter choice: ")

# Calls the defined operations and executes the whole program
if choice == "1":
    answer = add_numbers(first, second)
elif choice == "2":
    answer = subtract_numbers(first, second)
elif choice == "3":
    answer = multiply_numbers(first, second)
elif choice == "4":
    answer = divide_numbers(first, second)
else:
    answer = "Invalid choice."

# Prints the final answer
print("Result:", answer)
