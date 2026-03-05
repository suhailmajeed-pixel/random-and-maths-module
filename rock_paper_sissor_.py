import random 

while True:
    user_action = input("Chose one rock , paper , sissor :")
    possible_action = ["rock" , "paper" , "sissor"]

    computer_choise = random.choice(possible_action)
    print (f"\n you chose {user_action}, i chose {computer_choise}. \n")


    if user_action == computer_choise:
        print ("since both selected{user_action} . SO IT IS A TIE ")
    
    elif user_action == "paper":
        if computer_choise == "rock":
            print ("since paper covers rock . SO YOU WIN")
        else:
            print("since sissor cuts paper. SO U LOSE ")

    elif user_action == "sissor":
       if computer_choise == "papeer":
            print("since sissor cuts paper. U WIN ")
        
        else:
           print("")