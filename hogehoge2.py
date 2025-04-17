if judge_vacant(board=board_rc, y=by, x=bx) is True:
        if black_upper(board=board_rc, y=by, x=bx) is True:
            black(board=board_rc, y=by, x=bx)
        elif black_upper_right(board_rc, y=by, x=bx) is True:
            black(board=board_rc, y=by, x=bx)
        elif black_right(board_rc, y=by, x=bx) is True:
            black(board=board_rc, y=by, x=bx)
        elif black_lower_right(board_rc, y=by, x=bx) is True:
            black(board=board_rc, y=by, x=bx)
        elif black_lower(board_rc, y=by, x=bx) is True:
            black(board=board_rc, y=by, x=bx)
        elif black_lower_left(board_rc, y=by, x=bx) is True:
            black(board=board_rc, y=by, x=bx)
        elif black_left(board_rc, y=by, x=bx) is True:
            black(board=board_rc, y=by, x=bx)
        elif black_upper_left(board_rc, y=by, x=bx) is True:
            black(board=board_rc, y=by, x=bx)
        else:
            print('置けません')
    else:
        print('空いていません')




row_lis = [0, 1, 2]

for j in row_lis:
    print(j)

for k in row_lis:
    print(row_lis)



for i in range(1, 8):
    print(i)




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






# 反転させる
# 石を置いた座標の八方向を探索する


def white_to_black(board, y, x):
    if board[y-1][x] == '●':                    # 上の反転
        gap = x
        for i in range(gap):
            if board[y-i-1][x] == '●':
                board[y-i-1][x] = '○'
            else:
                break