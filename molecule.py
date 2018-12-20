import copy

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
    board = [i for i in [[' ' for k in range(12)] for j in range(12)]]
    return board


''' add_list_to_board:
Does just that. It adds a list of charachters to an existing
Usage: add_list_to_board(0, 'AAAAAAAA', board)
'''


def add_list_to_board(index, charlist, board):
    # index 0-11 map to side ascending 12-23 map to columns across
    # return new board with added list if list fits else none
    b = copy.deepcopy(board)

    if len(charlist) is not 12:
        print '@add_list_to_board, charlist is not 12 chars'
        return None

    if index > 0 and index < 11:
        for i, char in enumerate(charlist):
            if board[index][i] == char or board[index][i] == ' ':
                board[index][i] = char
            else:
                return b
    elif index > 12 and index < 23:
        for i, char in enumerate(charlist):
            if board[i][index-12] == char or board[i][index-12] == ' ':
                board[i][index-12] = char
            else:
                return b
    else:
        return None
    return board


''' add_list_to_board:
Does just that. It adds a list of charachters to an existing
Usage: add_list_to_board(0, 'AAAAAAAA', board)
'''


def find_space_on_board(charlist, board):
    # index 0-11 map to side ascending 12-23 map to columns across
    # return new board with added list if list fits else none
    matching_rows = []
    matching_cols = []

    buffer = []

    if len(charlist) is not 12:
        print '@add_list_to_board, charlist is not 12 chars'
        return None

    for index in range(0, 23):
        if index > 0 and index < 11:
            for i, char in enumerate(charlist):
                if board[index][i] == char or board[index][i] == ' ':
                    pass
                elif i == 0:
                    buffer += [i-1, i, i+1]
                    break
                else:
                    break

            matching_rows.append(index)
        elif index > 12 and index < 23:
            for i, char in enumerate(charlist):
                if board[i][index-12] == char or board[i][index-12] == ' ':
                    pass
                elif i == 0:
                    buffer += [i-1, i, i+1]
                    break
                else:
                    break
            matching_cols.append(index)
        else:
            pass

    return filter(lambda x: x not in buffer, matching_rows + matching_cols)


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
    # answers = []
    s_list = [b, c, d]

    for down in range(1, 11):
        _board_ = create_board()
        board = add_list_to_board(down, a, _board_)
        for across in range(12, 23):
            print('\nrow: {}, column: {}\n\n'.format(down, across))
            for side_2 in s_list:
                b2 = add_list_to_board(across, side_2, board)
                print_map(b2)
                del(b2)
                # if b2 is not None:
        del(board)

    # filter through queue and check for position three
    # filter through queue and check for position four
    # for items still in queue, tally space in middle and return largest


''' HELPERS '''


def print_map(m):
    if m is None:
        print 'Empty'
    else:
        for line in m:
            print line



'''DISPLAY RESULT'''
