'''ARGPARSE'''

'''
Take input from STDIN and FILENAME and store.
'''


def parse_args():
    pass


'''PROCESS'''

'''
read_file(FILENAME): return array of lists of four string.
'''


def read_file(filename):
    # return list of lists of four strings 12 chars long
    pass


'''
create_map(LIST OF FOUR STRINGS)
'''


def create_board():
    board = [i for i in [['' for k in range(10)] for j in range(10)]]
    return board


''' add_list_to_board:
Does just that. It adds a list of charachters to an existing
Usage: add_list_to_board(0, 'AAAAAAAA', board)
'''


def add_list_to_board(index, charlist, board):
    # index 0-11 map to side ascending 12-23 map to columns across
    # return new board with added list if list fits else none
    if len(charlist) is not 12:
        print '@add_list_to_board, charlist is not 10 chars'
        return board

    if index > 0 and index < 11:
        for i, char in enumerate(charlist):
            if board[index][i] == char or board[index][i] == '':
                board[index][i] = char
            else:
                return board
    elif index > 12 and index < 23:
        for i, char in enumerate(charlist):
            if board[i][index-12] == char or board[i][index-12] == '':
                board[i][index-12] = char
            else:
                return board
    else:
        pass

    return board


'''

'''


def match_string():
    pass


'''
match_strings( LIST OF FOUR STRINGS ): returns number of possible matches
'''


def match_strings(a, b, c, d):
    # call create_board() and start with a in position one
    # loop through position for a
        # apply each ramaining items to position two
        # loop though positions for b
        # save matching positions to queue if they exist
    answers = {}

    for down in range(10):
        layer_count = 0
        board = create_board()
        board = add_list_to_board(down+1, a, board)
        for across in range(10):
            pass


    # filter through queue and check for position three
    # filter through queue and check for position four
    # for items still in queue, tally space in middle and return largest
    pass


'''DISPLAY RESULT'''
