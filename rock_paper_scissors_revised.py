import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    print("Computer picked", options[random_number] + ".")

    user_pick = options.index(user_input)

    if user_pick - random_number > 0 or user_pick - random_number == -2:
        print("user win")
        user_wins += 1
    elif user_pick - random_number < 0 or user_pick - random_number == 2:
        print("computer win")
        computer_wins += 1
    else:
        print("draw")


print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Goodbye!")


