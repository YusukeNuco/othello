import board_2
import input_cordinate
import judge_black_position
import judge_white_position
import place
import to_black
import to_white
import vs_com_function


import random


def main():
    board_rc = []
    for i in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    board_2.initial_position(board_rc)
    while not board_2.is_full(board_rc):
        print('Your Turn')
        board_2.show_board(board_rc)
        board_2.show_board(board_rc)
        by = int(input_cordinate.by_input())
        bx = int(input_cordinate.bx_input())
        if judge_black_position.judge_vacant(board_rc, by, bx):
            place.black_place(board_rc, by, bx)
            to_black.to_black(board_rc, by, bx)
        else:
            print('空いていません')
        board_2.show_board(board_rc)
        print('Enemy Turn')
        vs_com_function.all_cordinates()
        vs_com_function.enemy_choices()
        enemy_choice = random.choice(enemy_choices())
        ey = enemy_choice[1]
        ex = enemy_choice[0]
        vs_com_function.enemy_place(board_rc, ey, ex)
        to_white.to_white(board_rc, ey, ex)
    else:
        board_2.judgement(board_rc)


if __name__ == '__main__':
    main()
