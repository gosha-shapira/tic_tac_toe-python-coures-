
import check_board
import make_move

def tic_tac_toe():
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    move_counter = 0
    while(check_board.check_board(board) or move_counter < 9):
        if(move_counter % 2):
            board = make_move.make_move('X', board)
            if(check_board.check_board(board)):
                return
            move_counter += 1
        else:
            board = make_move.make_move('O', board)
            if(check_board.check_board(board)):
                return
            move_counter += 1
    
    print('It\'s a draw')

if '__init__':
    tic_tac_toe()