import board_2
import input_cordinate
import judge_black_position
import judge_white_position
import place
import to_black
import to_white


def main():
    board_rc = []
    for _ in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    board_2.initial_position(board_rc)
    while not board_2.is_full(board_rc):
        print("Turn: Black")
        board_2.show_board(board_rc)
        by = int(input_cordinate.by_input())
        bx = int(input_cordinate.bx_input())
        if judge_black_position.judge_vacant(board=board_rc, y=by, x=bx):
            place.black_place(board=board_rc, y=by, x=bx)
            to_black.to_black(board=board_rc, y=by, x=bx)
        else:
            print('空いていません')
        board_2.show_board(board_rc)
        print('Turn: White')
        wy = int(input_cordinate.wy_input())
        wx = int(input_cordinate.wx_input())
        if judge_white_position.judge_vacant(board_rc, wy, wx):
            place.white_place(board_rc, wy, wx)
            to_white.to_white(board_rc, wy, wx)
        else:
            print('空いていません')
        board_2.show_board(board_rc)
    else:
        board_2.judgement(board=board_rc)


if __name__ == '__main__':
    main()
