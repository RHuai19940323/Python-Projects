#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 52 playing cards
# Spade, Heart, Diamond, Club
# Ace : 11 or 1(if the card over than __)
# J, Q, K : 10
# Others: number of cards 

# Start round
# 1. player places bets
# 2. dealing two cards to the player
# 3. dealer's cards: 1 face up, another face down
# 4. If a player total of 21 on  the first two cards is a "Black Jack",  and the player wins immediately.
# 5. elif a dealer total of 21 on  the first two cards is a "Black Jack", and the dealer wins immediately.
# 6. elif player's decision
    # Hit : take a card until stand or bust
    # Stand : end turn
    # Double : wager * 2 -> take a card -> end turn
    # Split: if the first two cards are the same value, each new hand gets another card, the player has two starting hands
        #    requiring another bet on the second hand
        #    making decision(Hit, Stand) for each hand until ending the round
    # if busting, dealer wins immediately
# 7. if dealer total on first two cards is <= 17, taking cards until >= 17 and <= 21
# comparing the total, if player total > dealer total: player wins, else dealer wins
# computing the bets
# end game: enter 0 or palyer's bets 


# In[1]:


from random import randint
            
def get_card_value(card):
    if card[-1] == "A":
        return 11
    elif card[-1] == "J" or card[-1] == "Q" or card[-1] == "K":
        return 10
    else:
        return int(card[-2] + card[-1])
        
def take_a_card(card, card_value, count_card):
    shuffle = randint(0, count_card)
    card.append(trump[shuffle])
    card_value.append(get_card_value(card[len(card)-1]))
    del trump[shuffle]
    count_card -= 1
    return count_card

def print_cards(cards):
    current_card = "Current cards: " 
    for i in range(0, len(cards)):
        if i < len(cards) - 1:
            current_card += (cards[i] +", ")
        else:
            current_card += cards[i]
    print(current_card)

def total_card_value(cards, card_value):
    for i in range(0, len(cards)):
        if cards[i][-1] == "A" and sum(card_value) > 21 and card_value[i] == 11:
            card_value[i] -= 10
    return card_value


def Hit(player_cards, player_card_value, count_card, player_decision):
    hit_player_decision = player_decision
    while sum(player_card_value) < 21:
        count_card = take_a_card(player_cards, player_card_value, count_card)
        print_cards(player_cards)
        player_card_value = total_card_value(player_cards, player_card_value)
        print("Your current card totals: %i" %sum(player_card_value))
        if sum(player_card_value) >= 21:
            break
            
        while True:
            try:
                hit_player_decision = int(input("Make decision (1) Hit (2) Stand : "))
                if 1 <= hit_player_decision <= 2:
                    break
                else:
                    print("Please enter the number1~2, thank you!")
                            
            except:
                print("Invalid enter !")
                       
        if hit_player_decision == 1:
            print("Hit !")
        else:
            print("Stand !")
            break

    return (count_card, hit_player_decision)

def make_decision(**player):
    if player["player_decision"] == 1:
        print("Hit !")
        player["count_card"], player["player_decision"] = Hit(player["player_cards"], player["player_card_value"], player["count_card"], player["player_decision"])
        
    elif player["player_decision"] == 2:
        print("Stand !")
    else:
        print("Double !")
        print("Your current chips : %i" %player["total_chips"])
        player["count_card"] = take_a_card(player["player_cards"], player["player_card_value"], player["count_card"])
        print_cards(player["player_cards"])
        player["player_card_value"] = total_card_value(player["player_cards"], player["player_card_value"])
        print("Your current card totals: %i" %sum(player["player_card_value"]))
    return player["count_card"]

def win_or_lose(**value_and_chips):
    if sum(value_and_chips["player_card_value"]) <= 21:
        if sum(value_and_chips["dealer_card_value"]) > 21:
            print("You win !!!")
            value_and_chips["total_chips"] += value_and_chips["placing_chips"]*2
        elif sum(value_and_chips["player_card_value"]) > sum(value_and_chips["dealer_card_value"]):
            print("You win !!!")
            value_and_chips["total_chips"] += value_and_chips["placing_chips"]*2
        else:
            print("You lose !!!")
    else:
        print("You lose !!!")
    return value_and_chips["total_chips"]

#-----main-----

print("Welcome to \"BlackJack\"!")
name = input("Please enter your username: ")

print("================================================================================================================")

while True:
    tutorial_need = input("Do you need a BlackJack game tutorial?(enter \"Y\" or\"N\")")
    if tutorial_need == "Y" or tutorial_need == "N":
        break
    else:
        print("Please enter \"Y\" or\"N\"")
if tutorial_need == "Y":
    print("1. How to win:")
    print("    1.1  On your first two cards, you get exactly 21 card totals(called\"BlackJack\"), you win immediately.")
    print("    1.2  If you don't get BlackJack, you should make decision.Then comparing your card totals with the dealer's")
    print("2. Decisions:")
    print("    2.1  Hit : taking a card.")
    print("    2.2  Stand : doing nothing , and ending your turn.")
    print("    2.3  Double: placing the same number of starting chips , then taking a card, and ending your turn.")
    print("    2.4  Split : when your first two cards have the same value, you can placing them separately, ")
    print("                 and placing the same number of starting chips for second place.")
    print("                 Then they will get another card independently.Making decision for the first place.")
    print("                 If first place is end, then making decision for the second place.")
    print("3. When you lose:")
    print("    3.1  If you don't get BlackJack, but dealer get, you lose immediately.")
    print("    3.2  If your card totals exceeding 21(called \"Bust\")")
    print("    3.3  If your card totals are not larger than the dealer's.")
print("You have 100 gambling chips.")
print("For each round, you have to place at least 5 chips to start.")
print("If you enter \"0\", the chips which you have will be the final scores, and end this game.")
print("Let's gamble!")
print("================================================================================================================")
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spade", "Heart", "Diamond", "Club"]
trump = []
count_card = 51
for i in range(0, 4):
    for j in range(0, 13):
        trump.append(suits[i] + " " + numbers[j])

total_chips = 100
while True:

    print("Your total chips : %i" %total_chips)
    while True:
        try:
            placing_chips = int(input("How many chips do you want to place: "))
            if 1 <= placing_chips <= 4:
                print("You must place at least 5 chips!")
            else:
                break
        except:
            print("Invalid enter !")
    if placing_chips == 0:
        break
    total_chips -= placing_chips

    print("Your current chips : %i" %total_chips)
    player_cards = []
    player_card_value = []
    dealer_cards = []
    dealer_card_value = []
    
    
    for i in range(0, 2):
        count_card = take_a_card(player_cards, player_card_value, count_card) 
        count_card = take_a_card(dealer_cards, dealer_card_value, count_card)

    print(f"Your first two cards: {player_cards[0]}, {player_cards[1]}")
    player_card_value = total_card_value(player_cards, player_card_value)
    print("Your current card totals: %i" %sum(player_card_value))
    print(f"One of Dealer's cards : {dealer_cards[0]}")
    dealer_card_value = total_card_value(dealer_cards, dealer_card_value)
    
    while True:
        # 是否BlackJack
        
        if sum(player_card_value) == 21:
            print("You got BlackJack !!! You win !")
            total_chips += int(2.5 * placing_chips)
            break     
        elif sum(dealer_card_value) == 21:
            print(f"Dealer's first two cards: {dealer_cards[0]}, {dealer_cards[1]}")
            print("Dealer got BlackJack !!! You lose !")
            break
        
        # 是否Split
        if player_card_value[0] == player_card_value[1] or player_cards[0][-1] == player_cards[1][-1]:
            while True:
                try:
                    player_decision = int(input("Make decision (1) Hit (2) Stand (3) Double (4) Split : "))
                    if 1 <= player_decision <= 4:
                        break
                    else:
                        print("Please enter the number 1 ~ 4, thank you!")
                except:
                    print("Invalid enter !")
            if player_decision == 4:
                print("Split !")
                total_chips -= placing_chips
                placing_chips_A, placing_chips_B = placing_chips, placing_chips
                print("Your current chips : %i" %total_chips)
                print("Each hand will be independent.")
                player_card_A = [player_cards[0]]
                player_card_value_A = [player_card_value[0]]
                count_card = take_a_card(player_card_A, player_card_value_A, count_card)
                print("On A side")
                print_cards(player_card_A)
                print("Your current card totals: %i" %sum(player_card_value_A))
                if sum(player_card_value_A) == 21:
                    print("You got BlackJack !!! You win !")
                    total_chips += int(2.5 * placing_chips)
                else:                    
                    while True:
                        try:
                            player_decision = int(input("Make decision (1) Hit (2) Stand (3) Double : "))
                            if 1 <= player_decision <= 3:
                                break
                            else:
                                print("Please enter the number1~3, thank you!")

                        except:
                            print("Invalid enter!")

                    if player_decision == 3:
                        total_chips -= placing_chips_A
                        placing_chips_A *= 2

                    count_card = make_decision(player_decision = player_decision, player_cards = player_card_A,
                                                player_card_value = player_card_value_A, count_card = count_card, 
                                                total_chips = total_chips)                     


                    if sum(player_card_value_A) > 21:
                        print("Bust!!!!! A side loses !")
                    
                player_card_B = [player_cards[1]]
                player_card_value_B = [player_card_value[1]]
                count_card = take_a_card(player_card_B, player_card_value_B, count_card)
                print("On B side")
                print_cards(player_card_B)
                print("Your current card totals: %i" %sum(player_card_value_B))
                
                if sum(player_card_value_B) == 21:
                    print("You got BlackJack !!! You win !")
                    total_chips += int(2.5 * placing_chips)
                    
                else:                   
                    while True:
                        try:
                            player_decision = int(input("Make decision (1) Hit (2) Stand (3) Double : "))
                            if 1 <= player_decision <= 3:
                                break
                            else:
                                print("Please enter the number1~3, thank you!")

                        except:
                            print("Invalid enter!")

                    if player_decision == 3:
                        total_chips -= placing_chips_B
                        placing_chips_B *= 2

                    count_card = make_decision(player_decision = player_decision, player_cards = player_card_B,
                                                player_card_value = player_card_value_B, count_card = count_card, 
                                                total_chips = total_chips)


                    if sum(player_card_value_B) > 21:
                        print("Bust!!!!! B side loses !")
                        break
                
                print("--------------------Dealer Side---------------------")
                print(f"Dealer's cards : {dealer_cards[0]}, {dealer_cards[1]}")
                print("Dealer's current card totals: %i" %sum(dealer_card_value))

                while sum(dealer_card_value) < 17:
                    count_card = take_a_card(dealer_cards, dealer_card_value, count_card)
                    print_cards(dealer_cards)
                    dealer_card_value = total_card_value(dealer_cards, dealer_card_value)
                    print("Dealer's current card totals: %i" %sum(dealer_card_value))
                print("----------------------------------------------------")
                print("On A side")
                total_chips = win_or_lose(dealer_card_value = dealer_card_value, player_card_value = player_card_value_A, 
                                            placing_chips = placing_chips_A, total_chips = total_chips)
                print("On B side")
                total_chips = win_or_lose(dealer_card_value = dealer_card_value, player_card_value = player_card_value_B, 
                                            placing_chips = placing_chips_B, total_chips = total_chips)
                break

            # 可以split，但選擇其他   
            else:
                if player_decision == 3:
                    total_chips -= placing_chips
                    placing_chips *= 2
                    
                count_card = make_decision(player_decision = player_decision, player_cards = player_cards,
                                            player_card_value = player_card_value, count_card = count_card, 
                                            total_chips = total_chips)
                
                if sum(player_card_value) > 21:
                    print("Bust!!!!! You lose !")
                    break
                    
                print("--------------------Dealer Side---------------------")
                print(f"Dealer's cards : {dealer_cards[0]}, {dealer_cards[1]}")
                print("Dealer's current card totals: %i" %sum(dealer_card_value))

                while sum(dealer_card_value) < 17:
                    count_card = take_a_card(dealer_cards, dealer_card_value, count_card)
                    print_cards(dealer_cards)
                    dealer_card_value = total_card_value(dealer_cards, dealer_card_value)
                    print("Dealer's current card totals: %i" %sum(dealer_card_value))
                print("----------------------------------------------------")
                
                total_chips = win_or_lose(dealer_card_value = dealer_card_value, player_card_value = player_card_value, 
                                            placing_chips = placing_chips, total_chips = total_chips)
                break

                
        # 兩張牌不一樣的情況
        else:
            while True:
                try:
                    player_decision = int(input("Make decision (1) Hit (2) Stand (3) Double : "))
                    if 1 <= player_decision <= 3:
                        break
                    else:
                        print("Please enter the number1~3, thank you!")

                except:
                    print("Invalid enter!")
            if player_decision == 3:
                total_chips -= placing_chips
                placing_chips *= 2
                
            count_card = make_decision(player_decision = player_decision, player_cards = player_cards,
                                        player_card_value = player_card_value, count_card = count_card, 
                                        total_chips = total_chips)

            if sum(player_card_value) > 21:
                print("Bust!!!!! You lose !")
                break
                
            print("--------------------Dealer Side---------------------")
            print(f"Dealer's cards : {dealer_cards[0]}, {dealer_cards[1]}")
            print("Dealer's current card totals: %i" %sum(dealer_card_value))

            while sum(dealer_card_value) < 17:
                count_card = take_a_card(dealer_cards, dealer_card_value, count_card)
                print_cards(dealer_cards)
                dealer_card_value = total_card_value(dealer_cards, dealer_card_value)
                print("Dealer's current card totals: %i" %sum(dealer_card_value))
            print("----------------------------------------------------")
            total_chips = win_or_lose(dealer_card_value = dealer_card_value, player_card_value = player_card_value, 
                                        placing_chips = placing_chips, total_chips = total_chips)
            break

    print("number of cards : %i" %count_card)    
    # 洗牌
    if count_card <= 8:
        print("Shuffle cards !")
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Spade", "Heart", "Diamond", "Club"]
        trump = []
        count_card = 51
        for i in range(0, 4):
            for j in range(0, 13):
                trump.append(suits[i] + " " + numbers[j])
            
    # 籌碼不足，強制結束遊戲
    if total_chips <= 4:
        print("Your chips are less than 5, game over !")
        break
    print("=======================================================")
    
print("Your final scores : %i" %total_chips)
print("Thank you for playing this game")

