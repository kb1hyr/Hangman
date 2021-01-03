# Write your code here
import random


def obscured(the_word, correct_guessed_set):
    result = ''
    for letter in the_word:
        if letter in correct_guessed_set:
            result = result + letter
        else:
            result = result + "-"
    return result

def do_menu():
    answer = ''
    while answer != 'play' and answer != 'exit':
        print('Type "play" to play the game, "exit" to quit: ', end="")
        answer = input()
    return answer

words = ['python', 'java', 'kotlin', 'javascript']
selected = words[random.randint(0, len(words) - 1)]
correct_guessed = set()
all_guessed = set()
lowercase = 'abcdefghijklmnopqrstuvwxyz'

print('H A N G M A N')
counter = 0

while do_menu() != 'exit':
    while counter < 8:
        print()
        print(f'{obscured(selected, correct_guessed)}')
        if obscured(selected, correct_guessed).find('-') == -1:
            print('You guessed the word!')
            print('You survived!')
            break

        print('Input a letter: ', end="")
        ltr = input()

        if len(ltr) != 1:
            print("You should input a single letter")
            continue
        if ltr not in lowercase:
            print("Please enter a lowercase English letter")
            continue
        if ltr in all_guessed:
            print("You've already guessed this letter")
            continue

        if ltr not in selected:
            print("That letter doesn't appear in the word")
            counter += 1
        if ltr in selected:
            correct_guessed.add(ltr)
        all_guessed.add(ltr)
    if obscured(selected, correct_guessed).find('-') != -1:
        print('You lost!')
