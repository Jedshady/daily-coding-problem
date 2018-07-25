# -- coding: utf-8 --
'''
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the 'k' for 's', substitute the 'e' for 'i', and append a 'g'.

Given two strings, compute the edit distance between them.
'''
def edit_distance(str1, str2):
    '''
    Dynamic Programming
    Args:
        str1(string)
        str2(string)
    Returns:
        int
    '''
    m, n = len(str1), len(str2)

    dp = [[0] * (n+1) for i in xrange(m+1)]

    for i in xrange(n+1):
        dp[0][i] = i

    for j in xrange(m+1):
        dp[j][0] = j

    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    return dp[m][n]


def main():
    '''
    >>> edit_distance('kitten', 'sitting')
    3
    >>> edit_distance('', '')
    0
    >>> edit_distance('', 'hi')
    2
    '''
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    main()
