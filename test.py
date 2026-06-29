import random
import hangman_art
import hangman_words
print(hangman_art.logo)
wordlist = hangman_words.word_list
chosen_word = random.choice(wordlist)
word_length = len(chosen_word)

display = ["_"] * word_length
end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose. The word was {chosen_word}.")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(hangman_art.stages[lives])

