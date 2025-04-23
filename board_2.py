# 最初の盤面を作成
def create_bord():
    board_rc = []
    for i in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-'])
    initial_position(board_rc)


# 現在の盤面を表示
def show_board(board: list[list[str]]):
    for row in board:
        print(*row)


# 初期配置
def initial_position(board: list[list[str]]):
    board[3][3] = '●'
    board[4][4] = '●'
    board[4][3] = '○'
    board[3][4] = '○'


# 空きマスが残っているか判定(残っていたらFalse)
def is_full(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True


# 勝敗判定
def judgement(board: list[list[str]]):
    black = 0
    white = 0
    for row in board:
        black += row.count('○')
        white += row.count('●')
    if black < white:
        print('white win!')
    elif white < black:
        print('black win!')
    else:
        print('draw')

