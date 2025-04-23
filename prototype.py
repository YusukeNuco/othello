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
    white_x = input('X座標を入力してください')
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


# 上反転
def upper_to_black(board, y, x):
    if board[y-1][x] == '●':
        for i in range(y):
            if board[y-i-1][x] == '○':
                u_to_black(board, y, x)
            else:
                pass


def u_to_black(board, y, x):
    for i in range(y):
        if board[y-i-1][x] == '●':
            board[y-i-1][x] = '○'
        else:
            break


def upper_to_white(board, y, x):
    if board[y-1][x] == '○':
        for i in range(y):
            if board[y-i-1][x] == '●':
                u_to_white(board, y, x)
            else:
                pass


def u_to_white(board, y, x):
    for i in range(y):
        if board[y-i-1][x] == '○':
            board[y-i-1][x] = '●'
        else:
            break


# 右上反転
def upper_right_to_black(board, y, x):
    if board[y-1][x+1] == '●':
        if 6 <= x:
            pass
        elif x == 5:
            for i in range(2):
                if board[y-i-1][x+i+1] == '○':
                    ur_to_black(board, y, x)
                else:
                    pass
        elif x == 4:
            if y == 2:
                for i in range(2):
                    if board[y-i-1][x+i+1] == '○':
                        ur_to_black(board, y, x)
            elif 5 <= y:
                for i in range(3):
                    if board[y-i-1][x+i+1] == '○':
                        ur_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 3:
            if y == 2:
                for i in range(2):
                    if board[y-i-1][x+i+1] == '○':
                        ur_to_black(board, y, x)
                    else:
                        pass
            elif 5 <= y:
                for i in range(4):
                    if board[y-i-1][x+i+1] == '○':
                        ur_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 2:
            if 6 <= y:
                for i in range(5):
                    if board[y-i-1][x+i+1] == '○':
                        ur_to_black(board, y, x)
                    else:
                        pass
            elif 2 <= y <= 5:
                for i in range(y):
                    if board[y-i-1][x+i+1] == '○':
                        ur_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 1:
            if 2 <= y <= 6:
                for i in range(y):
                    if board[y-i-1][x+i+1] == '○':
                        ur_to_black(board, y, x)
                    else:
                        pass
            elif y == 7:
                for i in range(6):
                    if board[y-i-1][x+i+1] == '○':
                        ur_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 0:
            if 2 <= y:
                for i in range(y):
                    if board[y-i-1][x+i+1] == '○':
                        ur_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
    else:
        pass


def ur_to_black(board, y, x):
    for i in range(7-x):
        if board[y-i-1][x+i+1] == '●':
            board[y-i-1][x+i+1] = '○'
        else:
            break


def upper_right_to_white(board, y, x):
    if board[y-1][x+1] == '○':
        if 6 <= x:
            pass
        elif x == 5:
            for i in range(2):
                if board[y-i-1][x+i+1] == '●':
                    ur_to_white(board, y, x)
                else:
                    pass
        elif x == 4:
            if y == 2:
                for i in range(2):
                    if board[y-i-1][x+i+1] == '●':
                        ur_to_white(board, y, x)
            elif 5 <= y:
                for i in range(3):
                    if board[y-i-1][x+i+1] == '●':
                        ur_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 3:
            if y == 2:
                for i in range(2):
                    if board[y-i-1][x+i+1] == '●':
                        ur_to_white(board, y, x)
                    else:
                        pass
            elif 5 <= y:
                for i in range(4):
                    if board[y-i-1][x+i+1] == '●':
                        ur_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 2:
            if 6 <= y:
                for i in range(5):
                    if board[y-i-1][x+i+1] == '●':
                        ur_to_white(board, y, x)
                    else:
                        pass
            elif 2 <= y <= 5:
                for i in range(y):
                    if board[y-i-1][x+i+1] == '●':
                        ur_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 1:
            if 2 <= y <= 6:
                for i in range(y):
                    if board[y-i-1][x+i+1] == '●':
                        ur_to_white(board, y, x)
                    else:
                        pass
            elif y == 7:
                for i in range(6):
                    if board[y-i-1][x+i+1] == '●':
                        ur_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 0:
            if 2 <= y:
                for i in range(y):
                    if board[y-i-1][x+i+1] == '●':
                        ur_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
    else:
        pass


def ur_to_white(board, y, x):
    for i in range(7-x):
        if board[y-i-1][x+i+1] == '○':
            board[y-i-1][x+i+1] = '●'
        else:
            break


# 右反転
def right_to_black(board, y, x):
    if board[y][x+1] == '●':
        for i in range(7-x):
            if board[y][x+i+1] == '○':
                r_to_black(board, y, x)
            else:
                pass


def r_to_black(board, y, x):
    for i in range(7-x):
        if board[y][x+i+1] == '●':
            board[y][x+i+1] = '○'
        else:
            break


def right_to_white(board, y, x):
    if board[y][x+1] == '○':
        for i in range(7-x):
            if board[y][x+i+1] == '●':
                r_to_white(board, y, x)
            else:
                pass


def r_to_white(board, y, x):
    for i in range(7-x):
        if board[y][x+i+1] == '○':
            board[y][x+i+1] = '●'
        else:
            break


# 右下反転
def lower_right_to_black(board, y, x):
    if board[y+1][x+1] == '●':
        if 6 <= x:
            pass
        elif x == 5:
            for i in range(2):
                if board[y+i+1][x+i+1] == '○':
                    lr_to_black(board, y, x)
                else:
                    pass
        elif x == 4:
            if y == 5:
                for i in range(2):
                    if board[y+i+1][x+i+1] == '○':
                        lr_to_black(board, y, x)
            elif y <= 2:
                for i in range(3):
                    if board[y+i+1][x+i+1] == '○':
                        lr_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 3:
            if y == 5:
                for i in range(2):
                    if board[y+i+1][x+i+1] == '○':
                        lr_to_black(board, y, x)
                    else:
                        pass
            elif y <= 2:
                for i in range(4):
                    if board[y+i+1][x+i+1] == '○':
                        lr_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 2:
            if y < 2:
                for i in range(5):
                    if board[y+i+1][x+i+1] == '○':
                        lr_to_black(board, y, x)
                    else:
                        pass
            elif 2 <= y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x+i+1] == '○':
                        lr_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 1:
            if 1 <= y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x+i+1] == '○':
                        lr_to_black(board, y, x)
                    else:
                        pass
            elif y == 0:
                for i in range(6):
                    if board[y+i+1][x+i+1] == '○':
                        lr_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 0:
            if y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x+i+1] == '○':
                        lr_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
    else:
        pass


def lr_to_black(board, y, x):
    for i in range(7-x):
        if board[y+i+1][x+i+1] == '●':
            board[y+i+1][x+i+1] = '○'
        else:
            break


def lower_right_to_white(board, y, x):
    if board[y+1][x+1] == '○':
        if 6 <= x:
            pass
        elif x == 5:
            for i in range(2):
                if board[y+i+1][x+i+1] == '●':
                    lr_to_white(board, y, x)
                else:
                    pass
        elif x == 4:
            if y == 5:
                for i in range(2):
                    if board[y+i+1][x+i+1] == '●':
                        lr_to_white(board, y, x)
            elif y <= 2:
                for i in range(3):
                    if board[y+i+1][x+i+1] == '●':
                        lr_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 3:
            if y == 5:
                for i in range(2):
                    if board[y+i+1][x+i+1] == '●':
                        lr_to_white(board, y, x)
                    else:
                        pass
            elif y <= 2:
                for i in range(4):
                    if board[y+i+1][x+i+1] == '●':
                        lr_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 2:
            if y < 2:
                for i in range(5):
                    if board[y+i+1][x+i+1] == '●':
                        lr_to_white(board, y, x)
                    else:
                        pass
            elif 2 <= y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x+i+1] == '●':
                        lr_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 1:
            if 1 <= y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x+i+1] == '●':
                        lr_to_white(board, y, x)
                    else:
                        pass
            elif y == 0:
                for i in range(6):
                    if board[y+i+1][x+i+1] == '●':
                        lr_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 0:
            if y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x+i+1] == '●':
                        lr_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
    else:
        pass


def lr_to_white(board, y, x):
    for i in range(7-x):
        if board[y+i+1][x+i+1] == '○':
            board[y+i+1][x+i+1] = '●'
        else:
            break


# 下反転
def lower_to_black(board, y, x):
    if board[y+1][x] == '●':
        for i in range(7-y):
            if board[y+i+1][x] == '○':
                l_to_black(board, y, x)
            else:
                pass


def l_to_black(board, y, x):
    for i in range(7-y):
        if board[y+i+1][x] == '●':
            board[y+i+1][x] = '○'
        else:
            break


def lower_to_white(board, y, x):
    if board[y+1][x] == '○':
        for i in range(7-y):
            if board[y+i+1][x] == '●':
                l_to_white(board, y, x)
            else:
                pass


def l_to_white(board, y, x):
    for i in range(7-y):
        if board[y+i+1][x] == '○':
            board[y+i+1][x] = '●'
        else:
            break


# 左下反転
def lower_left_to_black(board, y, x):
    if board[y+1][x-1] == '●':
        if x <= 1:
            pass
        elif x == 2:
            for i in range(2):
                if board[y+i+1][x-i-1] == '○':
                    ll_to_black(board, y, x)
                else:
                    pass
        elif x == 3:
            if y == 5:
                for i in range(2):
                    if board[y+i+1][x-i-1] == '○':
                        ll_to_black(board, y, x)
            elif y <= 2:
                for i in range(3):
                    if board[y+i+1][x-i-1] == '○':
                        ll_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 4:
            if y == 5:
                for i in range(2):
                    if board[y+i+1][x-i-1] == '○':
                        ll_to_black(board, y, x)
                    else:
                        pass
            elif y <= 2:
                for i in range(4):
                    if board[y+i+1][x-i-1] == '○':
                        ll_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 5:
            if y < 2:
                for i in range(5):
                    if board[y+i+1][x-i-1] == '○':
                        ll_to_black(board, y, x)
                    else:
                        pass
            elif 2 <= y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x-i-1] == '○':
                        ll_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 6:
            if 1 <= y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x-i-1] == '○':
                        ll_to_black(board, y, x)
                    else:
                        pass
            elif y == 0:
                for i in range(6):
                    if board[y+i+1][x-i-1] == '○':
                        ll_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 7:
            if y <= 5:
                for i in range(x-y):
                    if board[y+i+1][x-i-1] == '○':
                        ll_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
    else:
        pass


def ll_to_black(board, y, x):
    for i in range(x):
        if board[y+i+1][x-i-1] == '●':
            board[y+i+1][x-i-1] = '○'
        else:
            break


def lower_left_to_white(board, y, x):
    if board[y+1][x-1] == '○':
        if x <= 1:
            pass
        elif x == 2:
            for i in range(2):
                if board[y+i+1][x-i-1] == '●':
                    ll_to_white(board, y, x)
                else:
                    pass
        elif x == 3:
            if y == 5:
                for i in range(2):
                    if board[y+i+1][x-i-1] == '●':
                        ll_to_white(board, y, x)
            elif y <= 2:
                for i in range(3):
                    if board[y+i+1][x-i-1] == '●':
                        ll_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 4:
            if y == 5:
                for i in range(2):
                    if board[y+i+1][x-i-1] == '●':
                        ll_to_white(board, y, x)
                    else:
                        pass
            elif y <= 2:
                for i in range(4):
                    if board[y+i+1][x-i-1] == '●':
                        ll_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 5:
            if y < 2:
                for i in range(5):
                    if board[y+i+1][x-i-1] == '●':
                        ll_to_white(board, y, x)
                    else:
                        pass
            elif 2 <= y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x-i-1] == '●':
                        ll_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 6:
            if 1 <= y <= 5:
                for i in range(7-y):
                    if board[y+i+1][x-i-1] == '●':
                        ll_to_white(board, y, x)
                    else:
                        pass
            elif y == 0:
                for i in range(6):
                    if board[y+i+1][x-i-1] == '●':
                        ll_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 7:
            for i in range(x-y):
                if board[y+i+1][x-i-1] == '●':
                    ll_to_white(board, y, x)
                else:
                    pass
    else:
        pass


def ll_to_white(board, y, x):
    for i in range(x):
        if board[y+i+1][y-i-1] == '○':
            board[y+i+1][y-i-1] == '●'
        else:
            break


# 左反転
def left_to_black(board, y, x):
    if board[y][x-1] == '●':
        for i in range(x):
            if board[y][x-i-1] == '○':
                le_to_black(board, y, x)
            else:
                pass


def le_to_black(board, y, x):
    for i in range(x):
        if board[y][x-i-1] == '●':
            board[y][x-i-1] = '○'
        else:
            break


def left_to_white(board, y, x):
    if board[y][x-1] == '○':
        for i in range(x):
            if board[y][x-i-1] == '●':
                le_to_white(board, y, x)
            else:
                pass


def le_to_white(board, y, x):
    for i in range(x):
        if board[y][x-i-1] == '○':
            board[y][x-i-1] = '●'
        else:
            break


# 左上反転
def upper_left_to_black(board, y, x):
    if board[y-1][x-1] == '●':
        if x <= 1:
            pass
        elif x == 2:
            for i in range(2):
                if board[y-i-1][x-i-1] == '○':
                    ul_to_black(board, y, x)
                else:
                    pass
        elif x == 3:
            if y == 2:
                for i in range(2):
                    if board[y-i-1][x-i-1] == '○':
                        ul_to_black(board, y, x)
            elif 5 <= y:
                for i in range(3):
                    if board[y-i-1][x-i-1] == '○':
                        ul_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 4:
            if y == 2:
                for i in range(2):
                    if board[y-i-1][x-i-1] == '○':
                        ul_to_black(board, y, x)
                    else:
                        pass
            elif 5 <= y:
                for i in range(4):
                    if board[y-i-1][x-i-1] == '○':
                        ul_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 5:
            if 6 <= y:
                for i in range(5):
                    if board[y-i-1][x-i-1] == '○':
                        ul_to_black(board, y, x)
                    else:
                        pass
            elif 2 <= y <= 5:
                for i in range(y):
                    if board[y-i-1][x-i-1] == '○':
                        ul_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 6:
            if 2 <= y <= 6:
                for i in range(y):
                    if board[y-i-1][x-i-1] == '○':
                        ul_to_black(board, y, x)
                    else:
                        pass
            elif y == 7:
                for i in range(6):
                    if board[y-i-1][x-i-1] == '○':
                        ul_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 7:
            if 2 <= y:
                for i in range(y):
                    if board[y-i-1][x-i-1] == '○':
                        ul_to_black(board, y, x)
                    else:
                        pass
            else:
                pass
    else:
        pass


def ul_to_black(board, y, x):
    for i in range(x):
        if board[y-i-1][x-i-1] == '●':
            board[y-i-1][x-i-1] = '○'
        else:
            break


def upper_left_to_white(board, y, x):
    if board[y-1][x-1] == '○':
        if x <= 1:
            pass
        elif x == 2:
            for i in range(2):
                if board[y-i-1][x-i-1] == '●':
                    ul_to_white(board, y, x)
                else:
                    pass
        elif x == 3:
            if y == 2:
                for i in range(2):
                    if board[y-i-1][x-i-1] == '●':
                        ul_to_white(board, y, x)
            elif 5 <= y:
                for i in range(3):
                    if board[y-i-1][x-i-1] == '●':
                        ul_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 4:
            if y == 2:
                for i in range(2):
                    if board[y-i-1][x-i-1] == '●':
                        ul_to_white(board, y, x)
                    else:
                        pass
            elif 5 <= y:
                for i in range(4):
                    if board[y-i-1][x-i-1] == '●':
                        ul_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 5:
            if 6 <= y:
                for i in range(5):
                    if board[y-i-1][x-i-1] == '●':
                        ul_to_white(board, y, x)
                    else:
                        pass
            elif 2 <= y <= 5:
                for i in range(y):
                    if board[y-i-1][x-i-1] == '●':
                        ul_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 6:
            if 2 <= y <= 6:
                for i in range(y):
                    if board[y-i-1][x-i-1] == '●':
                        ul_to_white(board, y, x)
                    else:
                        pass
            elif y == 7:
                for i in range(6):
                    if board[y-i-1][x-i-1] == '●':
                        ul_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
        elif x == 7:
            if 2 <= y:
                for i in range(y):
                    if board[y-i-1][x-i-1] == '●':
                        ul_to_white(board, y, x)
                    else:
                        pass
            else:
                pass
    else:
        pass


def ul_to_white(board, y, x):
    for i in range(x):
        if board[y-i-1][x-i-1] == '○':
            board[y-i-1][x-i-1] = '●'
        else:
            break


# 入力座標に対する黒石の置き位置を判定し、Trueなら置く
def black_place(board, x, y):
    if black_upper(board, y, x) or\
       black_upper_right(board, y, x) or\
       black_right(board, y, x) or\
       black_lower_right(board, y, x) or\
       black_lower(board, y, x) or\
       black_lower_left(board, y, x) or\
       black_left(board, y, x) or\
       black_upper_left(board, y, x) is True:
        black(board, y, x)
    else:
        print('置けません')


# 入力座標に対する白石の置き位置を判定し、Trueなら置く
def white_place(board, y, x):
    if white_upper(board, y, x) or\
       white_upper_right(board, y, x) or\
       white_right(board, y, x) or\
       white_lower_right(board, y, x) or\
       white_lower(board, y, x) or\
       white_lower_left(board, y, x) or\
       white_left(board, y, x) or\
       white_upper_left(board, y, x) is True:
        white(board, y, x)
    else:
        print('置けません')


# 白石を黒石に反転
def to_black(board, y, x):
    upper_to_black(board, y, x)
    upper_right_to_black(board, y, x)
    right_to_black(board, y, x)
    lower_right_to_black(board, y, x)
    lower_to_black(board, y, x)
    lower_left_to_black(board, y, x)
    left_to_black(board, y, x)
    upper_left_to_black(board, y, x)


# 黒石を白石に反転
def to_white(board, y, x):
    upper_to_white(board, y, x)
    upper_right_to_white(board, y, x)
    right_to_white(board, y, x)
    lower_right_to_white(board, y, x)
    lower_to_white(board, y, x)
    lower_left_to_white(board, y, x)
    left_to_white(board, y, x)
    upper_left_to_white(board, y, x)


# 空きマスが残っているか判定(残っていたらFalse)
def is_full(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True


def main():
    board_rc = []
    for _ in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    initial_position(board_rc)
    while not is_full(board_rc):
        print("Turn: Black")
        show_board(board_rc)
        by = int(by_input())
        bx = int(bx_input())
        if judge_vacant(board=board_rc, y=by, x=bx):
            black_place(board=board_rc, y=by, x=bx)
            to_black(board=board_rc, y=by, x=bx)
        else:
            print('空いていません')
        show_board(board_rc)
        print('Turn: White')
        wy = int(wy_input())
        wx = int(wx_input())
        if judge_vacant(board_rc, wy, wx):
            white_place(board_rc, wy, wx)
            to_white(board_rc, wy, wx)
        else:
            print('空いていません')
        show_board(board_rc)
    else:
        judgement(board=board_rc)


if __name__ == '__main__':
    main()
