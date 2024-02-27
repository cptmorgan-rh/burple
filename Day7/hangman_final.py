import random
import hangman_art
import hangman_words

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6

#print(f"The chosen word is {chosen_word}")

print(hangman_art.logo)

display = []
for x in range(word_length):
    display.append("_")

guessed_letter = []

print(hangman_art.stages[lives])

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    if guess not in guessed_letter:
        guessed_letter += guess
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter


        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The correct answer was: {chosen_word}")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win")

        print(hangman_art.stages[lives])

    else:
        print(f"You have already guessed: {guess}\n")
        print("Guess again.\n")