'''
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you
can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb
any number from a set of positive integers X? For example, if X = {1, 3, 5}, you
could climb 1, 3, or 5 steps at a time.
'''
def cache(func):
    data = dict()
    def wrapper(N, X):
        if N in data:
            return data[N]
        else:
            data[N] = func(N, X)
            return data[N]
    return wrapper


@cache
def climb_up(N, X):
    '''
    Dynamic Programming
    Args:
        N(int): a staircase with N steps
        X(list): steps that are allowed
    Returns:
        int: number of ways to get to the top of the staircase
    '''
    if N <= 1:
        return 1

    num_ways = 0
    for step in X:
        if N >= step:
            num_ways += climb_up(N - step, X)
    return num_ways


def main():
    print climb_up(100, [1, 3, 5])

if __name__ == '__main__':
    main()
