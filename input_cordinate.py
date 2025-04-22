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