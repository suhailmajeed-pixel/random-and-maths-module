import random
playing = True
number = str(random.randint(0,9))
print ("i will genarate a number from 0 to 9 and u will have to gess the number one digit at a time .")
print("the game will end when u get 1 hero .")

while playing :
    guess = input("Give me your best guess! \n")
    if number == guess :
        print("YOU WIN")
        print ("the number was", number)
        break

    else:
        print ("WRONG ANSWER . try again \n")
    