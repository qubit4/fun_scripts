import random

print("The winner is the first player to reach 5 wins.")

# score variables
user_wins = 0
computer_wins = 0
draws = 0

options = ["FOOT", "COCKROACH", "ATOMIC BOMB"]

# main game loop
while True:

    # first to reach 5 wins wins the whole match
    if user_wins == 5:
        break
    if computer_wins == 5:
        break

    user_input = input("Choose FOOT or COCKROACH or ATOMIC BOMB: ").upper()
    options = ["FOOT", "COCKROACH", "ATOMIC BOMB"]

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_input = options[random_number]

    print("You played {}. Computer played {}.".format(user_input, computer_input))

    # rules
    if user_input == "FOOT" and computer_input == "COCKROACH":
        print("Great play. You win.")
        user_wins += 1
        continue

    if user_input == "COCKROACH" and computer_input == "ATOMIC BOMB":
        print("Great play. You win.")
        user_wins += 1
        continue

    if user_input == "ATOMIC BOMB" and computer_input == "FOOT":
        print("Great play. You win.")
        user_wins += 1
        continue

    if user_input == computer_input:
        print("That's a draw.")
        draws += 1
        continue
    else:
        print("Computer wins this time.")
        computer_wins += 1
        continue

# end of match and final statistics
print("You won {} times.".format(user_wins))
print("Computer won {} times.".format(computer_wins))
print("Number of draws: {}.".format(draws))
