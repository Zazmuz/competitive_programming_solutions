syllable_amount, player_amount = map(int, input().split())
player_list = []
for i in range(player_amount):
    player_list.append(3)
    player_list.append(0)

current_player = -1
last_player = -1
i_hate_life = {}
for i in range(0,player_amount*2,2):
    i_hate_life[i] = i//2 + 1
    i_hate_life[i+1] = i // 2 + 1



while any(player_list):

    for i in range(syllable_amount):
        current_player = (current_player + 1) % len(player_list)
        while player_list[current_player] == 0:
            current_player = (current_player + 1) % len(player_list)

    if player_list[current_player] == 3:
        player_list[current_player] = 2
        last_player = current_player
        player_list[current_player + 1] = 2
        current_player = current_player - 1
    elif player_list[current_player] == 2:
        player_list[current_player] = 1
        last_player = current_player

    elif player_list[current_player] == 1:
        player_list[current_player] = 0
        last_player = current_player
 #   print(player_list, current_player)
print(i_hate_life[last_player])
#print(last_player)