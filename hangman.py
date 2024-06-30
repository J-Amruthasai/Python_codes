# Day-7 Start
# Hang Man project


import random
import os
Hangman = '''
                                                                              
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba, 
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a 
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88  
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88
                                    aa,    ,88                                
                                     "Y8bbdP"                                 '''

HANGMANPICS = ['''
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

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def play_game():
    print(Hangman)
    life = len(HANGMANPICS)
    word_choosen = random.choice(words)
    length = len(word_choosen)
    #print(word_choosen)
    list = []
    for i in range(length):
        list.append("_")
    print(" ".join(list))
    print("\n")
    while life>=0:
        
        if "_" in list and life!=0:
            guess = input("Guess a letter: ").lower()
        elif life == 0 :
            print("You lost the game")
        else:
            life = -1
            print("Congratulations! You won the game")
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please guess a single letter.")
            continue
        if guess in word_choosen:
            for i in range(len(word_choosen)):
                if word_choosen[i] == guess:
                    list[i] = guess
            if (life>0):
                print("Good guess!")
                print(" ".join(list))
        else:
            life -= 1
            if (life >= 0):
                print(HANGMANPICS[len(HANGMANPICS)-life-1])
                print("You loose a life")

def clear_screen():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
        clear_screen()

if __name__ == "__main__":
    main()



