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
        return "Error: Division by zero!"

if __name__ == "__main__":
    print("Simple Calculator")
    print("Choose operation: add, subtract, multiply, divide")

    choice = input("Enter operation: ").strip().lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "add":
        print("Result:", add(num1, num2))
    elif choice == "subtract":
        print("Result:", subtract(num1, num2))
    elif choice == "multiply":
        print("Result:", multiply(num1, num2))
    elif choice == "divide":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")
