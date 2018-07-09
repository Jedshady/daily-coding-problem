'''
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element
from the stream with uniform probability.
'''
'''
Note:

Let the current element's index be i.

Choose to 'remember' the current element at probability 1/i. When EOF is reached,
produced the element you remember.

At the end, for each element with index i there is a probability to be chosen:

https://stackoverflow.com/questions/23351918/select-an-element-from-a-stream-with-uniform-distributed-probability

A formal prove can be done using induction, following these guidelines.
'''
import random
random.seed(0xBADC0FFE)

def sample_gen_func(num):
    for x in xrange(num):
        yield x

def solution(sample_generator):
    sample_count = 0
    selected_sample = None

    for sample in sample_generator:
        sample_count += 1
        if random.random() <= 1.0 / sample_count:
            selected_sample = sample

    return selected_sample

def main():
    num = 1000
    print solution(sample_gen_func(num))

if __name__ == '__main__':
    main()
