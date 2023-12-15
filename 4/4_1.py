with open("input.txt", "r") as f:
    running_sum = 0
    for line in f:
        game_sum = 0
        game_idx_lst, game_data_lst = line.strip().split(":")
        win_cards_lst, elf_cards_lst = game_data_lst.split("|")
        elf_cards_lst = elf_cards_lst.split(" ")
        win_cards_lst = win_cards_lst.split(" ")
        win_cards_lst = set(win_cards_lst)
        for card in elf_cards_lst:
            if card in win_cards_lst and card.isnumeric():
                if game_sum==0:
                    game_sum += 1
                else:
                    game_sum *= 2
        running_sum += game_sum
        
print(running_sum)