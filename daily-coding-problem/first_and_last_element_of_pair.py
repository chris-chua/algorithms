"""Jane Street interview question

cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair.

Given this implementation of cons:
    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair

Implement car and cdr.

https://stackoverflow.com/questions/52481607/dont-understand-the-inner-function-in-python

Example:
>>> print(car(cons(3, 4)))
3

>>> print(cdr(cons(3, 4)))
4
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def get_first(a, b):
        return a
    return pair(get_first)

def cdr(pair):
    def get_last(a, b):
        return b
    return pair(get_last)

if __name__ == '__main__':
    import doctest
    doctest.testmod()