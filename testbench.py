import chesslogic

board_starting_state = [['BR', 'BN', 'BB', 'BK', 'BQ', 'BB', 'BN', 'BR'],
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    ['WR1', 'WN', 'WB', 'WK', 'WQ', 'WB', 'WN', 'WR2']]



flipped_white_board = [
    ['WR1', 'WN', 'WB', 'WK', 'WQ', 'WB', 'WN', 'WR2'],
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    ['BR', 'BN', 'BB', 'BK', 'BQ', 'BB', 'BN', 'BR']




]

chesslogic_sample = chesslogic.Chesslogic()
chesslogic_sample.setBoard(flipped_white_board)
print(flipped_white_board[1][3])
print(flipped_white_board[2][2])
print(flipped_white_board[7][7])
print(flipped_white_board[0][1])
#y, x coord
print(chesslogic_sample.validate((1, 3), (3, 3)))
print(chesslogic_sample.validate((1, 3), (2, 3)))
print(chesslogic_sample.validate((1, 3), (2, 3)))



board_starting_state = [['BR', 'BN', 'BB', 'BK', 'BQ', 'BB', 'BN', 'BR'],
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'WP', 'EE', 'EE', 'EE'],
    ['EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE', 'EE'],
    ['WP', 'WP', 'WP', 'WP', 'EE', 'WP', 'WP', 'WP'],
    ['WR1', 'WN', 'WB', 'WK', 'WQ', 'WB', 'WN', 'WR2']]

chesslogic_sample