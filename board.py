def main():
    y = int(input())
    x = int(input())
    row_lis = ['-', '-', '-', '-', '-', '-', '-', '-',]
    board_rc = []
    for _ in range(8):
        board_rc.append(['-', '-', '-', '-', '-', '-', '-', '-',])
    board_rc[y][x] = '⚪️'
    print(*board_rc, sep = '\n')



if __name__ == '__main__':
    main()