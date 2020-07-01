import os
from read_csv import reading
from game_functionality import game_functionality


class InvalidCharException(Exception):
    pass


def authenticate_data():
    data_list = reading()
    for i in range(2):
        name = str(input("Enter Name: ")).strip()
        email = str(input("Enter Email: ")).strip()
        if [name, email] in data_list:
            print("-----------------------------------Credentials Matched--------------------------------------")
            break

        print("Invalid credentials")
        if i == 1:
            return
    ROOT_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    WELCOME_PATH = ROOT_DIR + r'\resources\welcome_note.txt'
    INSTRUCTIONS_PATH = ROOT_DIR + r'\resources\game_instruction.txt'
    f = open(WELCOME_PATH, 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    while True:
        choice = input("Do you want to enter the game?(Yes/No)")
        if choice == "Yes":
            break
        elif choice == "No":
            return
        else:
            print("Invalid Input")

    f = open(INSTRUCTIONS_PATH, 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

    while True:
        choice = input("Press P to Play: ")
        try:
            if choice == "P":
                break
        except InvalidCharException:
            pass
        print("Invalid Input")

    print("------------------------------------------GAME BEGINS-------------------------------------")
    rows = int(input("Enter rows for matrix: "))
    cols = int(input("Enter rows for matrix: "))
    matrix = []
    for i in range(rows):
        print("Enter ", str(cols), " values for row", str(i+1), " (0's and 1's only, comma separated and no spaces)")
        _str = input()
        _list = _str.split(',')
        _list2 = [int(i.strip()) for i in _list]
        if len(_list2) != cols:
            print("Invalid number of entries. Exiting")
            return
        if set(_list2) not in [{0, 1}, {0}, {1}]:
            print("Invalid entries! Only 0's and 1's are allowed. Exiting")
            return
        matrix.append(_list)
    temp = game_functionality(matrix)
    river_list = list(filter(lambda a: a != 0, temp))
    river_list.sort()
    user_list = []
    print("There are ", len(river_list), " rivers.\n")
    for i in range(len(river_list)):
        user_list.append(int(input("Guess the size of river: ")))
    user_list.sort()
    if river_list == user_list:
        print("You are the winner")
    else:
        matches = 0
        for i in range(len(user_list)):
            if user_list[i] in river_list:
                river_list.remove(user_list[i])
                matches += 1
        print(matches)
        ratio = matches / len(user_list)
        if ratio >= 0.6:
            print("You got second position.")
        else:
            print("Invest more money on Almonds, then come back.")

    choice = input("Do you want to play again?(Yes/No): ")
    if choice == "Yes":
        authenticate_data()
    else:
        return


if __name__ == "__main__":
    authenticate_data()