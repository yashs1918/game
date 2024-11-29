import random

def display_menu():
    print("\nRock, Paper, Scissors Game:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    while True:
        display_menu()
        try:
            player_input = int(input("\nEnter your choice (1-4): "))
            if player_input == 4:
                print("Thanks for playing! Goodbye!")
                break
            elif player_input in [1, 2, 3]:
                choices = ["Rock", "Paper", "Scissors"]
                player_choice = choices[player_input - 1]
                computer_choice = get_computer_choice()
                print(f"\nYou chose: {player_choice}")
                print(f"Computer chose: {computer_choice}")
                result = determine_winner(player_choice, computer_choice)
                print(result)
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
