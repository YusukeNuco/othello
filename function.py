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
    elif white < black:
        print('black win!')
    else:
        print('draw')


def main():
    board_rc = []
    for _ in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    board_rc[3][3] = '●'
    board_rc[4][4] = '●'
    board_rc[4][3] = '○'
    board_rc[3][4] = '○'
    print("black")
    by = int(input())
    bx = int(input())
    black(board=board_rc, y=by, x=bx)
    show_board(board=board_rc)
    while board_rc[by][bx] != '○':
        by2 = int(input())
        bx2 = int(input())
        black(board=board_rc, y=by2, x=bx2)
        show_board(board=board_rc)
        if board_rc[by2][bx2] == '○':
            break
    show_board(board=board_rc)
    print("white")
    wy = int(input())
    wx = int(input())
    white(board=board_rc, y=wy, x=wx)
    show_board(board=board_rc)
    while board_rc[wy][wx] != '●':
        wy2 = int(input())
        wx2 = int(input())
        white(board=board_rc, y=wy2, x=wx2)
        show_board(board=board_rc)
        if board_rc[wy2][wx2] == '●':
            break
    show_board(board=board_rc)
    judgement(board=board_rc)


if __name__ == '__main__':
    main()
