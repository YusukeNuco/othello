def main():
    y = int(input())
    x = int(input())
    row_lis = [0, 1, 2, 3, 4, 5, 6, 7,]
    board_rc = []
    for i in row_lis:
        board_rc.append(row_lis)
    print('\n'.join(map(str, board_rc)))
    # print(board_rc[0][1])
    # print(board_rc[1][0])
    # print(board_rc[0])
    # print(board_rc[1])
    print(board_rc[y][x])
    board_rc[y][x] = 'maru'
    print('\n'.join(map(str, board_rc)))

if __name__ == '__main__':
    main()
