# Choose Symbols for players
player1_symbol = ''
player2_symbol = ''
board_map = [" " for x in range(10)]
player_turn = 1
is_win_or_draw = False
total_moves = 0


def game_init():
    global player1_symbol
    global player2_symbol
    while True:
        player1_symbol = input("Player 1 Choose Your Symbol X or O: ")
        player2_symbol = ''
        if player1_symbol == 'X':
            player2_symbol = 'O'
            break
        elif player1_symbol == 'O':
            player2_symbol = 'X'
            break
        else:
            print("Invalid Symbol, Please try again")

    print(f'Player 1 if {player1_symbol} and Player 2 is {player2_symbol}.\nPlayer 1 starts first.\nLets Play!')


def player_turn_switch():
    global player_turn
    if player_turn == 1:
        player_turn = 2
    elif player_turn == 2:
        player_turn = 1


def print_board():
    print(f" {board_map[6]} | {board_map[7]} | {board_map[8]} \n-----------\n {board_map[3]} | {board_map[4]} | {board_map[5]} \n-----------\n {board_map[0]} | {board_map[1]} | {board_map[2]} ")


def make_move():
    # Takes in player move, validates it and switches the player turn
    global total_moves
    while True:
        next_move = input(f"Player {player_turn} next move: ")
        if board_map[int(next_move) - 1] != " ":
            print("Square is already filled")
        elif 0 < int(next_move) < 10:
            if player_turn == 1:
                board_map[int(next_move) - 1] = player1_symbol
                print_board()
                player_turn_switch()
                total_moves += 1
                break
            else:
                board_map[int(next_move) - 1] = player2_symbol
                print_board()
                player_turn_switch()
                total_moves += 1
                break
        else:
            print("Invalid Input")


def check_win():
    global is_win_or_draw
    # Horizontal Bottom
    if board_map[0] == board_map[1] == board_map[2] == player1_symbol:
        print('Player 1 wins')
        is_win_or_draw = True
    elif board_map[0] == board_map[1] == board_map[2] == player2_symbol:
        print("Player 2 wins")
        is_win_or_draw = True

    # Horizontal Middle
    elif board_map[3] == board_map[4] == board_map[5] == player1_symbol:
        print('Player 1 wins')
        is_win_or_draw = True
    elif board_map[3] == board_map[4] == board_map[5] == player2_symbol:
        print('Player 2 wins')
        is_win_or_draw = True

    # Horizontal Top
    elif board_map[6] == board_map[7] == board_map[8] == player1_symbol:
        print('Player 1 wins')
        is_win_or_draw = True
    elif board_map[6] == board_map[7] == board_map[8] == player2_symbol:
        print('Player 2 wins')
        is_win_or_draw = True

    # Vertical Left
    elif board_map[0] == board_map[3] == board_map[6] == player1_symbol:
        print('Player 1 wins')
        is_win_or_draw = True
    elif board_map[0] == board_map[3] == board_map[6] == player2_symbol:
        print('Player 2 wins')
        is_win_or_draw = True

    # Vertical Middle
    elif board_map[1] == board_map[4] == board_map[7] == player1_symbol:
        print('Player 1 wins')
        is_win_or_draw = True
    elif board_map[1] == board_map[4] == board_map[7] == player2_symbol:
        print('Player 2 wins')
        is_win_or_draw = True

    # Vertical Right
    elif board_map[2] == board_map[5] == board_map[8] == player1_symbol:
        print('Player 1 wins')
        is_win_or_draw = True
    elif board_map[2] == board_map[5] == board_map[8] == player2_symbol:
        print('Player 2 wins')
        is_win_or_draw = True

    # Diagonal Back
    elif board_map[6] == board_map[4] == board_map[2] == player1_symbol:
        print('Player 1 wins')
        is_win_or_draw = True
    elif board_map[6] == board_map[4] == board_map[2] == player2_symbol:
        print('Player 2 wins')
        is_win_or_draw = True

    # Diagonal Forward
    elif board_map[8] == board_map[4] == board_map[0] == player1_symbol:
        print('Player 1 wins')
        is_win_or_draw = True
    elif board_map[8] == board_map[4] == board_map[0] == player2_symbol:
        print('Player 2 wins')
        is_win_or_draw = True

    else:
        is_win_or_draw = False


def check_draw():
    global is_win_or_draw
    if total_moves == 9 and is_win_or_draw == False:
        is_win_or_draw = True
        print("Draw")


game_init()


while not is_win_or_draw:
    make_move()
    check_win()
    check_draw()
