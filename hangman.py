
import random

Stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
lives = 6
print("Solution for the game is "+ chosen_word)
k=0
length=len(chosen_word)
word = []
for i in range (0,length):
    underscore = '_'
    word.append(underscore)

end_of_game = False
while (end_of_game == False):
    guess = input("Make a guess of a letter in the word: ").lower()
    if guess in word:
        print("You already guessed this try other letter")
    for i in range (0,length):
        if chosen_word[i] == guess:
            word[i] = guess
            print("Right")
    print(Stages[7-lives])
    if guess not in chosen_word:
        print("You guessed a letter which is not in the word. You loose a life")
        lives -=1
        if lives ==0:
            end_of_game = True
            print('you lose')
    print(word)
    if '_'  not in word:
        end_of_game = True
        print("you win")

#print ASCII stages of hangman
    








