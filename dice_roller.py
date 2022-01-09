import random


def roll_dice():
    dice_number = int(input("How many dice do you want to roll? "))
    dice_size = int(input("How many sides are the dice? "))

    dice_sum = 0

    for i in range(0, dice_number):
        roll = random.randint(1, dice_size)
        print("You rolled {}.".format(roll))
        dice_sum += roll

    print("You rolled {} in total.".format(dice_sum))


while True:
    rolling = input("For rolling type 1, for quitting type 0: ")
    if rolling == "1":
        try:
            roll_dice()
        except ValueError:
            print("Not a valid input. Try again.")
    else:
        exit()
