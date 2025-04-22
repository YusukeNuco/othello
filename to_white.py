# 上反転
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
            if y <= 5:
                for i in range(x-y):
                    if board[y+i+1][x-i-1] == '●':
                        ll_to_white(board, y, x)
                    else:
                        pass
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
