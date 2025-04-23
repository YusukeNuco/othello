import board


# 斜めの判定だけ gap を場合分けしないと IndexError になる。
# 誤った座標を入力した際に、もう一度入力できるようにする
# 各手番の終わりに勝敗判定をつける
# → まだ置ける位置がある場合、続行
# → 一方が置けない場合、相手の手番にスキップ(正式なルールでは２回スキップで負けらしい)
# → 盤面が埋まった or 両者が置けなくなった場合、石の数を数えて勝敗判定

# 探索も場合分けしないといけない。
# 座標に7を入れた時点で、IndexError: out of range になるため、7とそれ以外の入力で場合わけが必要

# 反転させる時の gap の取り方も改善しないといけないか。
# xとyの壁に近いほうと、壁との差分を探索。同値の場合はどっちでもいい。


def create_bord():
    board_rc = []
    for i in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-'])
    board.initial_position(board_rc)
    board.show_board(board_rc)


def create_board_2():
    row = []
    for i in range(8):
        row.append('-')
    board_rc_2 = []
    for i in range(8):
        board_rc_2.append(row)
    board.initial_position(board_rc_2)
    board.show_board(board_rc_2)


create_bord()
print('\t')
create_board_2()
