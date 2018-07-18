'''
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your
function should return true. The same regular expression on the string "raymond"
should return false.

Given the regular expression ".*at" and the string "chat", your function should
return true. The same regular expression on the string "chats" should return false.
'''
'''
Resource:
Youtube: https://www.youtube.com/watch?v=l3hda49XcDE
'''

def isMatch(self, s, p):
    m, n = len(s), len(p)
    DP = [[False]*(n+1) for i in range(m+1)]
    DP[0][0] = True
    for i in range(m+1):
        for j in range(1,n+1):
            if p[j-1] == '*':
                DP[i][j] = DP[i][j-2] or (i > 0 and j > 1 and (p[j-2] == '.' or 
                            s[i-1] == p[j-2]) and DP[i-1][j])
            elif i > 0 and (p[j-1] == '.' or p[j-1] == s[i-1]):
                DP[i][j] = DP[i-1][j-1]
    return DP[m][n]


def main():
    s = 'ray'
    p = '.a.'
    print isMatch(s, p)


if __name__ == '__main__':
    main()
