number = int(input("enter number: "))


def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("fizz")
    elif number % 3 == 0:
        print("buzz")
    else:
        print(number)


while True:
    fizzbuzz(number)
    number = int(input("enter number: "))
