def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def testing_board(board):
    testing_list = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for item in testing_list:
        if board[str(item[0])] != ' ' and board[str(item[0])] == board[str(item[1])] == board[str(item[2])]:
            return True

    return False
