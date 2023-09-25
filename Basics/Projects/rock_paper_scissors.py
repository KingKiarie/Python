import random

def get_choice():
    while True:
        player_option = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_option in ["rock", "paper", "scissors"]:
            return player_option
        else:
            print("Please enter rock, paper, or scissors.")

def online_round():
    choices = ["rock", "paper", "scissors"]
    computer_option = random.choice(choices)
    player_option = get_choice()

    print(f"Computer chose: {computer_option}")
    print(f"You chose: {player_option}")

    if player_option == computer_option:
        return "draw", 0
    elif(player_option == "rock" and computer_option == "scissors"):
       return "You win this round!", 1
    elif(player_option == "scissors" and computer_option == "paper"):
        return "You win this round!", 1
    elif(player_option == "paper" and computer_option == "rock"):
          return "You win this round!", 1
    else:
        return "Computer wins this round!", -1

def game():
    rounds = int(input("Enter the number of rounds (3 or 5): "))
    user_score = 0
    rival_score = 0

    for t in range(rounds):
        result, score = online_round()
        print(result)
        user_score += score

        if user_score >= 2 and rounds == 3:
            print("You won the game!")
            break
        elif user_score >= 3 and rounds == 5:
            print("You won the game!")
            break
        elif user_score <= -2 and rounds == 3:
            print("Computer won the game!")
            break
        elif user_score <= -3 and rounds == 5:
            print("Computer won the game!")
            break


    game()
