#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint

def board(count):
    print("============= Round %i ============="%count)
    print("--------------------------------")
    print("|          |          |         |")
    print("|          |          |         |")
    print("|     {}    |     {}    |    {}    |".format(position_dict[1], position_dict[2], position_dict[3]))
    print("|          |          |         |")
    print("|          |          |         |")
    print("--------------------------------")
    print("|          |          |         |")
    print("|          |          |         |")
    print("|     {}    |     {}    |    {}    |".format(position_dict[4], position_dict[5], position_dict[6]))
    print("|          |          |         |")
    print("|          |          |         |")
    print("--------------------------------")
    print("|          |          |         |")
    print("|          |          |         |")
    print("|     {}    |     {}    |    {}    |".format(position_dict[7], position_dict[8], position_dict[9]))
    print("|          |          |         |")
    print("|          |          |         |")
    print("--------------------------------")


def result(count, player_order):
        if ((position_dict[1] == position_dict[2] and  position_dict[2] == position_dict[3]) or        
            (position_dict[4] == position_dict[5] and  position_dict[5] == position_dict[6]) or
            (position_dict[7] == position_dict[8] and  position_dict[8] == position_dict[9]) or
            (position_dict[1] == position_dict[4] and  position_dict[4] == position_dict[7]) or
            (position_dict[2] == position_dict[5] and  position_dict[5] == position_dict[8]) or
            (position_dict[3] == position_dict[6] and  position_dict[6] == position_dict[9]) or
            (position_dict[1] == position_dict[5] and  position_dict[5] == position_dict[9]) or
            (position_dict[3] == position_dict[5] and  position_dict[5] == position_dict[7])):
            if (player_order == "1st" and count % 2 == 1) or (player_order == "2nd" and count % 2 == 0):
                print("Congratulation! You win !!!")
            else:
                print("HA! HA! HA! You Lose !!!")
            return True
        elif count == 9:
            print("Draw !!!")
            return True


# In[2]:


def com_motion(count, position_dict, player_dicision):
    if position_dict[5] == 5:
        return 5;
    
    elif count <= 3:
        if position_dict[1] == 1 and position_dict[9] == 9:
            return 1
        elif position_dict[3] == 3 and position_dict[7] == 7:
            return 3
        elif position_dict[7] == 7 and position_dict[3] == 3:
            return 7
        elif position_dict[9] == 9 and position_dict[1] == 1:
            return 9
        
    else:
        if position_dict[5] == position_dict[1] and position_dict[9] == 9 and position_dict[1] == "X":
            return 9
        elif position_dict[5] == position_dict[2] and position_dict[8] == 8 and position_dict[2] == "X":
            return 8
        elif position_dict[5] == position_dict[3] and position_dict[7] == 7 and position_dict[3] == "X":
            return 7
        elif position_dict[5] == position_dict[4] and position_dict[6] == 6 and position_dict[4] == "X":
            return 6
        elif position_dict[5] == position_dict[6] and position_dict[4] == 4 and position_dict[6] == "X":
            return 4
        elif position_dict[5] == position_dict[7] and position_dict[3] == 3 and position_dict[7] == "X":
            return 3
        elif position_dict[5] == position_dict[8] and position_dict[2] == 2 and position_dict[8] == "X":
            return 2
        elif position_dict[5] == position_dict[9] and position_dict[1] == 1 and position_dict[9] == "X":
            return 1
        
        elif position_dict[1] == position_dict[2] and position_dict[3] == 3 and position_dict[2] == "X":
            return 3
        elif position_dict[1] == position_dict[4] and position_dict[7] == 7 and position_dict[4] == "X":
            return 7
        elif position_dict[2] == position_dict[3] and position_dict[1] == 1 and position_dict[3] == "X":
            return 1
        elif position_dict[4] == position_dict[7] and position_dict[1] == 1 and position_dict[7] == "X":
            return 1
        elif position_dict[6] == position_dict[3] and position_dict[9] == 9 and position_dict[3] == "X":
            return 9
        elif position_dict[7] == position_dict[8] and position_dict[9] == 9 and position_dict[8] == "X":
            return 9
        elif position_dict[8] == position_dict[9] and position_dict[7] == 7 and position_dict[9] == "X":
            return 7
        elif position_dict[9] == position_dict[6] and position_dict[3] == 3 and position_dict[9] == "X":
            return 3
     
        elif position_dict[1] == position_dict[3] and position_dict[2] == 2 and position_dict[3] == "X":
            return 2
        elif position_dict[1] == position_dict[7] and position_dict[4] == 4 and position_dict[7] == "X":
            return 4
        elif position_dict[3] == position_dict[9] and position_dict[6] == 6 and position_dict[9] == "X":
            return 6
        elif position_dict[7] == position_dict[9] and position_dict[8] == 8 and position_dict[9] == "X":
            return 8

        else:

            if position_dict[5] == position_dict[1] and position_dict[9] == 9:
                return 9
            elif position_dict[5] == position_dict[2] and position_dict[8] == 8:
                return 8
            elif position_dict[5] == position_dict[3] and position_dict[7] == 7:
                return 7
            elif position_dict[5] == position_dict[4] and position_dict[6] == 6:
                return 6
            elif position_dict[5] == position_dict[6] and position_dict[4] == 4:
                return 4
            elif position_dict[5] == position_dict[7] and position_dict[3] == 3:
                return 3
            elif position_dict[5] == position_dict[8] and position_dict[2] == 2:
                return 2
            elif position_dict[5] == position_dict[9] and position_dict[1] == 1:
                return 1

            elif position_dict[1] == position_dict[2] and position_dict[3] == 3:
                return 3
            elif position_dict[1] == position_dict[4] and position_dict[7] == 7:
                return 7
            elif position_dict[2] == position_dict[3] and position_dict[1] == 1:
                return 1
            elif position_dict[4] == position_dict[7] and position_dict[1] == 1:
                return 1
            elif position_dict[6] == position_dict[3] and position_dict[9] == 9:
                return 9
            elif position_dict[7] == position_dict[8] and position_dict[9] == 9:
                return 9
            elif position_dict[8] == position_dict[9] and position_dict[7] == 7:
                return 7
            elif position_dict[9] == position_dict[6] and position_dict[3] == 3:
                return 3

            elif position_dict[1] == position_dict[3] and position_dict[2] == 2:
                return 2
            elif position_dict[1] == position_dict[7] and position_dict[4] == 4:
                return 4
            elif position_dict[3] == position_dict[9] and position_dict[6] == 6:
                return 6
            elif position_dict[7] == position_dict[9] and position_dict[8] == 8:
                return 8
            else:
                return randint(1, 9)


# In[3]:


def mode(mode_type):
    
    if mode_type == "E":
        count = 1
        while count <= 9:
            if player_order == "1st":
                while True:
                    try:
                        player_dicision = int(input("Please enter the position you want to mark(enter number 1~9): "))
                        if ((0 < player_dicision < 10) and 
                            (position_dict[player_dicision] != "O" and position_dict[player_dicision] != "X")):
                            position_dict[player_dicision] = "X"
                            break
                        else:
                            print("Your position is out of range or it has been occupied!")
                    except:
                        print("Please enter number 1~9")
                    
            
                board(count)
                if count >= 3:
                    if result(count, player_order) == True:
                        break            
                count += 1    

                while True:
                    com_dicision = randint(1, 9)
                    if position_dict[com_dicision] != "O" and position_dict[com_dicision] != "X":
                        break

                if count % 2 == 1:
                    position_dict[com_dicision] = "X"
                elif count % 2 == 0:
                    position_dict[com_dicision] = "O"

                board(count)
                if count >= 3:
                    if result(count, player_order) == True:
                        break
                count += 1

            else:
                if count == 1:
                    com_dicision = 5
                else:
                    while True:
                        com_dicision = randint(1, 9)
                        if position_dict[com_dicision] != "O" and position_dict[com_dicision] != "X":
                            break

                position_dict[com_dicision] = "X" 
                board(count)
                if count >= 3:
                        if result(count, player_order) == True:
                            break
                count += 1
                while True:
                    try:
                        player_dicision = int(input("Please enter the position you want to mark(enter number 1~9): "))
                        if ((0 < player_dicision < 10) and
                              (position_dict[player_dicision] != "O" and position_dict[player_dicision] != "X")):
                            position_dict[player_dicision] = "O"
                            break
                        else:
                            print("Your position is out of range or it has been occupied!")
                    except:
                        print("Please enter number 1~9")
                        
                board(count)
                
                if count >= 3:
                    if result(count, player_order) == True:
                        break
                count += 1
#############################################################################################################################

    if mode_type == "N":
        count = 1
        while count <= 9:
            if player_order == "1st":
                while True:
                    try:
                        player_dicision = int(input("Please enter the position you want to mark(enter number 1~9): "))
                        if ((0 < player_dicision < 10) and
                            (position_dict[player_dicision] != "O" and position_dict[player_dicision] != "X")):
                            position_dict[player_dicision] = "X"
                            break
                        else:
                            print("Your position is out of range or it has been occupied!")
                    except:
                        print("Please enter number 1~9")

                board(count)
                if count >= 3:
                    if result(count, player_order) == True:
                            break            
                count += 1

                while True:
                    com_dicision = com_motion(count, position_dict, player_dicision)
                    if position_dict[com_dicision] != "O" and position_dict[com_dicision] != "X":
                        break

                position_dict[com_dicision] = "O"

                board(count)
                if count >= 3:
                    if result(count, player_order) == True:
                        break
                count += 1


            else:
                if count == 1:
                    com_docision = 5
                    position_dict[5] = "X"
                    board(count)
                    count += 1
                    
                while True:               
                    try:
                        player_dicision = int(input("Please enter the position you want to mark(enter number 1~9): "))
                        if ((0 < player_dicision < 10) and
                              (position_dict[player_dicision] != "O" and position_dict[player_dicision] != "X")):
                            position_dict[player_dicision] = "O"
                            break
                        else:
                            print("Your position is out of range or it has been occupied!")
                    except:
                        print("Please enter number 1~9")
                board(count)
                if count >= 3:
                    if result(count, player_order) == True:
                        break
                count += 1
                
                while True:
                    com_dicision = com_motion(count, position_dict, player_dicision)
                    if position_dict[com_dicision] != "O" and position_dict[com_dicision] != "X":
                          break
                position_dict[com_dicision] = "X"
                board(count)
                if count >= 3:
                    if result(count, player_order) == True:
                        break
                count += 1
                


# In[9]:


# main code
one_or_two = randint(1,2)
H_T = {1: ["H", "Head"], 2:["T", "Tail"]}
print("------Welcome to Tic-Tac-Toe Game------")
name = input("Please enter your username: ")

while True:
    while True:
        mode_type = input("Choose the game mode: Easy or Normal(enter \"E\" or \"N\"): ")
        if mode_type == "E" or mode_type == "N":
            break
        else:
            print("Please enter \"E\" or \"N\" Thank you!")
    while True:
        player_guess = input("Now guess the side of coin, heads or tails(enter \"H\" or \"T\"): ")
        if  player_guess == "H" or player_guess == "T":
            print("The side is %s !" %H_T[one_or_two][1])
            if player_guess == H_T[one_or_two][0]:
                print("You first!")
                player_order = "1st"
            else:
                print("Computer first!")
                player_order = "2nd"
            break
        else:
            print("Please enter\"H\" or \"T\" Thank you!")
    position_dict = {}
    for i in range(1, 10):
        position_dict[i] = i
    mode(mode_type)
    restart = ""
    while True:
        restart = input("Do yo want to play again?(enter \"Y\" or \"N\")")
        if restart == "Y" or restart == "N":
            break
        else:
            print("Please enter \"Y\" or \"N\" Thank you!")
    if restart == "N":
        break
print("Thank you for playing !")

