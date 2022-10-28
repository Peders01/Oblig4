import random

global bet
global chips
chips = int(input("How many chips do you want to play with?: "))
while True:
    kortstokken = [
        {"name": "Spar 2", "value": 2}, {"name": "Spar 3", "value": 3}, {"name": "Spar 4", "value": 4},
        {"name": "Spar 5", "value": 5}, {"name": "Spar 6", "value": 6}, {"name": "Spar 7", "value": 7},
        {"name": "Spar 8", "value": 8}, {"name": "Spar 9", "value": 9}, {"name": "Spar 10", "value": 10},
        {"name": "Spar Knekt", "value": 10}, {"name": "Spar Dame", "value": 10},
        {"name": "Spar Konge", "value": 10}, {"name": "Spar Ess", "value": 11},
        {"name": "Hjerter 2", "value": 2}, {"name": "Hjerter 3", "value": 3}, {"name": "Hjerter 4", "value": 4},
        {"name": "Hjerter 5", "value": 5}, {"name": "Hjerter 6", "value": 6}, {"name": "Hjerter 7", "value": 7},
        {"name": "Hjerter 8", "value": 8}, {"name": "Hjerter 9", "value": 9}, {"name": "Hjerter 10", "value": 10},
        {"name": "Hjerter Knekt", "value": 10}, {"name": "Hjerter Dame", "value": 10},
        {"name": "Hjerter Konge", "value": 10}, {"name": "Hjerter Ess", "value": 11},
        {"name": "Kløver 2", "value": 2}, {"name": "Kløver 3", "value": 3}, {"name": "Kløver 4", "value": 4},
        {"name": "Kløver 5", "value": 5}, {"name": "Kløver 6", "value": 6}, {"name": "Kløver 7", "value": 7},
        {"name": "Kløver 8", "value": 8}, {"name": "Kløver 9", "value": 9}, {"name": "Kløver 10", "value": 10},
        {"name": "Kløver Knekt", "value": 10}, {"name": "Kløver Dame", "value": 10},
        {"name": "Kløver Konge", "value": 10}, {"name": "Kløver Ess", "value": 11},
        {"name": "Ruter 2", "value": 2}, {"name": "Ruter 3", "value": 3}, {"name": "Ruter 4", "value": 4},
        {"name": "Ruter 5", "value": 5}, {"name": "Ruter 6", "value": 6}, {"name": "Ruter 7", "value": 7},
        {"name": "Ruter 8", "value": 8}, {"name": "Ruter 9", "value": 9}, {"name": "Ruter 10", "value": 10},
        {"name": "Ruter Knekt", "value": 10}, {"name": "Ruter Dame", "value": 10},
        {"name": "Ruter Konge", "value": 10}, {"name": "Ruter Ess", "value": 11}
    ]


    def get_card():
        kortet = random.choice(kortstokken)
        kortstokken.remove(kortet)
        return kortet


    def player_hand():
        while True:

            spillers_hånd = []
            global player_verdi
            player_verdi = 0
            spillers_hånd.append(get_card())
            spillers_hånd.append(get_card())
            print("Du har:")
            for kort in spillers_hånd:
                player_verdi += kort["value"]
                print(kort["name"])
            if player_verdi == 22:
                player_verdi -= 10
            print(f"Verdien av dine kort: {player_verdi}")

            while True:
                hit_or_stand = input(f"Press:\nS for Stand \nH for Hit\n").title()
                if hit_or_stand == "H":
                    player_verdi = 0
                    spillers_hånd.append(get_card())
                    print("Du har:")
                    for kort in spillers_hånd:
                        player_verdi += kort["value"]
                        print(kort["name"])

                    global chips
                    if player_verdi > 21:
                        for kortene in spillers_hånd:
                            if "Ess" in kortene["name"]:
                                player_verdi -= 10

                        if player_verdi > 21:
                            print("You bust!")
                            chips -= bet
                            print(f"You have {chips} chips")
                            return None


                    elif player_verdi == 21:
                        print("Blackjack, you win!")
                        chips += (bet * 2)
                        print(f"You have {chips} chips")
                        return None
                    else:
                        continue
                    print(f"Verdien av dine kort: {player_verdi}")

                if hit_or_stand == "S":
                    return None


    def dealers_hand():
        global bet
        while True:
            bet = int(input("How many chips do you want to bet?: "))
            if bet < chips:
                break
            else:
                continue
        global deal_verdi
        deal_verdi = 0
        dealer_hand = []
        dealer_hand.append(get_card())
        dealer_hand.append(get_card())
        dealer_kort = [dealer_hand[0]]
        for value in dealer_hand:
            deal_verdi += value["value"]
        for kort in dealer_kort:
            print(f'Dealer har {kort["name"]} som har en verdi: {kort["value"]}')
        for x in range(5):
            if deal_verdi < 17:
                dealer_hand.append(get_card())
                deal_verdi = 0
                for value in dealer_hand:
                    deal_verdi += value["value"]
            if deal_verdi >= 17:
                return deal_verdi


    def game():
        dealers_hand()
        player_hand()

        print(f"Din verdi = {player_verdi}")
        global chips

        if player_verdi > 21:
            print(f"Verdien av dine kort: {player_verdi}")
            return None

        if player_verdi == 21:
            print(f"Verdien av dine kort: {player_verdi}")
            return None

        elif player_verdi > deal_verdi and player_verdi <= 21:
            print(f"Verdien av dine kort: {player_verdi}")
            print("You win!")
            chips += bet
            print(f"You have {chips} chips")

        elif deal_verdi > 21:
            print("Dealer busted!")
            print("You win!")
            chips += bet
            print(f"You have {chips} chips")

        elif deal_verdi > player_verdi:
            print(f"Dealer's verdi = {deal_verdi}")
            print("You lose!")
            chips -= bet
            print(f"You have {chips} chips")

        elif deal_verdi == player_verdi:
            print(f"Dealer's verdi = {deal_verdi}")
            print(f"You have {chips} chips")
            print("No one wins")

    game()
    play_again = input("Do you want to play again[Y/N]?: ").title()
    if play_again == "Y":
        continue
    elif play_again == "N":
        print("😭😭😭")
        break