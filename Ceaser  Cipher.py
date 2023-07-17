#Ceaser Cipher


def caeser(direction,text,shift):
    alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    end_char = ""# as char is for character
    shift=shift%26
    if direction == "decode":
        #for the shift for big number we can use %
        
        shift*=-1
 
    for char in text:
        if char in alphabet:
            position= alphabet.index(char)
            new_position = position+shift
            end_char+=alphabet[new_position]
        else:
            end_char +=char
    print(f"The encoded text is {end_char}")
        
    
            
'''
def encrypt(text,shift):
    alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if position+shift<27:
            new_position = position + shift
        else:
            new_position = position+shift-26
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
   
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text,shift):
    alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        if position-shift<0:
            new_position = position-shift+26
        else :
            new_position = position-shift
        new_letter = alphabet[new_position]
        text+=new_letter

    print(f"The decoded text is {text}")
'''


Run = True
while Run :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
    text = input("Type your message:\n").lower()
    shift = int (input("Type the shift number:\n"))
    shift = int(shift%26)
    caeser(direction,text,shift)
    ask_user = input("If you want to continue the code:\n Type 'yes' if you want or 'no' if you don't want to.  ")
    if (ask_user).lower() == "no":
        Run = False
        print("Good Bye! ")
