"""
O(1) Time | O(n) Space  worst case; 80th percentile Python perf.
"""

class MinWithCount(object):
    def __init__(self, minim, count):
        self.min = minim
        self.count = count


class MinStack(object):
    """
    Stack that supports push pop top and retrieves the min in constant time.
    """

    # define global vars
    minim = None
    count = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStackWithCount = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.minStackWithCount: #not empty
            ## if element that you are adding is equal to currentMin
            if x ==self.minStackWithCount[-1].min:
               self.minStackWithCount[-1].count =self.minStackWithCount[-1].count + 1
            elif x <self.minStackWithCount[-1].min: # We have a new min
               self.minStackWithCount.append(MinWithCount(x, 1))
        else: # min stack is empty
           self.minStackWithCount.append(MinWithCount(x, 1))

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack: # empty
            raise ValueError("pop(): empty stack")
        poppedElement = self.stack[-1]
        del self.stack[-1] # Remove the last element
        if poppedElement == self.minStackWithCount[-1].min:
            self.minStackWithCount[-1].count = self.minStackWithCount[-1].count - 1
            if (self.minStackWithCount[-1].count == 0):
                del self.minStackWithCount[-1]
        return poppedElement


    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise ValueError("top(): empty stack")
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if not self.minStackWithCount:
            raise ValueError("getMin(): empty minStack")
        return self.minStackWithCount[-1].min


# obj = MinStack()
# obj.push(3)
# obj.push(2)
# obj.push(1)
# print(obj.getMin())
# obj.push(1)
# print(obj.top())
# print(obj.pop())
# print(obj.getMin())
# print(obj.pop())
# print(obj.getMin())


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
