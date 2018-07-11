# -*- coding:utf-8 -*-
'''
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a
Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''
import random
import math

random.seed(0xBADC0FFE)

def est_pi(num):
    cnt = 0
    total = 0
    prev_pi, pi_approx = 0, 3

    while True:
        point = list()
        for i in range(num):
            point.append((random.random(), random.random()))
            if point[i][0] ** 2 + point[i][1] ** 2 <= 1:
                cnt += 1
            total += 1
        prev_pi = pi_approx
        pi_approx = 4 * cnt / float(total)
        print 'prev_pi = {}, pi_approx = {}'.format(prev_pi, pi_approx)
        if abs(prev_pi - pi_approx) < 1e-9:    # assume we don't know math.pi
            return pi_approx
        # if abs(math.pi - pi_approx) < 1e-4:   # assume math.pi is known
        #     return pi_approx


def main():
    print est_pi(1000)


if __name__ == '__main__':
    main()
