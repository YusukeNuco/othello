# '置けません'ではなく、True か　False の判定をとったほうがいいかも
# 右端までずっと白が続いた場合(ずっとcontinueの場合）どうなる？

# 上探索
def black_upper(board, y, x):
    gap = y
    if board[y-1][x] != '●':
        print('置けません')
    else:
        for i in range(gap):
            if board[y-i-i][x] == '○':
                black(board=board_rc, y=by, x=bx)
                break
            elif board[y-i-1][x] == '-':
                print('置けません')
            else:
                continue


def white_upper(board, y, x):
    gap = y
    if board[y-1][x] != '○':
        print('置けません')
    else:
        for i in range(gap):
            if board[y-i-1][x] == '●':
                white(board=board_rc, y=wy, x=wx)
                break
            elif board[y-i-1][x] == '-':
                print('置けません')
            else:
                continue


# 右上探索
def black_upper_right(board, y, x):
    gap = y
    if board[y-1][x+1] != '●':
        print('置けません')
    else:
        for i in range(gap):
            if board[y-i-1][x+i+1] == '○':
                black(board=board_rc, y=by, x=bx)
                break
            elif board[y-i-1][x+i+1] == '-':
                print('置けません')
            else:
                continue


def white_upper_right(board, y, x):
    gap = y
    if board[y-1][x+1] != '○':
        print('置けません')
    else:
        for i in range(gap):
            if board[y-i-1][x+i+1] == '●':
                white(board=board_rc, y=wy, x=wx)
                break
            elif board[y-i-1][x+i+1] == '-':
                print('置けません')
            else:
                continue


# 右探索
def black_right(board, y, x):
    gap = 7-x                                           # X座標と右端との差分を gap に格納
    if board[y][x+1] != '●':                            # 右が白石じゃないなら置けない。
        print('置けません')
    else:                                               # 右が白石だったら
        for i in range(gap):                            # 白石より右にある黒石を、差分の数だけ探索していく
            if board[y][x+i+1] == '○':                  # 白石より右側に黒石を見つけたら
                black(board=board_rc, y=by, x=bx)       # 入力した座標に石を置く。
                break                                   # 置いた時点で右への探索を切り上げる。
            elif board[y][x+i+1] == '-':                # 白石より右側に何もなかった場合、置けない。
                print('置けません')
            else:
                continue                                # '○' でも '-' でもない = 白石だった場合何もしない。


def white_right(board, y, x):
    gap = 7-x
    if board[y][x+1] != '○':
        print('置けません')
    else:
        for i in range(gap):
            if board[y][y+i*1] == '●':
                white(board=board_rc, y=wy, x=wx)
                break
            elif board[y][x+i+1] == '-':
                print('置けません')
            else:
                continue


# 右下探索
def black_lower_right(board, y, x):
    gap = 7-x
    if board[y+1][x+1] != '●':
        print('置けません')
    else:
        for i in range(gap):
            if board[y+i+1][x+i+1] == '○':
                black(board=board_rc, y=by, x=bx)
                break
            elif board[y+i+1][x+i+1] == '-':
                print('置けません')
            else:
                continue


def white_lower_right(board, y, x):
    gap = 7-x
    if board[y+1][x+1] != '○':
        print('置けません')
    else:
        for i in range(gap):
            if board[y+i+1][x+i+1] == '●':
                white(board=board_rc, y=wy, x=wx)
                break
            elif board[y+i+1][x+i+1] == '-':
                print('置けません')
            else:
                continue


# 下探索
def black_lower(board, y, x):
    gap = 7-y
    if board[y+1][x] != '●':
        print('置けません')
    else:
        for i in range(gap):
            if board[y+i+1][x] == '○':
                black(board=board_rc, y=by, x=bx)
                break
            elif board[y+i+1][x] == '-':
                print('置けません')
            else:
                continue


def white_lower(board, y, x):
    gap = 7-y
    if board[y+1][x] != '○':
        print('置けません')
    else:
        for i in range(gap):
            if board[y+i+1][x] == '●':
                white(board=board_rc, y=wy, x=wx)
                break
            elif board[y+i+1][x] == '-':
                print('置けません')
            else:
                continue


# 左下探索
def black_lower_left(board, y, x):
    gap = x
    if board[y+1][x-1] != '●':
        print('置けません')
    else:
        for i in range(gap):
            if board[y+i+1][x-i-1] == '○':
                black(board=board_rc, y=by, x=bx)
                break
            elif board[y+i+1][x-i-1] == '-':
                print('置けません')
            else:
                continue


def white_lower_left(board, y, x):
    gap = x
    if board[y+1][x-1] != '○':
        print('置けません')
    else:
        for i in range(gap):
            if board[y+i+1][x-i-1] == '●':
                white(board=board_rc, y=wy, x=wx)
                break
            elif board[y+i+1][x-i-1] == '-':
                print('置けません')
            else:
                continue


# 左探索
def black_left(board, y, x):
    gap = x
    if board[y][x-1] != '●':
        print('置けません')
    else:
        for i in range(gap):
            if board[y][x-i-1] == '○':
                black(board=board_rc, y=by, x=bx)
                break
            elif board[y][x-i-1] == '-':
                print('置けません')
            else:
                continue


def white_left(board, y, x):
    gap = x
    if board[y][x-1] != '○':
        print('置けません')
    else:
        for i in range(gap):
            if board[y][x-i-1] == '●':
                white(board=board_rc, y=wy, x=wx)
                break
            elif board[y][x-i-1] == '-':
                print('置けません')
            else:
                continue


# 左上探索
def black_upper_left(board, y, x):
    gap = x
    if board[y-1][x-1] != '●':
        print('置けません')
    else:
        for i in range(gap):
            if board[y-i-1][x-i-1] == '○':
                black(board=board_rc, y=by, x=bx)
                break
            elif board[y-i-1][x-i-1] == '-':
                print('置けません')
            else:
                continue


def white_upper_left(board, y, x):
    gap = x
    if board[y-1][x-1] != '○':
        print('置けません')
    else:
        for i in range(gap):
            if board[y-i-1][x-i-1] == '●':
                white(board=board_rc, y=wy, x=wx)
                break
            elif board[y-i-1][x-i-1] == '-':
                print('置けません')
            else:
                continue
