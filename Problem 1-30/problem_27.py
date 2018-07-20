'''
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

def is_balanced_method_2(brackets):
    '''
    Reference:
    https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_26_30.py#L35

    Note:
    reduce() accept 3 arguments:
    https://stackoverflow.com/questions/19589233/reduce-function-with-three-parameters
    The third argument is used as initializer

    The functools.reduce() documentation includes a Python version of the function:
    def reduce(function, iterable, initializer=None):
        it = iter(iterable)
        if initializer is None:
            value = next(it)
        else:
            value = initializer
        for element in it:
            value = function(value, element)
    return value
    '''
    copy = None
    while brackets and brackets != copy:

        copy = brackets
        brackets = reduce(lambda s, p: s.replace(p, ''), ['()', '[]', '{}'], brackets)

    return brackets == ''


def is_balanced(brackets):
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    dictionary = {')': '(', ']': '[', '}': '{'}

    br_stack = []

    for br in brackets:
        if br in open_brackets:
            br_stack.append(br)
        elif br in close_brackets:
            if match(br_stack, br, dictionary): # balance
                br_stack.pop()
            else:
                return False
        else:
            raise ValueError('Invalid String.')

    if not br_stack:
        return True
    else:
        return False


def match(br_list, br, dic):
    if not br_list:
        return False
    else:
        if br_list[-1] == dic[br]:
            return True
        else:
            return False


def main():
    '''
    >>> is_balanced('(({[]})}')
    False

    >>> is_balanced('..{}')
    Traceback (most recent call last):
    ...
    ValueError: Invalid String.

    >>> is_balanced('([])[]({})')
    True

    >>> is_balanced('([)]')
    False

    >>> is_balanced_method_2('([])[]({})')
    True
    '''
    import doctest
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()
