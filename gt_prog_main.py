from functools import reduce


def line_raze(*args):
    return reduce(lambda res, nxt: nxt + res + nxt , args)
