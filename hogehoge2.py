row_lis = [0, 1, 2]
board_rc = []
for i in row_lis:
    board_rc.append(row_lis)

print(*board_rc, sep='\n')
print('\n'.join(map(str, board_rc)))

# row_lis_2 = ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ' ]
# board_rc_2 = []
# for j in row_lis_2:
#     board_rc_2.append(row_lis_2)
# print('\n'.join(board_rc_2))


# for j in row_lis:
#     print(j)

# for k in row_lis:
#     print(row_lis)

print(type('- '))
