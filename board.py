# 右端までずっと白が続いた場合(ずっとcontinueの場合）どうなる？

# 上探索
def black_upper(board, y, x):
    gap = y
    if board[y-1][x] != '●':
        return False
    else:
        for i in range(gap):
            if board[y-i-1][x] == '○':
                return True
                break
            elif board[y-i-1][x] == '-':
                return False
            else:
                continue


def white_upper(board, y, x):
    gap = y
    if board[y-1][x] != '○':
        return False
    else:
        for i in range(gap):
            if board[y-i-1][x] == '●':
                return True
                break
            elif board[y-i-1][x] == '-':
                return False
            else:
                continue


# 右上探索
def black_upper_right(board, y, x):
    gap = y
    if board[y-1][x+1] != '●':
        return False
    else:
        for i in range(gap):
            if board[y-i-1][x+i+1] == '○':
                return True
                break
            elif board[y-i-1][x+i+1] == '-':
                return False
            else:
                continue


def white_upper_right(board, y, x):
    gap = y
    if board[y-1][x+1] != '○':
        return False
    else:
        for i in range(gap):
            if board[y-i-1][x+i+1] == '●':
                return True
                break
            elif board[y-i-1][x+i+1] == '-':
                return False
            else:
                continue


# 右探索
def black_right(board, y, x):
    gap = 7-x                                           # X座標と右端との差分を gap に格納
    if board[y][x+1] != '●':                            # 右が白石じゃないなら置けない。
        return False
    else:                                               # 右が白石だったら
        for i in range(gap):                            # 白石より右にある黒石を、差分の数だけ探索していく
            if board[y][x+i+1] == '○':                  # 白石より右側に黒石を見つけたら
                return True                                    # 入力した座標に石を置く。
                break                                   # 置いた時点で右への探索を切り上げる。
            elif board[y][x+i+1] == '-':                # 白石より右側に何もなかった場合、置けない。
                return False
            else:
                continue                                # '○' でも '-' でもない = 白石だった場合何もしない。


def white_right(board, y, x):
    gap = 7-x
    if board[y][x+1] != '○':
        return False
    else:
        for i in range(gap):
            if board[y][y+i*1] == '●':
                return True
                break
            elif board[y][x+i+1] == '-':
                return False
            else:
                continue


# 右下探索
def black_lower_right(board, y, x):
    gap = 7-x
    if board[y+1][x+1] != '●':
        return False
    else:
        for i in range(gap):
            if board[y+i+1][x+i+1] == '○':
                return True
                break
            elif board[y+i+1][x+i+1] == '-':
                return False
            else:
                continue


def white_lower_right(board, y, x):
    gap = 7-x
    if board[y+1][x+1] != '○':
        return False
    else:
        for i in range(gap):
            if board[y+i+1][x+i+1] == '●':
                return True
                break
            elif board[y+i+1][x+i+1] == '-':
                return False
            else:
                continue


# 下探索
def black_lower(board, y, x):
    gap = 7-y
    if board[y+1][x] != '●':
        return False
    else:
        for i in range(gap):
            if board[y+i+1][x] == '○':
                return True
                break
            elif board[y+i+1][x] == '-':
                return False
            else:
                continue


def white_lower(board, y, x):
    gap = 7-y
    if board[y+1][x] != '○':
        return False
    else:
        for i in range(gap):
            if board[y+i+1][x] == '●':
                return True
                break
            elif board[y+i+1][x] == '-':
                return False
            else:
                continue


# 左下探索
def black_lower_left(board, y, x):
    gap = x
    if board[y+1][x-1] != '●':
        return False
    else:
        for i in range(gap):
            if board[y+i+1][x-i-1] == '○':
                return True
                break
            elif board[y+i+1][x-i-1] == '-':
                return False
            else:
                continue


def white_lower_left(board, y, x):
    gap = x
    if board[y+1][x-1] != '○':
        return False
    else:
        for i in range(gap):
            if board[y+i+1][x-i-1] == '●':
                return True
                break
            elif board[y+i+1][x-i-1] == '-':
                return False
            else:
                continue


# 左探索
def black_left(board, y, x):
    gap = x
    if board[y][x-1] != '●':
        return False
    else:
        for i in range(gap):
            if board[y][x-i-1] == '○':
                return True
                break
            elif board[y][x-i-1] == '-':
                return False
            else:
                continue


def white_left(board, y, x):
    gap = x
    if board[y][x-1] != '○':
        return False
    else:
        for i in range(gap):
            if board[y][x-i-1] == '●':
                return True
                break
            elif board[y][x-i-1] == '-':
                return False
            else:
                continue


# 左上探索
def black_upper_left(board, y, x):
    gap = x
    if board[y-1][x-1] != '●':
        return False
    else:
        for i in range(gap):
            if board[y-i-1][x-i-1] == '○':
                return True
                break
            elif board[y-i-1][x-i-1] == '-':
                return False
            else:
                continue


def white_upper_left(board, y, x):
    gap = x
    if board[y-1][x-1] != '○':
        return False
    else:
        for i in range(gap):
            if board[y-i-1][x-i-1] == '●':
                return True
                break
            elif board[y-i-1][x-i-1] == '-':
                return False
            else:
                continue


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


# 黒石のY座標入力
def by_input():
    black_y = input('Y座標を入力してください: ')
    if black_y in ('0', '1', '2', '3', '4', '5', '6', '7'):
        return black_y
    else:
        print('座標は0-7で入力してください')
        return by_input()


# 黒石のX座標入力
def bx_input():
    black_x = input('X座標を入力してください: ')
    if black_x in ('0', '1', '2', '3', '4', '5', '6', '7'):
        return black_x
    else:
        print('座標は0-7で入力してください')
        return bx_input()


# 白石のY座標入力
def wy_input():
    white_y = input('Y座標を入力してください')
    if white_y in ('0', '1', '2', '3', '4', '5', '6', '7'):
        return white_y
    else:
        print('座標は0-7で入力してください')
        return wy_input


# 白石のX座標入力
def wx_input():
    white_x = input('Y座標を入力してください')
    if white_x in ('0', '1', '2', '3', '4', '5', '6', '7'):
        return white_x
    else:
        print('座標は0-7で入力してください')
        return wx_input()


# 入力座標が空きマスか判定
def judge_vacant(board, y, x):
    if board[y][x] != '-':
        return False
    else:
        return True


# 白石を黒石に反転
def white_to_black(board, y, x):
    if board[y-1][x] == '●':                    # 上の反転
        for i in range(x):
            if board[y-i-1][x] == '●':
                board[y-i-1][x] = '○'
            else:                               # '○'に到達
                break
    elif board[y-1][x+1] == '●':                # 右上の反転
        for i in range(y):
            if board[y-i-1][x+i+1] == '●':
                board[y-i-1][x+i+1] = '○'
            else:
                break
    elif board[y][x+1] == '●':                  # 右の反転
        for i in range(7-x):
            if board[y][x+i+1] == '●':
                board[y][x+i+1] = '○'
            else:
                break
    elif board[y+1][x+1] == '●':                # 右下の反転
        for i in range(7-x):
            if board[y+i+1][x+i+1] == '●':
                board[y+i+1][x+i+1] = '○'
            else:
                break
    elif board[y+1][x] == '●':                  # 下の反転
        for i in range(7-y):
            if board[y+i+1][x] == '●':
                board[y+i+1][x] = '○'
            else:
                break
    elif board[y+1][x-1] == '●':                # 左下の反転
        for i in range(x):
            if board[y+i+1][x-i-1] == '●':
                board[y+i+1][x-i-1] = '○'
            else:
                break
    elif board[y][x-1] == '●':                  # 左の反転
        for i in range(x):
            if board[y][x-i-1] == '●':
                board[y][x-i-1] = '○'
            else:
                break
    elif board[y-1][x-1] == '●':                # 左上の反転
        for i in range(y):
            if board[y-i-1][x-i-1] == '●':
                board[y-i-1][x-i-1] = '○'
            else:
                break
    else:
        print('何かが起きている')


# 黒石を白石に反転
def black_to_white(board, y, x):
    if board[y-1][x] == '○':                    # 上の反転
        for i in range(x):
            if board[y-i-1][x] == '○':
                board[y-i-1][x] = '●'
            else:                               # '○'に到達
                break
    elif board[y-1][x+1] == '○':                # 右上の反転
        for i in range(y):
            if board[y-i-1][x+i+1] == '○':
                board[y-i-1][x+i+1] = '●'
            else:
                break
    elif board[y][x+1] == '○':                  # 右の反転
        for i in range(7-x):
            if board[y][x+i+1] == '○':
                board[y][x+i+1] = '●'
            else:
                break
    elif board[y+1][x+1] == '○':                # 右下の反転
        for i in range(7-x):
            if board[y+i+1][x+i+1] == '○':
                board[y+i+1][x+i+1] = '●'
            else:
                break
    elif board[y+1][x] == '○':                  # 下の反転
        for i in range(7-y):
            if board[y+i+1][x] == '○':
                board[y+i+1][x] = '●'
            else:
                break
    elif board[y+1][x-1] == '○':                # 左下の反転
        for i in range(x):
            if board[y+i+1][x-i-1] == '○':
                board[y+i+1][x-i-1] = '●'
            else:
                break
    elif board[y][x-1] == '○':                  # 左の反転
        for i in range(x):
            if board[y][x-i-1] == '○':
                board[y][x-i-1] = '●'
            else:
                break
    elif board[y-1][x-1] == '○':                # 左上の反転
        for i in range(y):
            if board[y-i-1][x-i-1] == '○':
                board[y-i-1][x-i-1] = '●'
            else:
                break
    else:
        print('何かが起きている')


def main():
    board_rc = []
    for _ in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    initial_position(board=board_rc)
    print("Turn: Black")
    by = int(by_input())
    bx = int(bx_input())
    if judge_vacant(board=board_rc, y=by, x=bx) is True:
        if black_upper(board=board_rc, y=by, x=bx) or\
              black_upper_right(board=board_rc, y=by, x=bx) or\
              black_right(board=board_rc, y=by, x=bx) or\
              black_lower_right(board=board_rc, y=by, x=bx) or\
              black_lower(board=board_rc, y=by, x=bx) or\
              black_lower_left(board=board_rc, y=by, x=bx) or\
              black_left(board=board_rc, y=by, x=bx) or\
              black_upper_left(board=board_rc, y=by, x=bx) is True:
            black(board=board_rc, y=by, x=bx)
        else:
            print('置けません')
    else:
        print('空いていません')
    white_to_black(board=board_rc, y=by, x=bx)
    show_board(board=board_rc)
    print('Turn: White')
    wy = int(wy_input())
    wx = int(wy_input())
    if judge_vacant(board=board_rc, y=wy, x=wx) is True:
        if white_upper(board=board_rc, y=wy, x=wx) or\
              white_upper_right(board_rc, wy, wx) or\
              white_right(board_rc, wy, wx) or\
              white_lower_right(board_rc, wy, wx) or\
              white_lower(board_rc, wy, wx) or\
              white_lower_left(board_rc, wy, wx) or\
              white_left(board_rc, wy, wx) or\
              white_upper_left(board_rc, wy, wx) is True:
            white(board=board_rc, y=wy, x=wx)
        else:
            print('置けません')
    else:
        print('空いていません')
    black_to_white(board=board_rc, y=wy, x=wx)
    show_board(board=board_rc)


if __name__ == '__main__':
    main()
