import random

# 座標が空きマスか判定
def judge_vacant(board, y, x):
    if board[y][x] != '-':
        return False
    else:
        return True


# 白石の置き位置を判定し、Trueなら敵の選択肢に追加
def enemy_place(board, x, y):
    if white_upper(board, y, x) or\
       white_upper_right(board, y, x) or\
       white_right(board, y, x) or\
       white_lower_right(board, y, x) or\
       white_lower(board, y, x) or\
       white_lower_left(board, y, x) or\
       white_left(board, y, x) or\
       white_upper_left(board, y, x) is True:
        enemy_choices.append([x, y])


lis_1 = [i for i in range(8)]
lis_2 = [i for i in range(8)]
cordinate_lis = []
for j in lis_1:
    for k in lis_2:
        cordinate_lis.append([j, k])
        print(cordinate_lis)


enemy_choices = []
for cordinate in cordinate_lis:
    yc = cordinate[1]
    xc = cordinate[0]
    if judge_vacant(board_rc, yc, xc) is True:
        enemy_place(board_rc, yc, xc)

enemy_choice = random.choice(enemy_choices)
ey = enemy_choice[1]
ex = enemy_choice[0]

white(board_rc_ ey, ex)