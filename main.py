import os
board = "---------\n1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n\
7 | 8 | 9\n---------"

counter = [i for i in range(9)]
choice_counter = []

winning_conditions = [
    # Rows
    [0, 1, 2],  # Top row
    [3, 4, 5],  # Middle row
    [6, 7, 8],  # Bottom row

    # Columns
    [0, 3, 6],  # Left column
    [1, 4, 7],  # Middle column
    [2, 5, 8],  # Right column

    # Diagonals
    [0, 4, 8],  # Top-left to bottom-right diagonal
    [2, 4, 6],  # Top-right to bottom-left diagonal
]


def get_input(usr):
    while True:
        try:
            move = int(input("Your move User: " + usr + "( 1-9): "))
            if move in range(1, 10):
                return str(move)
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def input_tracker(input, usr, usr_var):
    global board

    choice_counter.append(input)

    counter[int(input) - 1] = usr_var
    board = board.replace(input, usr)


def check_win_condition(checker, symbol):
    for condition in winning_conditions:
        if all(checker[position] == symbol for position in condition):
            return True
    return False


def check_winner(counter):
    if check_win_condition(counter, 0):
        print("O wins")
        return True
    elif check_win_condition(counter, 1):
        print("X wins")
        return True


def main(usr, usr_var):
    global board
    print(board)

    move = get_input(usr)

    if move not in choice_counter:
        input_tracker(move, usr, usr_var)

        if check_winner(counter):
            return True
    else:
        print("The place is already full. Try again.")
        main(usr, usr_var)


def loop(total_round):
    for i in range(total_round):
        if os.name == 'nt':
            os.system('cls')  # Windows
        else:
            os.system('clear')  # Unix-like systems

        if (i % 2 == 0):
            if main("O", 0):
                break
        else:
            if main("X", 1):
                break


if __name__ == "__main__":
    loop(9)
