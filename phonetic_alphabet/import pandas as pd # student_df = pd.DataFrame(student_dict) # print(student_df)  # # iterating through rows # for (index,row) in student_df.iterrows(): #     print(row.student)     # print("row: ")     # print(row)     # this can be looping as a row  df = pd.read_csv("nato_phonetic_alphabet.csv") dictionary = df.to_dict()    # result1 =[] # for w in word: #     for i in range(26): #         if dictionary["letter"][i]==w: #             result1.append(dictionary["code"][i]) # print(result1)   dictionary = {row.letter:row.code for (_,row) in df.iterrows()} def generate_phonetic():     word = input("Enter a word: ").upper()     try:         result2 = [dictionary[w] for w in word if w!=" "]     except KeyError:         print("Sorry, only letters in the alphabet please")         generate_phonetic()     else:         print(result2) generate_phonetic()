
import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
dictionary = df.to_dict()

dictionary = {row.letter:row.code for (_,row) in df.iterrows()}
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result2 = [dictionary[w] for w in word if w!=" "]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(result2)
generate_phonetic()
