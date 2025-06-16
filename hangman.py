import random

# List of predefined words
word_list = ['apple', 'robot', 'chair', 'clock', 'plant']
selected_word = random.choice(word_list)

# Game setup
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Display setup
display_word = ['_' for _ in selected_word]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while incorrect_guesses < max_incorrect and '_' in display_word:
    print("\nWord to guess: " + ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess and update display
    if guess in selected_word:
        print("Correct!")
        # Reveal all positions where the letter matches
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong! You have {max_incorrect - incorrect_guesses} guesses left.")

# Final result
if '_' not in display_word:
    print("\n🎉 Congratulations! You guessed the word: " + selected_word)
else:
    print("\n❌ Game over! The word was: " + selected_word)
