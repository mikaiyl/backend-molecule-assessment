#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re # noqa
import argparse # noqa
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
    molecule_list = []
    file = open(filename, 'r')
    for line in file:
        if len(line) > 1:
            molecule_list.append(line[:-1])
    return molecule_list


'''
create_map(LIST OF FOUR STRINGS)
'''


def create_board():
    board = [i for i in [[' ' for k in range(12)] for j in range(12)]]
    return board


''' HELPERS '''


def print_map(m):
    if m is None:
        print 'Empty'
    else:
        for line in m:
            print line
    print '\n\n'


''' add_list_to_board:
Does just that. It adds a list of charachters to an existing
Usage: add_list_to_board(0, 'AAAAAAAA', board)
'''


def add_string_to_board(index, string, old_board, offset = 0): # noqa
    # index 0-9 map to side ascending 10-19 map to columns across
    # return new board with added list if list fits else none
    if len(string) is not 12:
        print '@add_list_to_board, charlist is not 12 chars'
        return None

    board = copy.deepcopy(old_board)
    b = copy.deepcopy(board)
    charlist = ' ' * offset + string[:12-offset] if offset > 0 else string[abs(offset):] + ' ' * abs(offset) # noqa
    if index > 0 and index < 11:
        for i, char in enumerate(charlist):
            if board[index][i] == char or board[index][i] == ' ':
                board[index][i] = char
            else:
                print('returning b, char: {}, at {}x{}'.format(char, i, index)) # noqa
                return b
    elif index > 12 and index < 23:
        for i, char in enumerate(charlist):
            if board[i][index-12] == char or board[i][index-12] == ' ':
                board[i][index-12] = char
            else:
                print('returning b, char: {}, at {}x{}'.format(char, i, index-12)) # noqa
                return b
    else:
        return None
    return board


def find_space_on_board(charlist, board, buffer = []): # noqa
    # index 0-11 map to side ascending 12-23 map to columns across
    # return new board with added list if list fits else none
    match_tuples = []
    if len(charlist) is not 12:
        print '@add_list_to_board, charlist is not 12 chars'
        return None

    for index in range(1, 23):
        print index
        if index in buffer:
            pass
        elif index > 0 and index < 11:
            vectors = []
            for i, char in enumerate(charlist):
                if i == 0 and board[index][i] is not ' ':
                    buffer += [index-1, index, index+1]
                    break
                elif i not in [0, 11] and board[index][i] in 'ABCDEFGHIJKLMNOP': # noqa
                    for j, c in enumerate(charlist):
                        if c == board[index][i] and j not in [0, 11]:
                            vectors.append(i-j)
            if vectors:
                match_tuples.append((index, vectors))
        elif index > 12 and index < 23:
            vectors = []
            for i, char in enumerate(charlist):
                if i == 0 and board[i][index-12] is not ' ' or board[i][index-12] is not char: # noqa
                    buffer += [index-1, index, index+1]
                    break
                elif i not in [0, 11] and board[i][index-12] in 'ABCDEFGHIJKLMNOP': # noqa
                    for j, c in enumerate(charlist):
                        if c == board[i][index-12] and j not in [0, 11]:
                            vectors.append(i-j)
            if vectors:
                match_tuples.append((index, vectors))
        else:
            pass

    return filter(lambda x: x[0] not in buffer, match_tuples)


''' get first degree  '''


def get_first_degree(a, b, c, d):
    items = [b, c, d]
    results = []
    for el in items:
        matches = []
        for i, c in enumerate(el):
            if c not in a or i in [0, 11]:
                pass
            else:
                m = []
                for j, d in enumerate(a):
                    if d == c and j not in [0, 11]:
                        m.append(j)
                matches.append((i, m))
        results.append((el, matches))

    for r in results:
        s1 = a
        s2 = r[0]

        print('s1: {}, s2: {}'.format(s1, s2))
        for i2, ia2 in r[1]:
            print('i2: {}'.format(i2))
            for i1 in ia2:
                # matches = {}
                b2 = add_string_to_board(int(i1) + 12, s2, add_string_to_board(int(i2), s1, create_board())) # noqa
                print('\nb2\n\n')
                print_map(b2)
                print('s2: {}, items: {}'.format(s2, items))
                for s3 in filter(lambda w: w is not s2, items):
                    #
                    sp1 = find_space_on_board(s3, b2, [i1+12, i2])
                    print('s1: {}'.format(sp1))
                    for i3, va1 in sp1:
                        for offset in va1:
                            b3 = add_string_to_board(i3, s3, b2, offset) # noqa
                            print('\nb3\n\n')
                            print_map(b3)
                            print('i1: {}\ni2: {}\ni3: {}\n'.format(i1, i2, i3)) # noqa
                            print('s1: {}\ns2: {}\ns3: {}\n'.format(s1, s2, s3)) # noqa
                            s4 = filter(lambda e: e not in [s2, s3], items)[0]
                            sp2 = find_space_on_board(s4, b3) # noqa
                            for i4, va2 in sp2:
                                for offset0 in va2:
                                    b4 = add_string_to_board(i4, s4, b3, offset0) # noqa
                                    print_map(b4)
    return results
    # return (a, results)


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


if __name__ == '__main__':
    for line in read_file('sampleinput.txt'):
        print line
