card_lookup = {'Shadow': 6, 'Gale': 5, 'Ranger': 4, 'Anvil': 7, 'Vexia': 3, 'Guardian': 8, 'Thunderheart': 6, 'Frostwhisper': 2, 'Voidclaw': 3, 'Ironwood': 3, 'Zenith': 4, 'Seraphina': 1}#{"Shadow": 6, "Gale":5, "Ranger": 4, "Anvil":7, "Vexia":3, "Guardian": 8, "Thunderheart": 6, "Frostwhisper": 2, "Voidclaw": 3, "Ironwood":3, "Zenith":4, "Seraphina":1}

locationswon_p1 = 0
locationswon_p2 = 0

totalpowerlevel_p1 = 0
totalpowerlevel_p2 = 0

p1_currentlocation = 0
p2_currentlocation = 0

for i in range(6):
    cards = input().split()[1:]
    if i % 2 == 0:
        for card in cards:
            p1_currentlocation += card_lookup[card]
            if card == "Thunderheart":
                if len(cards) == 4:
                    p1_currentlocation += card_lookup[card]
            elif card == "Zenith":
                if i == 2:
                    p1_currentlocation += 5
            elif card == "Seraphina":
                p1_currentlocation += len(cards)-1

        totalpowerlevel_p1 += p1_currentlocation

    else:
        for card in cards:
            p2_currentlocation += card_lookup[card]

            if card == "Thunderheart":
                if len(cards) == 4:
                    p2_currentlocation += card_lookup[card]
            elif card == "Zenith":
                if i == 3:
                    p2_currentlocation += 5
            elif card == "Seraphina":
                p2_currentlocation += len(cards) - 1
        totalpowerlevel_p2 += p2_currentlocation

        if p2_currentlocation > p1_currentlocation:
            locationswon_p2 += 1
        elif p1_currentlocation > p2_currentlocation:
            locationswon_p1 += 1


        p1_currentlocation = 0
        p2_currentlocation = 0

if locationswon_p1 > locationswon_p2:
    print("Player 1")
elif locationswon_p2 > locationswon_p1:
    print("Player 2")
else:
    if totalpowerlevel_p1 > totalpowerlevel_p2:
        print("Player 1")
    elif totalpowerlevel_p2 > totalpowerlevel_p1:
        print("Player 2")
    else:
        print("Tie")