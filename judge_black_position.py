# 入力座標が空きマスか判定
def judge_vacant(board, y, x):
    if board[y][x] != '-':
        return False
    else:
        return True


# 上探索
def black_upper(board, y, x):
    if y != 0:
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
    else:
        pass


# 右上探索
def black_upper_right(board, y, x):
    if 1 < y and x < 6:
        if board[y-1][x+1] != '●':
            return False
        else:
            gap = y
            for i in range(gap):
                if board[y-i-1][x+i+1] == '○':
                    return True
                    break
                elif board[y-i-1][x+i+1] == '-':
                    return False
                else:
                    continue
    else:
        pass


# 右探索
def black_right(board, y, x):
    if x != 7:
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
    else:
        pass


# 右下探索
def black_lower_right(board, y, x):
    if y < 6 and x < 6:
        if board[y+1][x+1] != '●':
            return False
        else:
            if x == 5:
                for i in range(2):
                    if board[y+i+1][x+i+1] == '○':
                        return True
                        break
                    elif board[y+i+1][x+i+1] == '-':
                        return False
                    else:
                        continue
            elif x == 4:
                if y == 5:
                    for i in range(2):
                        if board[y+i+1][x+i+1] == '○':
                            return True
                            break
                        elif board[y+i+1][x+i+1] == '-':
                            return False
                        else:
                            continue
                elif y < 5:
                    for i in range(3):
                        if board[y+i+1][x+i+1] == '○':
                            return True
                            break
                        elif board[y+i+1][x+i+1] == '-':
                            return False
                        else:
                            continue
            elif x == 3:
                if y < 4:
                    for i in range(4):
                        if board[y+i+1][x+i+1] == '○':
                            return True
                            break
                        elif board[y+i+1][x+i+1] == '-':
                            return False
                        else:
                            continue
                elif 4 <= y:
                    for i in range(7-y):
                        if board[y+i+1][x+i+1] == '○':
                            return True
                            break
                        elif board[y+i+1][x+i+1] == '-':
                            return False
                        else:
                            continue
            elif x == 2:
                if y < 3:
                    for i in range(5):
                        if board[y+i+1][x+i+1] == '○':
                            return True
                            break
                        elif board[y+i+1][x+i+1] == '-':
                            return False
                        else:
                            continue
                if 3 <= y:
                    for i in range(7-y):
                        if board[y+i+1][x+i+1] == '○':
                            return True
                            break
                        elif board[y+i+1][x+i+1] == '-':
                            return False
                        else:
                            continue
            elif x == 1:
                if y < 2:
                    for i in range(6):
                        if board[y+i+1][x+i+1] == '○':
                            return True
                            break
                        elif board[y+i+1][x+i+1] == '-':
                            return False
                        else:
                            continue
                elif 2 <= y:
                    for i in range(7-y):
                        if board[y+i+1][x+i+1] == '○':
                            return True
                            break
                        elif board[y+i+1][x+i+1] == '-':
                            return False
                        else:
                            continue
            elif x == 0:
                for i in range(7-y):
                    if board[y+i+1][x+i+1] == '○':
                        return True
                        break
                    elif board[y+i+1][x+i+1] == '-':
                        return False
                    else:
                        continue
            else:
                pass
    else:
        pass


# 下探索
def black_lower(board, y, x):
    if y != 7:
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
    else:
        pass


# 左下探索
def black_lower_left(board, y, x):
    if y < 6 and 1 < x:
        if board[y+1][x-1] != '●':
            return False
        else:
            if x == 2:
                for i in range(2):
                    if board[y+i+1][x-i-1] == '○':
                        return True
                        break
                    elif board[y+i+1][x-i-1] == '-':
                        return False
                    else:
                        continue
            elif x == 3:
                if y == 5:
                    for i in range(2):
                        if board[y+i+1][x-i-1] == '○':
                            return True
                            break
                        elif board[y+i+1][x-i-1] == '-':
                            return False
                        else:
                            continue
                elif y < 5:
                    for i in range(3):
                        if board[y+i+1][x-i-1] == '○':
                            return True
                            break
                        elif board[y+i+1][x-i-1] == '-':
                            return False
                        else:
                            continue
            elif x == 4:
                if y < 4:
                    for i in range(4):
                        if board[y+i+1][x-i-1] == '○':
                            return True
                            break
                        elif board[y+i+1][x-i-1] == '-':
                            return False
                        else:
                            continue
                elif 4 <= y:
                    for i in range(7-y):
                        if board[y+i+1][x-i-1] == '○':
                            return True
                            break
                        elif board[y+i+1][x-i-1] == '-':
                            return False
                        else:
                            continue
            elif x == 5:
                if y < 3:
                    for i in range(5):
                        if board[y+i+1][x-i-1] == '○':
                            return True
                            break
                        elif board[y+i+1][x-i-1] == '-':
                            return False
                        else:
                            continue
                elif 3 <= y:
                    for i in range(7-y):
                        if board[y+i+1][x-i-1] == '○':
                            return True
                            break
                        elif board[y+i+1][x-i-1] == '-':
                            return False
                        else:
                            continue
            elif x == 6:
                if y == 0:
                    for i in range(6):
                        if board[y+i+1][x-i-1] == '○':
                            return True
                            break
                        elif board[y+i+1][x-i-1] == '-':
                            return False
                        else:
                            continue
                elif 0 < y:
                    for i in range(7-y):
                        if board[y+i+1][x-i-1] == '○':
                            return True
                            break
                        elif board[y+i+1][x-i-1] == '-':
                            return False
                        else:
                            continue
            elif x == 7:
                for i in range(7-y):
                    if board[y+i+1][x-i-1] == '○':
                        return True
                        break
                    elif board[y+i+1][x-i-1] == '-':
                        return False
                    else:
                        continue
            else:
                pass
    else:
        pass


# 左探索
def black_left(board, y, x):
    if x != 0:
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
    else:
        pass


# 左上探索
def black_upper_left(board, y, x):
    if 1 < y and 1 < x:
        if board[y-1][x-1] != '●':
            return False
        else:
            gap = x
            for i in range(gap):
                if board[y-i-1][x-i-1] == '○':
                    return True
                    break
                elif board[y-i-1][x-i-1] == '-':
                    return False
                else:
                    continue
    else:
        pass
