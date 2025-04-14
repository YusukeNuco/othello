# 8 * 8 の盤面
def show_board(board: list[list[str]]):
    for row in board:
        print(*row)


# 黒石を置く
def black(board, y, x):
    board[y][x] = '●'


# 白石を置く
def white(board, y, x):
    board[y][x] = '○'


def main():
    board_rc = []
    for _ in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    black(board=board_rc, y=int(input()), x=int(input()))
    white(board=board_rc, y=int(input()), x=int(input()))
    board_rc[3][3] = '●'
    board_rc[4][4] = '●'
    board_rc[4][3] = '○'
    board_rc[3][4] = '○'
    show_board(board=board_rc)


if __name__ == '__main__':
    main()

