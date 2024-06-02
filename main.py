# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

print("Welcome to Simple Calculator")

while True:
    print("\nPlease select operation -\n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n" \
            "5. Quit\n")

    # Take input from the user
    select = input("Select operations from 1, 2, 3, 4, 5 : ")

    if select in ('1', '2', '3', '4'):
        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))

        if select == '1':
            print(number_1, "+", number_2, "=", add(number_1, number_2))

        elif select == '2':
            print(number_1, "-", number_2, "=", subtract(number_1, number_2))

        elif select == '3':
            print(number_1, "*", number_2, "=", multiply(number_1, number_2))

        elif select == '4':
            result = divide(number_1, number_2)
            if isinstance(result, str):
                print(result)
            else:
                print(number_1, "/", number_2, "=", result)

    elif select == '5':
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid input. Please try again.")
