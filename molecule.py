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
    molecule_list = []
    file = open(filename, 'r')
    for line in file:
        if len(line) > 1:
            molecule_list.append(line[:-1])
    print molecule_list

read_file('sampleinput.txt')

'''
create_map(LIST OF FOUR STRINGS)
'''


def create_board():
    board = [ i for i in [ range(10) for j in range(10) ] ]
    return board


def add_list_to_board(index, charlist, board):
    # index 0-9 map to side ascending 10-19 map to columns across
    # return new board with added list if list fits else none
    pass


'''
match_strings( LIST OF FOUR STRINGS ): returns number of possible matches
'''


def match_string(a, b, c, d):
    # call create_board() and start with a in position one
    # loop through position for a
        # apply each ramaining items to position two
        # loop though positions for b
        # save matching positions to queue if they exist

    # filter through queue and check for position three
    # filter through queue and check for position four
    # for items still in queue, tally space in middle and return largest
    pass


'''DISPLAY RESULT'''
