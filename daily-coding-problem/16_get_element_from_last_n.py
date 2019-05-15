"""Twitter interview question

You run an e-commerce website and want to record the 
last N order ids in a log. Implement a data structure 
to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. 
i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

class OrderLog:
    """
    Using the idea of a clock, the elements are being 
    overriden when the index comes back in one circle. 
    Unlike a list, this algorithm does not require 
    the list elements to be moved forward as the 
    first element is popped.
    """
    def __init__(self, N):
        self.log = [None] * N
        self.current_index = 0

    def __repr__(self):
        return str(self.log)
    
    def record(self, order_id):
        self.log[self.current_index] = order_id
        self.current_index += 1
        if self.current_index == len(self.log):
            self.current_index = 0
    
    def get_last(self, i):
        search_idx = self.current_index - i
        return self.log[search_idx]

if __name__ == '__main__':
    log = OrderLog(5)
    log.record(1)
    log.record(2)
    assert log.log == [1, 2, None, None, None]
    log.record(3)
    log.record(4)
    log.record(5)
    assert log.log == [1, 2, 3, 4, 5]
    log.record(6)
    log.record(7)
    log.record(8)
    assert log.log == [6, 7, 8, 4, 5]
    assert log.get_last(4) == 5
    assert log.get_last(1) == 8