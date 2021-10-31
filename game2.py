### basic python code _____ guess a number or die / with stamina

import random
import time

print("This is game number 2. Guess the number or die.")
time.sleep (3)
print("First, rolling 1 six-sided dice for your stamina.")
time.sleep (3)

x = random.randint(0,6)
stamina = x


print("You rolled {}. Your stamina is {}. \nIf your stamina comes down to 0, you die.".format(x, stamina))
time.sleep(3)
print("Second, rolling 2 six-sided dices to establish X.")
time.sleep(3)

x = random.randint(0,6)
y = random.randint(0,6)
upper_limit = x + y

print("You rolled {} and {}. X is {}. \nThe machine will now generate random number between 0 and X.".format(x,y,upper_limit))
time.sleep(3)

target_number = random.randint(0, upper_limit)

while True:

    if stamina == 0:
        print("You are dead.")
        exit()
    else:
        pass

    user_guess = input("Now guess the number or die: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("This is not a number. You have to pay.")
        stamina -= 1
        print("Your stamina is {}.".format(stamina))
        continue

    if user_guess == target_number:
        print("Correct. You get + 5 to your stamina. Proceed to the next room.")
        stamina += 5
        quit()
    
    else:
        print("Incorrect.")
        stamina -= 1
        if stamina == 0:
            print("You are dead.")
            exit()
        else:
            print("Your stamina is {}.".format(stamina))
            print("Do you want a hint in exchange for stamina? Yes / No")
            answer = input()

            if answer.lower() == "yes":
                if user_guess <= target_number:
                    print("Your guess is below the target number.")
                    stamina -= 1
                    print("Your stamina is {}.".format(stamina))
                else: 
                    print("Your guess is above the target number.")
                    stamina -= 1
                    print("Your stamina is {}.".format(stamina))
            else:
                continue
