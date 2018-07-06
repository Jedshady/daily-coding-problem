'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def find_max_sum(int_list):
    '''
    Use Dynamic Programming to find the max sum of non-adjacent numbers.
    Args:
        int_list(list): a list of integers that may have 0 or negative
    Returns:
        int
    '''
    if not int_list:
        return 0
    elif len(int_list) <= 2:
        return max(int_list)

    last_num = int_list[-1] # last number in the list
    with_last = find_max_sum(int_list[:-2]) + last_num  # sum include last_num
    without_last = find_max_sum(int_list[:-1])  # sum without last_num
    return max(with_last, without_last)


def main():
    # test_list = [2, 4, 6, 2, 5]
    # test_list = [5, 1, 1, 5]
    test_list = [-8, 4, -3, 2, 3, 4]
    print find_max_sum(test_list)


if __name__ == '__main__':
    main()
