'''
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle
numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out:

2
1.5
2
3.5
2
2
2
'''
from __future__ import division
import heapq
import random

def median(total_list=None):
    '''
    Find median of either a stream or a list
    Args:
        (total_list(list))
    Returns:
        None
    '''
    max_heap = []
    min_heap = []
    if total_list is None:  # pass a stream of random integer
        for num in random_int():
            print 'random int = ' + str(num)
            max_heap, min_heap = insert_num(max_heap, min_heap, num)
            print_median(max_heap, min_heap)

    else:   # pass a list
        if not total_list:
            print_median(max_heap, min_heap)
            return

        for i in xrange(0, len(total_list)):
            max_heap, min_heap = insert_num(max_heap, min_heap, total_list[i])
            print_median(max_heap, min_heap)


def insert_num(max_heap, min_heap, num):
    if len(max_heap) == len(min_heap) == 0:
        heapq.heappush(max_heap, -num)
    elif num < -max_heap[0]:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    return balance_heap(max_heap, min_heap)


def balance_heap(max_heap, min_heap):
    while abs(len(max_heap) - len(min_heap)) > 1:
        if len(max_heap) > len(min_heap):
            real_value = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, real_value)
        else:
            value = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -value)

    return max_heap, min_heap


def print_median(max_heap, min_heap):
    print 'max_heap = ' + str(max_heap)
    print 'min_heap = ' + str(min_heap)

    if not max_heap and not min_heap:
        print 0
        return

    if len(max_heap) == len(min_heap):
        num = (-max_heap[0] + min_heap[0]) / 2
        print int(num) if int(num) == float(num) else num
    elif len(max_heap) > len(min_heap):
        print -max_heap[0]
    else:
        print min_heap[0]


def random_int():
    for i in xrange(10):
        yield random.randint(0, 10)


def main():
    # median([])
    # median([2, 1, 5, 7, 2, 0, 5])
    median()
    # median([-1, -2, 3])


if __name__ == '__main__':
    main()
