# 8 * 8 の盤面
def show_board(board: list[list[str]]):
    for row in board:
        print(*row)


# 黒石を置く
def black(board, y, x):
    if board[y][x] == '-':
        board[y][x] = '○'
    else:
        print('置けません')


# def black(board, y, x):
#     while board[y][x] == '-':
#         board[y][x] = '○'


# 白石を置く
def white(board, y, x):
    if board[y][x] == '-':
        board[y][x] = '●'
    else:
        print('置けません')


# 勝敗判定
def judgement(board: list[list[str]]):
    black = 0
    white = 0
    for row in board:
        black += row.count('○')
        white += row.count('●')
    if black < white:
        print('white win!')
        print(black)
        print(white)
    elif white < black:
        print('black win!')
        print(black)
        print(white)
    else:
        print('draw')
        print(black)
        print(white)


def main():
    board_rc = []
    for _ in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    board_rc[3][3] = '●'
    board_rc[4][4] = '●'
    board_rc[4][3] = '○'
    board_rc[3][4] = '○'
    print("black")
    black(board=board_rc, y=int(input()), x=int(input()))
    print("white")
    white(board=board_rc, y=int(input()), x=int(input()))
    show_board(board=board_rc)
    judgement(board=board_rc)


if __name__ == '__main__':
    main()
