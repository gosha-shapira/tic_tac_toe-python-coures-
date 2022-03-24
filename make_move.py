# pretty board print function
def print_board(board):
    for i in range(len(board)):
        for x in board:
            print(x[i], end=' ')
        print()

def make_move(char,board):
    while(True):
        usr_input = input (f'Player \'{char}\' Please choose cell: ')
        usr_input =usr_input.split(' ')
        usr_input = [int(x) for x in usr_input]
        if(int(usr_input[0]) < 0 or int (usr_input[0] > 2)):
            print(f'Invalid line chosen {usr_input[0]}')
            print_board(board)
            continue
        if (int(usr_input[1]) < 0 or int (usr_input[1] > 2)):
            print (f'Invalid column chosen {usr_input[1]}')
            print_board (board)
            continue
        if (board[usr_input[0]][usr_input[1]] != '-'):
            print('The cell is taken')
            print_board(board)
            continue
        else:
            break
    board[usr_input[0]][usr_input[1]] = char
    print_board(board)
    return board