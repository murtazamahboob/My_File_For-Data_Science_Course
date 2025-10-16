print("TESTing FOr GIT AND GIT-HUB")
print("This is my First change in code after making my repos")
print("this is my change in git hub")
# write code for calculator
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
        return "Error! Division by zero."
def power(a, b):
    return a ** b
def modulus(a, b):
    return a % b
def floor_divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Error! Division by zero."
def square_root(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error! Square root of negative number."
def cube_root(a):
    return a ** (1/3)
def percentage(a, b):
    return (a / b) * 100 if b != 0 else "Error! Division by zero."
def factorial(n):
    if n < 0:
        return "Error! Factorial of negative number."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def logarithm(a, base=10):
    import math
    if a > 0 and base > 1:
        return math.log(a, base)
    else:
        return "Error! Logarithm undefined for given values."
def sine(angle):
    import math
    return math.sin(math.radians(angle))
def cosine(angle):
    import math
    return math.cos(math.radians(angle))
def tangent(angle):
    import math
    return math.tan(math.radians(angle))
def cotangent(angle):
    import math
    if angle % 180 == 0:
        return "Error! Cotangent undefined for this angle."
    return 1 / math.tan(math.radians(angle))
def secant(angle):
    import math
    if angle % 180 == 90:
        return "Error! Secant undefined for this angle."
    return 1 / math.cos(math.radians(angle))
def cosecant(angle):
    import math
    if angle % 180 == 0:
        return "Error! Cosecant undefined for this angle."
    return 1 / math.sin(math.radians(angle))


def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Divide")
    print("8. Square Root")
    print("9. Cube Root")
    print("10. Percentage")
    print("11. Factorial")
    print("12. Logarithm")
    print("13. Sine")
    print("14. Cosine")
    print("15. Tangent")
    print("16. Cotangent")
    print("17. Secant")
    print("18. Cosecant")

    choice = input("Enter choice (1-18): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7', '10']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '6':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '7':
            print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
        elif choice == '10':
            print(f"({num1}/{num2}) * 100 = {percentage(num1, num2)}%")

    elif choice in ['8', '9', '11', '12']:
        num = float(input("Enter number: "))

        if choice == '8':
            print(f"Square root of {num} = {square_root
(num)}")
        elif choice == '9':
            print(f"Cube root of {num} = {cube_root(num)}")
        elif choice == '11':
            print(f"Factorial of {int(num)} = {factorial(int(num))}")
        elif choice == '12':
            base = float(input("Enter base (default is 10): ") or 10)
            print(f"log base {base} of {num} = {logarithm(num, base)}")
    elif choice in ['13', '14', '15', '16', '17', '18']:
        angle = float(input("Enter angle in degrees: "))

        if choice == '13':
            print(f"Sine of {angle}° = {sine(angle)}")
        elif choice == '14':
            print(f"Cosine of {angle}° = {cosine(angle)}")
        elif choice == '15':
            print(f"Tangent of {angle}° = {tangent(angle)}")
        elif choice == '16':
            print(f"Cotangent of {angle}° = {cotangent(angle)}")
        elif choice == '17':
            print(f"Secant of {angle}° = {secant(angle)}")
        elif choice == '18':
            print(f"Cosecant of {angle}° = {cosecant(angle)}")
    else:
        print("Invalid input")
if __name__ == "__main__":
    main()
# end of code for calculator