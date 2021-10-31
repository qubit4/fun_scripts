### basic python code ___ quizzgame

import time

print("Ladies and Gentleman! Welcome to the QuizzGame!")
time.sleep(2)
willing_to_play = input("Do you want to play? Yes/No \n")

if willing_to_play.lower() != "yes":
    print("Nevermind. Let's play next time. Have a wonderful day!")
    time.sleep(2)
    quit()

score = 0
print("Amazing! Tell me, what is your name?")

name = input()

print("Hi, {}. Welcome to the Round 1. You start with {} $.".format(name, score))
time.sleep(2)
answer = input("Question 1. Who invented computer mouse? \n")

if answer.lower() == "douglas engelbart":
    score += 1000
    print("Bravo. You have {} $".format(score))
    time.sleep(2)

else: 
    print("Incorrect answer. Try again. You can even use Google!")
    answer = input("Question 1. Who invented computer mouse? \n")
    if answer.lower() == "douglas engelbart":
        score += 1000
        print("Bravo. You have {} $".format(score))
        time.sleep(2)
    else:
        print("Incorrect. Let's try another question.")
        time.sleep(2)
    
answer = input("Question 2. What does DNS stand for? \n")

if answer.lower() == "domain name system":
    score += 1000
    print("Bravo. You have {} $".format(score))
    time.sleep(2)
else: 
    print("Incorrect answer. Try again. You can even use Google!")
    time.sleep(2)
    answer = input("Question 2. What does DNS stand for? \n")
    if answer.lower() == "domain name system":
        score += 1000
        print("Bravo. You have {} $".format(score))
        time.sleep(2)
    else:
        print("Incorrect. Let's try another question.")
        time.sleep(2)

answer = input("Question 3. Who is current CEO of Google? \n")

if answer.lower() == "sundar pichai":
    score += 1000
    print("Bravo. You have {} $".format(score))
    time.sleep(2)
    
else: 
    print("Incorrect answer. Try again. You can even use Google!")
    time.sleep(2)
    answer = input("Question 3. Who is current CEO of Google? \n")
    if answer.lower() == "sundar pichai":
        score += 1000
        print("Bravo. You have {} $".format(score))
        time.sleep(2)
    else:
        print("Incorrect :(")
        time.sleep(2)

print("You have reached the end of Quizzgame. Thanks for playing! \nYou leave with {} $.".format(score))

