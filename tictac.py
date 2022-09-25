def main():
    board = create_board()
    variable = True
    player = "x"
    while variable:
        
        display_board(board)
        make_move(board, player)
        if check_sequence(board):
            print(f"{player} has won the game!")
            variable = False
        elif check_draw(board):
            print("Game has ended in a draw!")
            variable = False
        player = change_player(player)
    display_board(board)
        
# Create Board
def create_board():
    board = []
    for i in range(9):
        board.append(i + 1)
    return board
print(create_board())        
# Display board

def display_board(board):
    print(board[0], "|" , board[1], "|" , board[2])
    print ("----------")
    print(board[3], "|" , board[4], "|" , board[5])
    print ("----------")
    print(board[6], "|" , board[7], "|" , board[8])


# Make Move
def make_move(board, player_symbol):
    
    input_condition = int(input(f"{player_symbol}'s turn Enter a Number between 1 - 9: "))
    board[input_condition - 1] = player_symbol
    
    
#Check winner
def check_sequence(board):
  
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
       
# Check draw
def check_draw(board):
    for i in range(9):
        if board[i] != "x" and board[i] != "o":
            return False
    return True
# Switch
def change_player(symbol):
    if symbol == "o" or "":
        symbol = "x"
    elif symbol == "x":
        symbol = "o"
    return symbol
# Make Move

if __name__ == '__main__':
    main()