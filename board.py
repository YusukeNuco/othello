# 8 * 8 の盤面
def show_board(board: list[list[str]]):
    for row in board:
        print(*row)


# 初期配置
def initial_position(board: list[list[str]]):
    board[3][3] = '●'
    board[4][4] = '●'
    board[4][3] = '○'
    board[3][4] = '○'


# 黒石を置く
def black(board, y, x):
    board[y][x] = '○'


# 白石を置く
def white(board, y, x):
    board[y][x] = '●'


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


# 石を置けるかどうか判定
def place(board, y, x):
    if board[x][y] != '-':
        return False
    elif board[y != [0-7]][x != [0-7]]:
        return False
    elif board[y][x+1] == '-' and \
            board[y][x-1] == '-' and \
            board[y-1][x] == '-' and \
            board[y+1][x] == '-' and \
            board[y-1][x+1] == '-' and \
            board[y+1][x+1] == '-' and \
            board[y-1][x-1] == '-' and \
            board[y+1][x-1] == '-':
        return False
    else:
        True

# 右: board[y][x+1]
# 左: board[y][x-1]
# 上: board[y-1][x]
# 下: board[y+1][x]
# 右上: board[y-1][x+1]
# 右下: board[y+1][x+1]
# 左上: board[y-1][x-1]
# 左下: board[y+1][x-1]


def main():
    board_rc = []
    for _ in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    initial_position(board=board_rc)
    print("black")
    by = int(input())
    bx = int(input())
    if place(board=board_rc, y=by, x=bx) is True:
        black(board=board_rc, y=by, x=bx)
    show_board(board=board_rc)
    print('white')
    wy = int(input())
    wx = int(input())
    if place(board=board_rc, y=wy, x=wx) is True:
        white(board=board_rc, y=wy, x=wx)
    show_board(board=board_rc)


if __name__ == '__main__':
    main()
