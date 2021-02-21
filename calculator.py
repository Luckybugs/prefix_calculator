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
                continue
            n1 = result.pop()
            n2 = result.pop()
            val = op[e](n1, n2)
            result.append(val)

    return result[0] if len(result) == 1 else None


pres = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 0}


# part2 infix to prefex
def infix_to_prefix(expression):
    expression = expression.strip().split(' ')
    stack, res = [], []
    pop = None

    for e in reversed(expression):
        if e.isdigit():
            res.append(e)
        elif e == ')':
            stack.append(e)
        elif e == '(':
            # remove all up to the closing )
            pop = stack.pop
            while pop != ')':
                pop = stack.pop()
                if pop != ')':
                    res.append(pop)
        else:
            while len(stack) > 0 and pres[e] < pres[stack[-1]]:
                o = stack.pop()
                res.append(o)
            stack.append(e)

    res.extend(stack)
    res.reverse()
    res = ' '.join(map(str, res))  #convert to string
    return res


if __name__ == '__main__':

    infix_input = ' ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )'
    prefix_input = infix_to_prefix(infix_input)
    out = calculate_prefix(prefix_input)
    print(out)
