# Prefix & Infix Calculator

Pogram that accepts numerical calculations in prefix notation

---

## Task description:

#### Part One
You are to write a program that accepts numerical calculations in prefix notation, such as + 5 7 or - 12 * 2 6.

You can make the following assumptions:

* The system should support the operators {+, -, *, /} which all take exactly two args.
* The input literals are positive integers
* Calculations can be done in the floating-point or integer domain
* Handling division by zero is unimportant; program can crash or do anything if that arises.
* You don't need to consider operator presidence
* You are free to use any programming language of choice but please provide any requirements to run the code EG: Python version or Pip dependencies
* **Important: Your solution should be in O(1) space complexity and O(N) time complexity**

#### Sample input (caret prompt for clarity only):
```
> 3
3
> + 1 2
3
> + 1 * 2 3
7
> + * 1 2 3
5
> - / 10 + 1 1 * 1 2
3
> - 0 3
-3
> / 3 2
1 (or 1.5)
```


All assumptions from the previous task hold for this one.

#### Part Two
Implement your calculator in infix notation with support for full-parenthesized operands. It's OK to assume that all the tokens are space-separated, including the parenethesis tokens


### Sample input (caret prompt for clarity only):
```
> ( 1 + 2 )
3
> ( 1 + ( 2 * 3 ) )
7
> ( ( 1 * 2 ) + 3 )
5
> ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )
-1 (or -1.8)
```
---- 

##  Requirements:
```
Python 3.8
```

## How to use:

Navigate to the root of this repo.

To evaluate an expresson that is in **prefix** notation simply pass in the expression a a string. 

For example:

```
$ python3 calculator.py '- 12 * 2 6'
```

If you wish to evaluate an **infix** epression add a `-i` flag:



```
$  python3 calculator.py -i '( 1 + 2 )'
```

## Tests:

The tests can be found in the rooot of the repo. To run the tests:

```
python3 tests.py
```


## Notes:

- current solution for infix to prefix notation is NOT supporting multiple digit operands.(i.e a 12 somewhere in exppression will fail). Next step is to implement a solution with a list and space-separated tokens.
- add exceptions handling
- Add function to chek if its a valid expression.
- Add more tests for non valid imputs.
