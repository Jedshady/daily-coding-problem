'''
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different
colors. He has a goal of minimizing cost while ensuring that no two neighboring
houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to
build the nth house with kth color, return the minimum cost which achieves this
goal.
'''
def solution(costs):
    '''
    DP by adding a house at a time
    Args:
        costs(list of list)
    Returns:
        int
    '''
    best_cost = [0] * len(costs[0])
    for cost in costs:  # add a house at a time
        temp_cost = [0] * len(costs[0])
        for index in xrange(len(cost)):
            # best cost is the one for that color plus min cost between every other color
            temp_cost[index] = cost[index] + min(best_cost[:index] +
                                                    best_cost[index + 1:])
        best_cost = temp_cost
        print best_cost

    return min(best_cost)


def main():
    costs = [[2, 1, 1],
            [1, 10, 3],
            [1, 2, 100]]
    print solution(costs)

if __name__ == '__main__':
    main()
