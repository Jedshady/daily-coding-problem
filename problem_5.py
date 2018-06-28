'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
last element of that pair. For example, car(cons(3, 4)) returns 3, and
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

def cons(a, b):
    '''
    Args:
        a(int)
        b(int)
    Returns:
        function: a function has another function 'f' as argument
    '''
    def pair(f):
        '''
        Args:
            f(function)
        Returns:
            function: that has a, b as two arguments
        '''
        return f(a, b)
    return pair


def car(func):
    '''
    Args:
        func(function)
    Returns:
        function: define the function 'f'
    '''
    # method 1
    return func(lambda x, y: x)

    # method 2
    # ------------
    # def f(a, b):
    #     return a
    # return func(f)


def cdr(func):
    '''
    Args:
        func(function)
    Returns:
        function: define the function 'f'
    '''
    return func(lambda x, y: y)


def main():
    print car(cons(3, 4))
    print cdr(cons(3, 4))


if __name__ == '__main__':
    main()
