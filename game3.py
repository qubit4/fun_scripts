import random
import pyfiglet


## ascii banner ## you might need to pip install pyfiglet
ascii_banner = pyfiglet.figlet_format("ROCK PAPER SCISSORS")
print(ascii_banner)

print("The winner is the first player to reach 5 wins.")

### score variables
user_wins = 0
computer_wins = 0
draws = 0

### or something else? grass fire water? 
options = ["ROCK", "PAPER", "SCISSORS"]


### main game loop
while True:
    
    ## first to reach 5 wins wins the whole match
    if user_wins == 5:
        break
    if computer_wins == 5:
        break
    
    user_input = input("Choose ROCK or PAPER or SCISSORS: ").upper()
    options = ["ROCK", "PAPER", "SCISSORS"]

    if user_input not in options:
        continue

    
    random_number = random.randint(0, 2)
    computer_input = options[random_number]


    print("You played {}. Computer played {}.".format(user_input, computer_input))

    if user_input == "ROCK" and computer_input == "SCISSORS":
        print("Great play. You win.")
        user_wins += 1
        continue

    if user_input == "PAPER" and computer_input == "ROCK":
        print("Great play. You win.")
        user_wins += 1
        continue
        
    if  user_input == "SCISSORS" and computer_input == "PAPER":
        print("Great play. You win.")
        user_wins += 1
        continue 

    if  user_input == computer_input:
        print("That's a draw.")
        draws += 1
        continue
    else:
        print("Computer wins this time.")
        computer_wins += 1
        continue

### end of match and final statistics
print("You won {} times.".format(user_wins))
print("Computer won {} times.".format(computer_wins))
print("Bumber of draws: {}.".format(draws))








