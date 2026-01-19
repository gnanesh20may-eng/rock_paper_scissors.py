import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("❌ Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors Game 🎮")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😢 Computer wins this round!")
            computer_score += 1

        print(f"\n📊 Scoreboard → You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n👋 Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
