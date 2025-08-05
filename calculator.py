# 🧮 Mini Calculator using OOP in Python

class Calculator:
    def __init__(self):
        print("Simple OOP-Based Calculator Initialized")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def modulus(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b


if __name__ == "__main__":
    calc = Calculator()

    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")

    choice = int(input("\nEnter choice (1-6): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", calc.add(num1, num2))
    elif choice == 2:
        print("Result:", calc.subtract(num1, num2))
    elif choice == 3:
        print("Result:", calc.multiply(num1, num2))
    elif choice == 4:
        print("Result:", calc.divide(num1, num2))
    elif choice == 5:
        print("Result:", calc.modulus(num1, num2))
    elif choice == 6:
        print("Result:", calc.power(num1, num2))
    else:
        print("Invalid choice")
