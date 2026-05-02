import random

def show_header():
    print("\n" + "="*50)
    print("        NUMBER GUESSING GAME")
    print("="*50)

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy   (1-50, 10 chances)")
    print("2. Medium (1-100, 7 chances)")
    print("3. Hard   (1-1000, 5 chances)")

    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            break
        print("❌ Invalid choice! Try again.")

    if choice == '1':
        return 50, 10
    elif choice == '2':
        return 100, 7
    else:
        return 1000, 5

def play_game():
    show_header()

    upper_bound, chances = choose_difficulty()
    number = random.randint(1, upper_bound)

    print(f"\n🎯 Guess a number between 1 and {upper_bound}")
    print(f"💡 You have {chances} chances\n")

    for attempt in range(1, chances + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{chances}: "))
        except ValueError:
            print("❌ Enter a valid number!")
            continue

        if guess == number:
            score = (chances - attempt + 1) * 10
            print(f"\n🎉 Correct! The number is {number}")
            print(f"🏆 Your Score: {score}")
            return

        elif guess < number:
            print("📉 Too Low!")
        else:
            print("📈 Too High!")

    print(f"\n😢 Game Over! The number was {number}")

def main():
    while True:
        play_game()
        again = input("\n🔁 Play again? (yes/no): ").lower()
        if again != "yes":
            print("\n👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()