'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

# from sets import Set      # deprecated, now use 'set' directly

def solution(list_nums, target):
    '''
    Use a hash set to store the number we have seen. Then whenever we see a new
    number, check whether the difference of it and the target already in the
    hash set.

    Args:
        list_nums(list): a list of number
        target(int): the sum that is looked for

    returns:
        bool: whether there is a pair of numbers add up to target
    '''
    num_seen_set = set()
    for num in list_nums:
        if target - num in num_seen_set:
            return True
        else:
            num_seen_set.add(num)
    return False


def main():
    test_list = [10, 15, 3, 7]
    k = 17
    print solution(test_list, k)


if __name__ == '__main__':
    main()
