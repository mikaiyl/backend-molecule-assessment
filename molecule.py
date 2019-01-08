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


def create_rectangle_list():
    return [(h, w) for h in range(10, 1, -1) for w in range(h, 1, -1)]


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
