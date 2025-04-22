import judge_black_position
import judge_white_position


# 黒石を置く
def black(board, y, x):
    board[y][x] = '○'


# 白石を置く
def white(board, y, x):
    board[y][x] = '●'


# 入力座標に対する黒石の置き位置を判定し、Trueなら置く
def black_place(board, x, y):
    if judge_black_position.black_upper(board, y, x) or\
       judge_black_position.black_upper_right(board, y, x) or\
       judge_black_position.black_right(board, y, x) or\
       judge_black_position.black_lower_right(board, y, x) or\
       judge_black_position.black_lower(board, y, x) or\
       judge_black_position.black_lower_left(board, y, x) or\
       judge_black_position.black_left(board, y, x) or\
       judge_black_position.black_upper_left(board, y, x) is True:
        black(board, y, x)
    else:
        print('置けません')


# 入力座標に対する白石の置き位置を判定し、Trueなら置く
def white_place(board, x, y):
    if judge_white_position.white_upper(board, y, x) or\
       judge_white_position.white_upper_right(board, y, x) or\
       judge_white_position.white_right(board, y, x) or\
       judge_white_position.white_lower_right(board, y, x) or\
       judge_white_position.white_lower(board, y, x) or\
       judge_white_position.white_lower_left(board, y, x) or\
       judge_white_position.white_left(board, y, x) or\
       judge_white_position.white_upper_left(board, y, x) is True:
        white(board, y, x)
    else:
        print('置けません')