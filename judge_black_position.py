# 入力座標が空きマスか判定
def judge_vacant(board, y, x):
    if board[y][x] != '-':
        return False
    else:
        return True


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


# 右探索
def black_right(board, y, x):
    gap = 7-x
    if board[y][x+1] != '●':
        return False
    else:
        for i in range(gap):
            if board[y][x+i+1] == '○':
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
