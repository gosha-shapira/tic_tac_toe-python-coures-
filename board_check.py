# trying to make it generic for any n x n board
def check_row(row: list):
    if(row.count(row[0]) == len(row) and row[0] == 'X'):
        return 'X - wins!'
    elif(row.count(row[0]) == len(row) and row[0] == 'O'):
        return 'O - wins!'
    else:
        return None

def check_rows(board):
    for i in range(len(board)):
        check = check_row[i]
        if(check):
            return check
    return None

def check_col(board):
    for i in range(len(board)):
        check = check_row([item[i] for item in board])
        if(check):
            return check
    return None

def check_cross(board): # only for a 3 x 3 board
    if((board[0][0] == board[1][1] == board[2][2] == 'X') or (board[0][2] == board[1][1] == board[2][0] == 'X')):
        return 'X - wins!'
    elif((board[0][0] == board[1][1] == board[2][2] == 'O') or (board[0][2] == board[1][1] == board[2][0] == 'O')):
        return 'O - wins!'
    else:
        return None

def Check_board(board: list): # recieving list of lists
    rows_win = check_rows(board)
    if(rows_win):
        print(rows_win)
        return True
    
    col_win = check_col(board)
    if(col_win):
        print(col_win)
        return True

    cross_win = check_col(board)
    if(cross_win):
        print(cross_win)
        return True

    else:
        print(' ')
        return False