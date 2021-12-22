def fizzbuzz(number):
    if (number % 5 == 0) and (number % 3 == 0):
        return "fizzbuzz"
    if number % 5 == 0:
        return "fizz"
    if number % 3 == 0:
        return "buzz"
    return number


while True:
    try:
        number = int(input("enter number: "))
        print(fizzbuzz(number))
    except ValueError:
        print("not a number")
