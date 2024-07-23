class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y


def main():
    calculator = Calculator()

    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose an operation (or 'q' to quit): ")

        if choice == 'q':
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = calculator.add(num1, num2)
            elif choice == '2':
                result = calculator.subtract(num1, num2)
            elif choice == '3':
                result = calculator.multiply(num1, num2)
            elif choice == '4':
                result = calculator.divide(num1, num2)

            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
