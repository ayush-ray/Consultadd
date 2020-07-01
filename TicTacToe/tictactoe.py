from board import print_board
from board import testing_board

def tictactoe():
    print("-------------------------------------------------------------------------------------")
    print("---------------------------Welcome to the TIC-TAC-TOE Game---------------------------")
    print("-------------------------------------------------------------------------------------")

    board_dict = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

    print("\nBoard\n")
    print_board(board_dict)
    print("\nPlease enter positions to select your mark. \n"
          "Player 1 is X\n"
          "Player 2 is O")

    board_dict = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

    print("\nCurrent Board")
    print_board(board_dict)

    for i in range(9):
        print(board_dict)
        player = (i % 2) + 1
        print("Player ", player, " turn(Enter position to mark): ")
        position = input()
        while board_dict[position] != ' ':
            position = input("Position already taken. Please select another position")

        if player == 1:
            board_dict[position] = 'X'
        else:
            board_dict[position] = 'O'

        print("\nCurrent Board")
        print_board(board_dict)
        if testing_board(board_dict):
            print("Player ", player, " wins")
            return

    print("\nNobody Wins :(\n")
    print("-------------------------------------------------------------------------------------")
    print("-------------------------------------Good Bye----------------------------------------")
    print("-------------------------------------------------------------------------------------")

if __name__ == '__main__':
    tictactoe()
