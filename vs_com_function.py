import random
import judge_white_position


board_rc = []
for _ in range(8):
    board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])


# 座標が空きマスか判定
def judge_vacant(board, y, x):
    if board[y][x] != '-':
        return False
    else:
        return True


# 64の座標全てのリスト
def all_cordinates():
    lis_1 = [i for i in range(8)]
    lis_2 = [i for i in range(8)]
    cordinate_lis = []
    for j in lis_1:
        for k in lis_2:
            cordinate_lis.append([j, k])
    return cordinate_lis


# 全ての座標のうち、敵(白)が石を置ける座標のリスト == 敵の選択肢
def enemy_choices():
    enemy_choices = []
    for cordinate in all_cordinates():
        yc = cordinate[1]
        xc = cordinate[0]
        if judge_vacant(board_rc, yc, xc):
            if judge_white_position.white_upper(board_rc, yc, xc) or\
               judge_white_position.white_upper_right(board_rc, yc, xc) or\
               judge_white_position.white_right(board_rc, yc, xc) or\
               judge_white_position.white_lower_right(board_rc, yc, xc) or\
               judge_white_position.white_lower(board_rc, yc, xc) or\
               judge_white_position.white_lower_left(board_rc, yc, xc) or\
               judge_white_position.white_left(board_rc, yc, xc) or\
               judge_white_position.white_upper_left(board_rc, yc, xc) is True:
                enemy_choices.append([xc, yc])
    return enemy_choices


# 選択肢から無作為に座標を1つ抽出
enemy_choice = random.choice(enemy_choices())


# 敵が石を置く
def enemy_place(board, y, x):
    board[y][x] = '●'
