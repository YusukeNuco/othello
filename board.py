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


# # 石を置けるかどうか判定
# def place(board, y, x):
#     # 石の上に石を置こうとした時 False: 動いた
#     if board[y][x] != '-':
#         return False
#     # 八方に石がない場所に石を置こうとした時 False: 動いたが、いらないかも。
#     elif board[y][x+1] == '-' and \
#             board[y][x-1] == '-' and \
#             board[y-1][x] == '-' and \
#             board[y+1][x] == '-' and \
#             board[y-1][x+1] == '-' and \
#             board[y+1][x+1] == '-' and \
#             board[y-1][x-1] == '-' and \
#             board[y+1][x-1] == '-':
#         return False
#     # # 盤外に石を置こうとした時 False: 動かない
#     # IndexError: list index out of range のエラーが先に出る
#     # elif board[y != [0-7]][x != [0-7]]:
#     #     return False
#     else:
#         return True


def by_input():
    black_y = input('Y座標を入力してください: ')
    if black_y == 0:
        return black_y
    else:
        print('座標は0-7で入力してください')
        return by_input()


def bx_input():
    black_x = input('X座標を入力してください: ')
    if black_x == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7:
        return black_x
    else:
        print('座標は0-7で入力してください')
        return bx_input()


def main():
    board_rc = []
    for _ in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    initial_position(board=board_rc)
    print("black")
    by = by_input()
    bx = bx_input()
    if place(board=board_rc, y=by, x=bx) is True:
        black(board=board_rc, y=by, x=bx)
    else:
        print('置けません')
    show_board(board=board_rc)
    print('white')
    wy = int(input())
    wx = int(input())
    if place(board=board_rc, y=wy, x=wx) is True:
        white(board=board_rc, y=wy, x=wx)
    else:
        print('置けません')
    show_board(board=board_rc)


if __name__ == '__main__':
    main()
