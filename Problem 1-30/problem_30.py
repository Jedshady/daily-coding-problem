'''
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional
elevation map where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1)
space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in
the second, and 3 in the fourth index (we cannot hold 5 since it would run off
to the left), so we can trap 8 units of water.
'''
'''
Note:
https://www.geeksforgeeks.org/trapping-rain-water/

https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_26_30.py#L129
'''
def water_cnt(arr):
    water = 0

    while len(arr) > 2:
        # the idea is: from the smallest left/right boundary, accumulate water
        # level until reaching a higher wall inside. Then recurse with with the
        # new bound, until only two array entries.
        lval = arr[0]
        rval = arr[-1]
        if lval <= rval:

            cnt = 1
            while arr[cnt] < arr[0]:
                water += arr[0] - arr[cnt]
                cnt += 1

            arr = arr[cnt:]

        else:

            cnt = -2
            while arr[cnt] < arr[-1]:
                water += arr[-1] - arr[cnt]
                cnt -= 1

            arr = arr[:cnt + 1]
        # print water, arr
    return water


def main():
    '''
    >>> arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    >>> water_cnt(arr)
    6

    >>> arr = [3, 0, 1, 3, 0, 5]
    >>> water_cnt(arr)
    8

    >>> arr = [2, 1, 2]
    >>> water_cnt(arr)
    1
    '''
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
