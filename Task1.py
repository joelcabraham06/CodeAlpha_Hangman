import random
import hangman_art
import hangman_words

print("Hello...Welcome to Hangman")
print(f"{hangman_art.logo}")
chosen_word = random.choice(hangman_words.word_list)

lives=6
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
correct=[]

while True:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct.append(letter)
        elif letter in correct:
            display+=letter
        else:
            display += "_"
    
    print(display)
    if guess not in chosen_word:
        lives-=1
    print(hangman_art.stages[lives])
    if lives==0:
        print("**************** Game Over... You Lose****************")
        break
    elif "_" not in display:
        print("**************** Game Over... You Win****************")
        break
