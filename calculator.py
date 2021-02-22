#!/usr/bin/env python3

# part1 prefix calculator
op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


def prefix_eval(expr):
    return evaluate_rec(iter(expr.split()))

def evaluate_rec(expr_iter):
    elem = next(expr_iter)
    if elem.isdigit():
        return int(elem)

    op1 = evaluate_rec(expr_iter)
    op2 = evaluate_rec(expr_iter)
    return op[elem](op1, op2)


# part2 infix to prefex    
def infix_to_prefix(expr):
    result = convert_rec(expr.replace(' ', ''))
    return result.replace('', ' ')

def convert_rec(expr):

    # Single element. It can not be split in two parts
    if len(expr) == 1 and '(' not in expr and ')' not in expr:
        return expr
    else:
        # The first character is a bracket, which means that the first part is expression in parentheses
        if expr[0] == '(':
            i = 1
            t = 1
            head = '('
            while i >0: 
                if expr[t] == '(': i +=1
                elif expr[t] == ')': i -=1
                head = head + expr[t]
                t +=1
            if head == expr:
                #remove parentheses on both sides
                return(convert_rec(head[1:-1]))
            # The expression can be divided into two - the head has parentheses, operater and then tail
            else:
                tail = ''
                oper = ''
                oper =  oper + expr[t]
                tail = expr[t+1:]
                return  oper + '' +  convert_rec(head) + convert_rec(tail)
        # head is a single number and the operator in the middle of the two parts
        else:
            head = ''
            oper = ''
            head = head + expr[0]
            oper = oper + expr[1]
            tail = expr[2:]
            return  oper + convert_rec(head) + convert_rec(tail)


if __name__ == '__main__':
    
    i_expr = '( ( 1 * 2 ) + 3 )'
    # Convert a infix to prefix
    p_expr =infix_to_prefix(i_expr)
    print(p_expr)

    #calculate the prefix
    result = prefix_eval(p_expr)
    print(result)
