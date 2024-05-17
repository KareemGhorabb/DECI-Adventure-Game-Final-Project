import time
import random
import sys
total_score = 0


# print and pause function to make it easier
def print_pause(message, seconds=2):
    print(message)
    time.sleep(seconds)


# gamme function to store the words that will appear to user
def game():
    global total_score
    while True:
        print("1 - Go through the house")
        print("2 - Get into the cave")
        choice = input("Please enter 1 or 2: ")
        if choice == '1':
            house()
            break
        elif choice == '2':
            cave()
            break
        else:
            print("Invalid input. Please try again.")


# function to store what will happen in the cave
def cave():
    global total_score
    print("You choose to go into the cave!")
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Wand of ogoroth!")
    print_pause("You discard your rusty old magic wand and take the "
                "Wand of Ogoroth with you.")
    print_pause("now you take the magical wand ")
    while True:   # while loop to repeat the process
        choice2 = input("Choose:\n1 - If you want to cast a spell"
                        "\n2 - If you want to run away\n")
# if conditions to take an action based on user's choice
        if choice2 == '1':
            print_pause("You do your best...")
            print_pause("shit !!! You have been turned into a frog!")
            total_score -= 1
            print("Your score is:", total_score)
            if total_score > 0:
                print("Congratulations! You won!")
            else:
                print("sorry,you lose")
            choice3 = input("Do you want to play again? Enter 'y' or 'n': ")
            while True:

                if choice3 == 'y':
                    print_pause("Let's play again!")
                    print_pause("You find yourself standing in an open field, "
                                "filled with grass and yellow wildflowers.")
                    print_pause("Rumor has it that a wicked fairy is "
                                "somewhere around here and has been "
                                "terrifying the nearby village.")
                    print_pause("In front of you is a house.")
                    print_pause("To your right is a dark cave.")
                    print_pause("In your hand, you hold your trusty "
                                "(but not very effective) magic wand.")
                    print_pause("You must predict the magic wand's "
                                "color to continue the game. "
                                "It will be by luck!")
                    game()
                elif choice3 == 'n':
                    print("Thanks for playing!")
                    sys.exit()
                else:
                    print("Invalid input. Please try again.")
                    print(choice3)
            # sys function to exit from the program based on user's choice
        elif choice2 == '2':
            field()
            total_score += 1
            print("Your score is:", total_score)
            if total_score == 0:
                print("Sorry, you lose. You can try again.")
            elif total_score > 0:
                print("congrats , you won !!!!!!")
        else:
            print("Invalid input. Please try again.")
    game()


# function to store what will happen in the house
def house():
    global total_score
    print("You chose to enter the house!")
    print_pause("You approach the door of the house.")
    print_pause("You knock on the door.")
    print_pause("Eep! This is the dragon's house!")
    print_pause("The dragon finds you.")
    print_pause("You feel under-prepared for this, "
                "what with only having a tiny, rusty old magic wand.")
    while True:
        choice2 = input("Choose:\n1 - If you want to cast a spell"
                        "\n2 - If you want to run away\n")
        if choice2 == '1':
            print_pause("You do your best...")
            print_pause("shit !!! You have been turned into a frog!")
            total_score -= 1
            print("Your score is:", total_score)
            if total_score > 0:
                print("Congratulations! You won!")
            else:
                print("sorry,you lose")
            choice3 = input("Do you want to play again? Enter 'y' or 'n': ")
            if choice3 == 'y':
                print_pause("Let's play again!")
                print_pause("You find yourself standing in an open field, "
                            "filled with grass and yellow wildflowers.")
                print_pause("Rumor has it that a wicked fairy is somewhere "
                            "around here and has been terrifying "
                            "the nearby village.")
                print_pause("In front of you is a house.")
                print_pause("To your right is a dark cave.")
                print_pause("In your hand, you hold your trusty "
                            "(but not very effective) magic wand.")
                print_pause("You must predict the magic wand's color to "
                            "continue the game. "
                            "It will be by luck!")
                game()
            elif choice3 == 'n':
                print("Thanks for playing!")
                sys.exit()
            else:
                print("Invalid input. Please try again.")
                print(choice3)
        elif choice2 == '2':
            field()
            total_score += 1
            print("Your score is:", total_score)
            if total_score == 0:
                print("Sorry, you lose. You can try again.")
            elif total_score > 0:
                print("congrats , you won !!!!!!")
        else:
            print("Invalid input. Please try again.")


def field():  # function to store what will happen when turn back
    global total_score
    print("You choose to run back to the field!")
    print("You decided to be in your safe zone.")
    print("You run back into the field. Luckily, "
          "you don't seem to have been followed.")
    total_score += 1
    print("your score now is ", total_score)
    print("congrats you won")
    choice3 = input("Do you want to play again? Enter 'y' or 'n': ")
    if choice3 == 'y':
        print_pause("Let's play again!")
        print_pause("You find yourself standing in an open field, "
                    "filled with grass and yellow wildflowers.")
        print_pause("Rumor has it that a wicked fairy is somewhere "
                    "around here and has been terrifying the nearby village.")
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")
        print_pause("In your hand, you hold your trusty "
                    "(but not very effective) magic wand.")
        print_pause("You must predict the magic wand's color "
                    "to continue the game.It will be by luck!")
        game()
    elif choice3 == 'n':
        print("Thanks for playing!")
        sys.exit()
    else:
        print("Invalid input. Please try again.")
        print(choice3)


print_pause("You find yourself standing in an open field, "
            "filled with grass and yellow wildflowers.")
print_pause("Rumor has it that a wicked fairy is somewhere around here and "
            "has been terrifying the nearby village.")
print_pause("In front of you is a house.")
print_pause("To your right is a dark cave.")
print_pause("In your hand, you hold your trusty "
            "(but not very effective) magic wand.")
print_pause("You must predict the magic wand's color "
            "to continue the game. It will be by luck!")
colors_of_wind = ["red", "blue", "green"]
real_color = random.choice(colors_of_wind)
"""loop to give user ability to retry if prediction is not correct
or there is an error in his input"""
while True:
    prediction = input("Choose the color that you predict "
                       "(red, green or blue): ")
    if prediction == real_color:
        total_score += 1
        print("Correct prediction!")
        print("Total Score:", total_score)
        game()
    elif prediction not in ['red', 'blue', 'green']:
        print("Try again. Please choose a valid choice.")
    else:
        print("Prediction is incorrect. Better luck next time. Try again.")
