import random

# List of words
words = ["python", "developer", "hangman", "computer", "science", "programming"]

# Choose a random word
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word letter by letter.")

# Game loop
while attempts > 0:
    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)

    # Check if player has won
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

# If player loses
if attempts == 0:
    print("\n💀 Game Over! The word was:", secret_word)
