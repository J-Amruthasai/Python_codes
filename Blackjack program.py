# Blackjack Capstone Project

Blacjack_capstone_logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/  


          _____
         |X .  | _____
         | /.\ ||X ^  | _____
         |(_._)|| / \ ||X _  | _____
         |  |  || \ / || ( ) ||X_ _ |
         |____X||  .  ||(_'_)||( v )|
                |____X||  |  || \ / |
                       |____X||  .  |
                              |____X|

                                    
                      '''




import random , os
def play_game():
    print(Blacjack_capstone_logo)
    cards = ["11","2","3","4","5","6","7","8","9","10","10","10","10"]
    dict= {"flowers": cards, "leaves": cards,"diamonds":cards,"hearts":cards}

    computer = {}
    computer_dup = {}
    player = {}
    player_dup = {}
    player_score = 0
    computer_score = 0
    i=0

    def define_card(dictionary,i):
        result_dict={}
        for key in dictionary:
            result_dict[key+str(i)]=random.choice(dictionary[key])
            i=i+1
        return result_dict, i



    def selecting_keys(dictionary,k):
        selected_keys = random.sample(dictionary.keys(),k)
        result_dict = {key:dictionary[key] for key in selected_keys}
        return result_dict

    def extra(dictionary):
        extra_card_dict = {}
        extra_card_dict_key= random.choice(list(dictionary.keys()))
        extra_card_dict_value=dictionary.pop(extra_card_dict_key)
        extra_card_dict[extra_card_dict_key]=extra_card_dict_value
        return extra_card_dict


    def create_list(dictionary):
        list = []
        for key in dictionary:
            list.append(dictionary[key])
        return list

    def sum_dict(dictionary):
        add = sum(int(value) for value in dictionary.values())
        return add

    def print_fun(dictionary, string):
        print(f"The {string} cards are:")
        print("{")
        for keys in dictionary:
            key = keys.rstrip('0123456789')
            print(f"{key}:{dictionary[keys]},",end=" ")
        print("\n}\n")

    computer_dup,j =define_card(dict,i)
    player_dup,_ = define_card(dict,j)

    computer = selecting_keys(computer_dup,3)
    player = selecting_keys(player_dup,2)

    extra_card_dict = extra(computer)

    list1=create_list(player)
    print(f"The cards you got :{list1} ")

    list2=create_list(computer)
    print(f"one card of dealer is {random.choice(list2)}")

    want = input("Do you want to take a card from the dealer (y/n): ").lower()

    if want == "y":
        player.update(extra_card_dict)

    player_score=sum_dict(player)
    computer_score=sum_dict(computer)

    if (str(11) in player.values() and player_score>21):
        player_score -= 10

    print_fun(player,"User")
    print_fun(computer,"Dealer")

    print(f"User score is : {player_score}")
    print(f"Dealer score is: {computer_score}")

    if player_score >21:
        print("You busted! Dealer wins")
    elif (player_score<computer_score):
        print("Dealer wins")
    elif (player_score>computer_score):
        print("You win")
    else:
        print("It's a draw")
        
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
