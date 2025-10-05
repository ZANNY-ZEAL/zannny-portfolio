import random

print("🎲 Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100...")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("👉 Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("⚠️ Please guess a number between 1 and 100 only!")
        elif guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it right in {attempts} tries!")
            break

    except ValueError:
        print("❌ Please enter a valid number!")
