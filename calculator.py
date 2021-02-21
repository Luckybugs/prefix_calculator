#!/usr/bin/env python3

op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


# part1 prefix calculator
def calculate_prefix(expresion):
    result = []
    expresion = expresion.strip().split(' ')

    for e in reversed(expresion):
        if e.isdigit():
            result.append(int(e))
        else:
            n1 = result.pop()
            n2 = result.pop()
            val = op[e](n1, n2)
            result.append(val)
    return result


# part2 infix to prefex
def infix_to_prefix(input):
    pass


if __name__ == '__main__':
    prefix_input = '- / 10 + 1 1 * 1 2'
    calculate_prefix(prefix_input)
