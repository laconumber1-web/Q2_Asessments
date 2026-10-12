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


first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

print("\nChoose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter choice: ")

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

print("Result:", answer)
