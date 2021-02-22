# Prefix & Infix Calculator

Pogram that accepts numerical calculations in prefix notation

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

If you wish to evaluate an **infix** epression add a `--i` flag:



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
- Add function to chek if its a valid expression.
- Add more tests for non valid imputs.