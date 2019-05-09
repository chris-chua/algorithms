"""Apple Interview Question

Implement a job scheduler which takes 
in a function f and an integer n, and
calls f after n milliseconds.
"""

import time

def jobscheduler(f, n):
    time.sleep(n / 1000)
    return f()

print('Program start:', time.ctime())
print(jobscheduler(lambda: 'Function delayed: ' + time.ctime(), 2000))