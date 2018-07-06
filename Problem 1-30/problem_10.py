'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and
calls f after n milliseconds.
'''

'''
EdgeCases:
* Imagine a case, where (A,10) task A is scheduled to run after 10 seconds
* and then when at 3rd second, another task B comes where (B,2) seconds
* then which one would be executed first ?

A more sophisticated edge case is, if two items receive the same absolute time,
is it required to maintain order of insertion when running? Might be relevant
in some use cases. The mentioned edge case, is obvious. at 5 task B runs, at 10
task A runs.
'''

'''
Solution:
1) calculate absolute times when a task get's added
2) push it into a priority queue with smallest absolute on top (binary heap)
3) have a runner that polls the queue once in a time interval (e.g. second) and
    checks if top task is to be executed, pop items from the heap that need to
    be executed.
4) now, the question is, how long does the run take? can I execute it
    synchronously or will this delay the scheduler? I could as well span into a
    thread pool to call run there.

Also refer to following URL:
https://pymotw.com/3/sched/
'''
