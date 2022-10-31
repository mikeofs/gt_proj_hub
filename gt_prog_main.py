from functools import reduce


def line_raze(*args):
    return reduce(lambda res, nxt: res + nxt, args)
