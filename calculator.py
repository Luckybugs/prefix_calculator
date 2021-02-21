#!/usr/bin/env python3

op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


# part1 prefix calculator
def calculate_prefix(expression):
    result = []
    expression = expression.strip().split(' ')

    for e in reversed(expression):
        if e.isdigit():
            result.append(int(e))
        else:
            if len(result) < 2:
                return None
            n1 = result.pop()
            n2 = result.pop()
            val = op[e](n1, n2)
            result.append(val)

    return result[0] if len(result) == 1 else None


# part2 infix to prefex
def infix_to_prefix(input):
    pass


if __name__ == '__main__':
    prefix_input = '- / 10 + 1 1 * 1 '
    out = calculate_prefix(prefix_input)
    print(out)
