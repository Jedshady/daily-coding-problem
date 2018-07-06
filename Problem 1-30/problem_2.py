'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
'''

def solution(list_nums):
    '''
    Without using division, have to create a (k,v) dictionary to store the index
    and the multiplication result to the left of each num we see in first scan.
    Then create the new list by go from right to left in second run. At the same
    time, the multiplication to the right need to be stored.

    Args:
        list_nums(list): a list of numbers

    Returns:
        list: a new list
    '''
    mul_left = dict()
    mul_right = dict()

    new_list = [None] * len(list_nums)  # best practice: use None to initiate

    mul_left[-1] = 1
    for i in range(len(list_nums) - 1):
        mul_left[i] = list_nums[i] * mul_left[i - 1]

    mul_right[len(list_nums)] = 1
    for j in reversed(range(len(list_nums))[1:]):
        mul_right[j] = list_nums[j] * mul_right[j + 1]

    for i in range(len(list_nums)):
        new_list[i] = mul_left[i - 1] * mul_right[i + 1]

    return new_list

def main():
    list_nums = [1, 2, 3, 4, 5]
#    list_nums = [3, 2, 1]
#    list_nums = []
    print solution(list_nums)

if __name__ == '__main__':
    main()
