'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.
'''
def solution(alist):
    '''
    Use the index of the list to denote whether we have seen this number.
    For example:
        We see 2, then change the number on index 2 from + to -.
        [2, 4, 1]  -->  [2, 4, -1]

    ------
    Args:
        alist(list): a list of numbers may includes duplicates and negative
    Returns:
        int: the smallest positive integer missing in the given list
    '''
    pos_list = remove_negative(alist)
    smart_list = modify_index(pos_list)
    smallest_pos = find_smallest_pos(smart_list)
    return smallest_pos


def remove_negative(alist):
    '''
    Args:
        alist(list): a list of numbers may includes duplicates and negative
    Returns:
        list: a list of numbers may includes only duplicates, no negative and 0
    '''
    # filter seems not an in-place modification
    # new_list = list(filter(lambda x: x > 0, alist))

    # following is not an in-place way either
    # alist = [x for x in alist if x > 0]

    # finally, this seems like an in-place operate as the id(alist) remains same
    # correct me if I'm wrong
    alist[:] = [x for x in alist if x > 0]
    return alist


def modify_index(pos_list):
    '''
    Args:
        pos_list(list)
    Returns:
        list
    '''
    for num in pos_list:
        if abs(num) - 1 < len(pos_list) and pos_list[abs(num) - 1] > 0:
            pos_list[abs(num) - 1] = - pos_list[abs(num) - 1]
    return pos_list


def find_smallest_pos(smart_list):
    '''
    Args:
        smart_list(list)
    Returns:
        int
    '''
    for idx, num in enumerate(smart_list):
        if num > 0:
            return idx + 1
    return len(smart_list) + 1


def main():
    # test_list = [3, 4, -1, 1]
    # test_list = [1, 2, 0]
    # test_list = [2, 4, -8, 10, 15, 0, 0 , -1]
    test_list = [0, 0, 0]
    print solution(test_list)


if __name__ == '__main__':
    main()
