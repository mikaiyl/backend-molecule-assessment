#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re # noqa
import argparse # noqa


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
create_rectangle_list(): Returns list of rectangle heights and widths
'''


def create_rectangle_list():
    return [(h, w) for h in range(10, 1, -1) for w in range(h, 1, -1)]


'''
match_strings( LIST OF FOUR STRINGS ): returns number of possible matches
'''


def match_string(dims, top, bottom, left, right):
    h, w = dims
    for h0 in range(1, 12 - h):
        for w0 in range(1, 12 - w):
            if top[w0] is not left[h0]:
                continue
            for h1 in range(1, 12 - h):
                if top[w0+w-1] is not right[h1]:
                    continue
                for w1 in range(1, 12 - w):
                    if bottom[w1] is left[h0+h-1] and bottom[w1+w-1] is right[h1+h-1]: # noqa
                        #print(h0, w0, h1, w1)
                        #print(dims, top, bottom, left, right)
                        return (h - 2) * (w - 2)
    return 0


'''DISPLAY RESULT'''


def check_set(sentence):
    # swap dims
    dims = sorted(create_rectangle_list(), key=lambda x: x[0]*x[1], reverse=True) # noqa
    for i in range(0, 4):
        new_arr = sentence[i:] + sentence[:i]
        for d in dims:
            result = match_string(d, *new_arr)
            if result > 0:
                return result
    return result


def main():
    strings = read_file('sampleinput.txt')
    for i in range(0, len(strings), 4):
        four = strings[i:i+4]
        print(check_set(four))


if __name__ == '__main__':
    main()
