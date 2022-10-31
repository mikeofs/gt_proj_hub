from functools import reduce


def line_raze(*args):
    return reduce(lambda res, nxt: nxt + res + nxt + ['newgit '], args)

get_in = input()

match get_in:
    case [com , int(val)]:
        val += 20
        print(f"{com=}  ha {val=}")
    case (a1, a2, a3):
        print(a1, a2 , a3)

