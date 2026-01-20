import random
import os

HIGHSCORE_FILE = "highscore.txt"

def get_high_score():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            try:
                return int(file.read())
            except:
                return None
    return None

def save_high_score(score):
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(score))

def select_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1–10, 5 chances)")
    print("2. Medium (1–20, 3 chances)")
    print("3. Hard (1–50, 2 chances)")

    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == '1':
            return 10, 5
        elif choice == '2':
            return 20, 3
        elif choice == '3':
            return 50, 2
        else:
            print("❌ Invalid choice. Try again.")

def play_game():
    print("\n🎯 Number Guessing Game 🎯")

    high_score = get_high_score()
    if high_score:
        print(f"🏆 Current High Score: {high_score} attempt(s)")
    else:
        print("🏆 No high score yet. Be the first!")

    max_number, attempts = select_difficulty()
    secret_number = random.randint(1, max_number)

    print(f"\nGuess the number between 1 and {max_number}")
    print(f"You have {attempts} attempts\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: "))
        except ValueError:
            print("⚠️ Enter a valid number")
            continue

        if guess < 1 or guess > max_number:
            print(f"⚠️ Number must be between 1 and {max_number}")
            continue

        if guess < secret_number:
            print("⬇️ Too low")
        elif guess > secret_number:
            print("⬆️ Too high")
        else:
            print(f"\n🎉 Correct! You guessed in {attempt} attempt(s).")

            if high_score is None or attempt < high_score:
                save_high_score(attempt)
                print("🔥 New High Score Saved!")
            else:
                print("Good try! High score remains.")

            return

    print(f"\n😢 Game Over! The number was {secret_number}")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing 👋")
            break

main()