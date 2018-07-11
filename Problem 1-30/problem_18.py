'''
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
[10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and
you do not need to store the results. You can simply print them out as you
compute them.

Reference:
https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
'''
from __future__ import print_function
from collections import deque

# A Deque (Double ended queue) based
# method for printing maximum element
# of all subarrays of size k
def printMax(arr, n, k):
    '''Create a Double Ended Queue, q that
    will store indexes of array elements.
    The queue will store indexes of useful
    elements in every window and it will
    maintain decreasing order of values from
    front to rear in q, i.e., arr[q.front[]]
    to arr[q.rear()] are sorted in decreasing
    order.

    Args:
        arr(list): input array of integers
        n(int): length of input array
        k(int): window size

    Returns:
        None
    '''
    q = deque()

    # Process first k (or first window)
    # elements of array
    for i in range(k):

        # For every element, the previous
        # smaller elements are useless
        # so remove them from q
        while q and arr[i] >= arr[q[-1]] :
            q.pop()

        # Add new element at rear of queue
        q.append(i)

    # Process rest of the elements, i.e.
    # from arr[k] to arr[n-1]
    for i in range(k, n):

        # The element at the front of the
        # queue is the largest element of
        # previous window, so print it
        print(str(arr[q[0]]) + " ", end = "")

        # Remove the elements which are
        # out of this window
        while q and q[0] <= i-k:

            # remove from front of deque
            q.popleft()

        # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while q and arr[i] >= arr[q[-1]] :
            q.pop()

        # Add current element at the rear of q
        q.append(i)

    # Print the maximum element of last window
    print(str(arr[q[0]]))


def main():
    test_arr = [10, 5, 2, 7, 8, 7]
    k = 3
    printMax(test_arr, len(test_arr), k)


if __name__ == '__main__':
    main()
