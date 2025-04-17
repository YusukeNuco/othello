row_lis = [0, 1, 2]

for j in row_lis:
    print(j)

for k in row_lis:
    print(row_lis)



for i in range(1, 8):
    print(i)


# まず、おける位置かどうか判定する('-'なら置ける, True) ← この判定ができる関数は、ほぼできてる

# 置けるなら、その座標の八方を順番に探索していく
# 例えば、右、右下、下、左下、左、左上、上、右上といった順番に

# 黒石の場合の例
# 右が黒石の場合 → 探索終了 → 右下の探索へ
# 右下が白石の場合 → さらに右下を探索 → ...
#  → 最後の石が黒石だった → 置ける判定 → 探索終了 → 下の探索へ
#  → 最後の石が白石だった →　探索終了 → 下の探索へ
#  → 右端に到達 → 探索終了 → 下の探索へ

# 八方のいずれかに置ける判定があると、置ける

# 八方の表し方は？
# 入力したXY座標に数値を足し引きしていくしかないか？
# 右隣:[y][x+1]

# 足し引きしていった際に座標の数値が0-7以外になったら？
# 



def black_right():
    # 右の探索
    if board[y][x+1] == '●':    # 白だった場合
        if board[y][x+2] == '●':    # 白だった場合
            if board[y][x+3] == '●':    # 白だった場合
    
    else:
        print('置けません')
    

# 終わらないし、いずれ x が 8 になる
# + の部分をforでループできるか


def black_right():
    for i in range(1, 8):
        # 右の探索
        if board[y][x+i] == '●':
            if board[y][x+i+1] == '●':  # 何も変わってなくね？


# while でいけるか？ 例えば [x+i] == 8 とかで break とか


def black_right():
    # 右の探索
    while board[y][x+1] == '●':
        for i in range(1, 7):

    if [x+i] == 8:
        break   # '○'が見つからないまま右端に到達したから break 探索を切り上げる


# '○'を見つけた場合の break も必要か


def black_right(board, y, x):
    for i in range(1, 8):
        # 右の探索
        if board[y][x+i] != board[y][8]: # 右が少なくとも右端ではないなら
            if board[y][x+i] != '●':    # 右が白石ではないなら('-' or '○' なら)
                print('置けません')
            else:   # 右が白石だったらどうしたい → i を次の値に進めたい
                pass    # 本当か？
        else:
            print('置けません')




# [x]と 7 の差分だけ右側を探索
# 白を見つけたら、黒があるか探索

def black_right(board, y, x):
    for i in range([7-x]):  # X座標と右端との差分を獲得し i に入れていく
        if board[y][x+i] == '●':    # 右が白石なら

        
        else:
            print('置けません')


def black_right(board, y, x):
    gap = 7-x   # X座標と右端との差分を獲得
    if board[y][x+1] == '●':    # 右が白石なら
        for i in range(gap+1):  # 差分をiに入れていく
            if board[y][x+i] == '○':    # 右側に黒石があるなら  +0から始まるので注意
                black(board=board_rc, y=by, x=bx)   # 石を置く
                # 石を置いたからここで探索を終了したい
            else:
                pass
                

                
    else:
        print('置けません')


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
