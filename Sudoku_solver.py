

def check(board, number, position):     # check if the number put into position in the board is valid or not
    x = check_row(board,number,position)
    y = check_col(board,number,position)
    sub_square = check_square(board,number,position)
    return x and y and sub_square

def check_row(board,number,position):
    row = position[0]
    col = position[1]

    # check row horizontal:
    for index in range(len(board[0])):
        if board[row][index] == number and col != index:  # "col!=index" let the program ignore the inserted number
            return False
    return True

def check_col(board,number,position):
    row = position[0]
    col = position[1]
    # check col vertical:
    for index in range(len(board[0])):
        if board[index][col] == number and row != index:
            return False
    return True

def check_square(board,number,position):
    row = position[0]
    col = position[1]

    # check sub-grid. the table have 9 boxes, 3 first row, 3 second row and 3 third row
    box_pos_x = col // 3  # determine where the box is horizontally
    box_pos_y = row // 3  # determine where the box is  vertically

    # multiply by 3 because each box contain 3 item horizontally and 3 item vertically
    # for example, to get to the 3rd item in the 3rd box, need to get 8th index or 3*3 = 9
    for i in range(box_pos_y * 3, box_pos_y + 3):
        for j in range(box_pos_x * 3, box_pos_x + 3):
            if board[i][j] == number and (i, j) != position:  # "(i,j)!=position" is the inserted number, ignore that
                return False
    return True


def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)

    return None     # no empty spots


def solve_board(board):   # recursively backtrack till the board is solve
    # base case:
    empty = find_empty(board)
    if not empty:     # no more empty position meaning board is solved
        return True

    else:
        (row,col) = empty  # store the empty position

        for num in range(1,10):
            status = check(board,num,(row,col)) # check if the number in position is a valid choice or not
            if status:    # number in position is "valid"
                board[row][col] = num       # insert number into board
                if solve_board(board):            # recur with the new board
                    return True
                else:
                    board[row][col] = 0  # if could not solve on prev recursive call, backtrack to the original "valid" position

        return False  # loop through all number at that position but could not find one that worked so must backtrack




def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")  # print separate line after 3 rows

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:     # print vertical line every 3 column
                print(" | ", end="")

            if j == 8:                    # print last number of each row
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + ' ', end='' )





