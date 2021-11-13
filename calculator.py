### calculator

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select numerical operation")
print("1. Add")    
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice 1/2/3/4 \n")
    if choice in ("1","2","3","4"):
        num1 = float(input("Enter first number: \n"))
        num2 = float(input("Enter second number: \n"))

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))

    next_calculation = input("Do you want to proceed with another calculation? yes/no \n").lower()

    if next_calculation == "no":
        break

    else:
        print("Invalid input.")

print("Thanks. That was fun!")
