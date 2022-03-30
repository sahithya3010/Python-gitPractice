def get_move(player):
    move = ""
    while move not in ["rock", "paper", "scissors"]:
    	move = input(f"{player} make your move (rock, paper, scissors): ")
    return move

def is_first_winner(first,second):
    if first == "rock" and second == "scissors" or \
			first == "paper" and second == "rock" or \
			first == "scissors" and second == "paper": 
            return True
    return False

while True:
    player_1 = get_move("Player_1")
    player_2 = get_move("Player_2")
    if player_1 == player_2:
        winner_mesage = f"Tie! Both have choosen {player_1}"
    elif is_first_winner(player_1, player_2):
        winner_mesage = "Player 1 is winner"
    elif is_first_winner(player_2, player_1):
        winner_mesage = "Player 2 is the winner"
    print(winner_mesage)
    reply_to_continue = ""
    # while reply_to_continue not in ["y", "n"]:
    reply_to_continue = input("Do you want to continue? y or n :")
    if reply_to_continue.lower() == 'y':
        continue
    elif reply_to_continue.lower() == 'n':
        break
    

